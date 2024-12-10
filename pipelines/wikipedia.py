import json
import os
import re
import requests
import pandas as pd
from bs4 import BeautifulSoup
from geopy import Nominatim
from datetime import datetime

# Constants
NO_IMAGE = 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/No-image-available.png/480px-No-image-available.png'

def get_wikipedia_page(url):
    """
    Fetch the HTML content of the Wikipedia page.
    
    Args:
        url (str): URL of the Wikipedia page
    
    Returns:
        str: HTML content of the page
    """
    print("debut de la fonction pour get_wikipedia_page")
    print("Getting wikipedia page...", url)
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"An error occurred while fetching the page: {e}")
        return None
def extract_stadium_data(html):
    """
    Extract stadium data from Wikipedia HTML.
    
    Args:
        html (str): HTML content of the page
    
    Returns:
        list: Extracted stadium data
    """
    print("debut de la fonction pour extract_stadium_data")
    if not html:
        return []

    soup = BeautifulSoup(html, 'html.parser')
    
    # Try multiple table finding strategies
    table_strategies = [
        soup.find_all("table", class_=lambda x: x and all(c in x.split() for c in ["wikitable", "sortable"])),
        soup.find_all("table", {"class": "wikitable sortable"}),
        soup.find_all("table", {"class": "sortable wikitable"}),
        soup.find_all("table", class_="wikitable"),
    ]
    
    table = None
    for strategy in table_strategies:
        if strategy:
            table = strategy[0]
            break
    
    if not table:
        print("No suitable table found on the page.")
        return []

    # Find table rows
    rows = table.find_all('tr')
    
    if len(rows) < 2:
        print("Not enough rows in the table.")
        return []

    # Extract data
    stadiums = []
    headers = [clean_text(th.text) for th in rows[0].find_all(['th', 'td'])]
    
    for row in rows[1:]:
        cells = row.find_all(['td', 'th'])
        
        if len(cells) < 7:
            continue
        
        try:
            stadium_data = {
                'rank': len(stadiums) + 1,
                'stadium': clean_text(cells[0].text),
                'capacity': clean_text(cells[1].text).replace(',', '').replace('.', ''),
                'region': clean_text(cells[2].text) if len(cells) > 2 else '',
                'country': clean_text(cells[3].text) if len(cells) > 3 else '',
                'city': clean_text(cells[4].text) if len(cells) > 4 else '',
                'images': ('https:' + cells[5].find('img').get('src').split("//")[1]) if cells[5].find('img') else NO_IMAGE,
                'home_team': clean_text(cells[6].text) if len(cells) > 6 else ''
            }
            
            # Validate capacity is numeric
            try:
                stadium_data['capacity'] = int(re.sub(r'\D', '', stadium_data['capacity']))
            except ValueError:
                stadium_data['capacity'] = 0
            
            stadiums.append(stadium_data)
        
        except Exception as e:
            print(f"Error processing row: {e}")
    
    return stadiums
def clean_text(text):
    """
    Clean and normalize text data.
    
    Args:
        text (str): Input text to clean
    
    Returns:
        str: Cleaned text
    """
    print("debut de la fonction pour clean_text")
    if not text:
        return ""
    
    text = str(text).strip()
    
    # Remove references, annotations, and extra information
    text = re.sub(r'\[.*?\]', '', text)  # Remove square bracket annotations
    text = re.sub(r'\(.*?\)', '', text)  # Remove parentheses and content
    
    # Remove special characters and extra whitespace
    text = re.sub(r'\s+', ' ', text)
    text = text.replace('&nbsp', '').replace('♦', '').strip()
    
    return text
def get_lat_long(country, location_name):   
    """
    Get latitude and longitude for a given location.
    
    Args:
        country (str): Country name
        location_name (str): Location name (city or stadium)
    
    Returns:
        tuple or None: Latitude and longitude, or None if not found
    """
    print("debut de la fonction pour get_lat_long")
    try:
        geolocator = Nominatim(user_agent='stadium_locator')
        
        # Try multiple location search strategies
        location_searches = [
            f"{location_name}, {country}",
            f"{country}, {location_name}",
            location_name,
            country
        ]
        
        for search_query in location_searches:
            location = geolocator.geocode(search_query)
            if location:
                return (location.latitude, location.longitude)
        
        return None
    
    except Exception as e:
        print(f"Geolocation error for {location_name}, {country}: {e}")
        return None

def transform_wikipedia_data(stadiums_data):
    """
    Transform and enrich stadium data.
    
    Args:
        stadiums_data (list): Raw stadium data
    
    Returns:
        pd.DataFrame: Transformed stadium data
    """
    print("debut de la fonction pour transform_wikipedia_data")
    stadiums_df = pd.DataFrame(stadiums_data)
    
    # Add geolocation
    stadiums_df['location'] = stadiums_df.apply(
        lambda row: get_lat_long(row['country'], row['stadium']), 
        axis=1
    )
    
    # Ensure images are valid
    stadiums_df['images'] = stadiums_df['images'].apply(
        lambda x: x if x and x != 'NO_IMAGE' else NO_IMAGE
    )
    
    return stadiums_df

def write_wikipedia_data(stadiums_df, output_dir='data'):
    """
    Write stadium data to CSV.
    
    Args:
        stadiums_df (pd.DataFrame): Stadium data
        output_dir (str, optional): Output directory
    
    Returns:
        str: Path to saved CSV file
    """
    print("debut de la fonction pour write_wikipedia_data")
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate unique filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f'stadiums_data_{timestamp}.csv'
    filepath = os.path.join(output_dir, filename)
    
    # Save to CSV
    stadiums_df.to_csv(filepath, index=False)
    print(f"Data saved to {filepath}")
    
    return filepath

def wikipedia_stadiums_pipeline(url):
    """
    Complete pipeline to extract, transform, and save stadium data.
    
    Args:
        url (str): Wikipedia page URL
    
    Returns:
        pd.DataFrame: Processed stadium data
    """
    print("debut de la fonction pour wikipedia_stadiums_pipeline")
    # Fetch HTML
    html = get_wikipedia_page(url)
    
    # Extract data
    stadiums_data = extract_stadium_data(html)
    
    if not stadiums_data:
        raise ValueError("No stadium data could be extracted.")
    
    # Transform data
    stadiums_df = transform_wikipedia_data(stadiums_data)
    
    # Write data
    write_wikipedia_data(stadiums_df)
    
    return stadiums_df

def main():
    """
    Main execution function.
    """
    print("debut de la fonction pour main")
    try:
        url = "https://en.wikipedia.org/wiki/List_of_association_football_stadiums_by_capacity"
        stadiums = wikipedia_stadiums_pipeline(url)
        
        # Display basic information
        print("\nStadium Data Overview:")
        print(f"Total Stadiums: {len(stadiums)}")
        print("\nFirst 5 Stadiums:")
        print(stadiums[['stadium', 'capacity', 'country']].head())
    
    except Exception as e:
        print(f"Pipeline execution failed: {e}")

if __name__ == "__main__":
    main()
