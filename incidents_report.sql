SELECT DATE_FORMAT(incident_date, '%Y-%m-01') AS incident_month
, neighborhood_district
, COUNT(DISTINCT incident_number) AS total_incidents
, AVG(TIMESTAMPDIFF(SECOND, alarm_dttm, arrival_dttm)) AS avg_arrival_seconds
, AVG(fire_fatalities) AS avg_fire_fatalities
, AVG(fire_injuries) AS avg_fire_injuries
, AVG(civilian_fatalities) AS avg_civilian_fatalities
, AVG(civilian_injuries) AS avg_civilian_injuries
FROM your_schema.fire_incidents
WHERE incident_date >= '2021-01-01'
GROUP BY 1,2
ORDER BY 1,2;