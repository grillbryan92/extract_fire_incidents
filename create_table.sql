CREATE TABLE your_schema.fire_incidents (
incident_number int NOT NULL
,exposure_number int NOT NULL
,id text
,address text
,incident_date DATETIME
,call_number text
,alarm_dttm DATETIME
,arrival_dttm DATETIME
,close_dttm DATETIME
,city text
,zipcode text
,battalion varchar(100) NOT NULL
,station_area text
,box text
,suppression_units int DEFAULT NULL
,suppression_personnel int DEFAULT NULL
,ems_units int DEFAULT NULL
,ems_personnel int DEFAULT NULL
,other_units int DEFAULT NULL
,other_personnel int DEFAULT NULL
,first_unit_on_scene text
,estimated_property_loss int DEFAULT NULL
,estimated_contents_loss int DEFAULT NULL
,fire_fatalities int DEFAULT NULL
,fire_injuries int DEFAULT NULL
,civilian_fatalities int DEFAULT NULL
,civilian_injuries int DEFAULT NULL
,number_of_alarms int DEFAULT NULL
,primary_situation text
,mutual_aid text
,action_taken_primary text
,action_taken_secondary text
,action_taken_other text
,detector_alerted_occupants text
,property_use text
,area_of_fire_origin text
,ignition_cause text
,ignition_factor_primary text
,ignition_factor_secondary text
,heat_source text
,item_first_ignited text
,human_factors_associated_with_ignition text
,structure_type text
,structure_status text
,floor_of_fire_origin int DEFAULT NULL
,fire_spread text
,no_flame_spead text
,number_of_floors_with_minimum_damage int DEFAULT NULL
,number_of_floors_with_significant_damage int DEFAULT NULL
,number_of_floors_with_heavy_damage int DEFAULT NULL
,number_of_floors_with_extreme_damage int DEFAULT NULL
,detectors_present text
,detector_type text
,detector_operation text
,detector_effectiveness text
,detector_failure_reason text
,automatic_extinguishing_system_present text
,automatic_extinguishing_sytem_type text
,automatic_extinguishing_sytem_perfomance text
,automatic_extinguishing_sytem_failure_reason text
,number_of_sprinkler_heads_operating int DEFAULT NULL
,supervisor_district varchar(100) -- NOT NULL
,neighborhood_district varchar(100) -- NOT NULL
,point_lat float
,point_long float
,PRIMARY KEY (`incident_number`,`exposure_number`)
,KEY `fire_incidents_incident_number` (`incident_number`)
,KEY `fire_incidents_incident_date` (`incident_date`)
,KEY `fire_incidents_supervisor_district` (`supervisor_district`)
,KEY `fire_incidents_neighborhood_district` (`neighborhood_district`)
,KEY `fire_incidents_battalion` (`battalion`));