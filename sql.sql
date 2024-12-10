USE DATABASE BI_PROJECT;
USE SCHEMA PUBLIC;

-- Top 5 des stades par capacité
SELECT TOP 5 "rank", "stadium", "capacity"  
FROM "BI_PROJECT"."PUBLIC"."BI"  
ORDER BY "capacity" DESC;  

-- Moyenne de capacité par région
SELECT "region", AVG("capacity") as avg_capacity
FROM "BI_PROJECT"."PUBLIC"."BI"  
GROUP BY "region"
ORDER BY avg_capacity DESC;

-- Nombre de stades par pays
SELECT "country", COUNT(*) as stadium_count
FROM "BI_PROJECT"."PUBLIC"."BI"  
GROUP BY "country"
ORDER BY stadium_count DESC, "country" ASC;

-- Classement des stades par région
SELECT "rank", "stadium", "region",
    RANK() OVER(PARTITION BY "region" ORDER BY "capacity" DESC) as region_rank
FROM "BI_PROJECT"."PUBLIC"."BI";

-- Top 3 des stades par région
WITH ranked_stadiums AS (
    SELECT "rank", "stadium", "region", "capacity",
           RANK() OVER (PARTITION BY "region" ORDER BY "capacity" DESC) as region_rank
    FROM "BI_PROJECT"."PUBLIC"."BI"
)
SELECT "rank", "stadium", "region", "capacity", region_rank
FROM ranked_stadiums
WHERE region_rank <= 3;

-- Stades au-dessus de la moyenne régionale
WITH regional_avg AS (
    SELECT "region", AVG("capacity") as avg_capacity 
    FROM "BI_PROJECT"."PUBLIC"."BI"
    GROUP BY "region"
)
SELECT s."stadium", s."region", s."capacity", ra.avg_capacity
FROM "BI_PROJECT"."PUBLIC"."BI" s
JOIN regional_avg ra ON s."region" = ra."region"
WHERE s."capacity" > ra.avg_capacity
ORDER BY s."region";

-- Stades les plus proches de la médiane par région
WITH MedianCTE AS (
    SELECT 
        "region", 
        PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY "capacity") AS median_capacity
    FROM "BI_PROJECT"."PUBLIC"."BI"
    GROUP BY "region"
),
RankedStadiums AS (
    SELECT
        s."rank", 
        s."stadium", 
        s."region", 
        s."capacity",
        m.median_capacity,
        ROW_NUMBER() OVER (PARTITION BY s."region" ORDER BY ABS(s."capacity" - m.median_capacity)) AS median_rank
    FROM "BI_PROJECT"."PUBLIC"."BI" s
    JOIN MedianCTE m ON s."region" = m."region"
)
SELECT "rank", "stadium", "region", "capacity", median_capacity, median_rank
FROM RankedStadiums
WHERE median_rank = 1;

-- Affichage des 10 premières lignes
SELECT * 
FROM "BI_PROJECT"."PUBLIC"."BI"
LIMIT 10;