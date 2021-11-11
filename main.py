# make sure to install these packages before running:
# pip install sodapy
# pip install pymysql

from sodapy import Socrata
import json
import pymysql

# You can use my app token
client = Socrata("data.sfgov.org", "ci42oqHV99DT538i5oLhOevEf")

conn = pymysql.connect(host='localhost', user='your_user', passwd='your_password', db='mysql')
cur = conn.cursor()

columns_schema = {
    'incident_number': 'int'
    , 'exposure_number': 'int'
    , 'id': 'text'
    , 'address': 'text'
    , 'incident_date': 'text'
    , 'call_number': 'text'
    , 'alarm_dttm': 'text'
    , 'arrival_dttm': 'text'
    , 'close_dttm': 'text'
    , 'city': 'text'
    , 'zipcode': 'text'
    , 'battalion': 'text'
    , 'station_area': 'text'
    , 'box': 'text'
    , 'suppression_units': 'int'
    , 'suppression_personnel': 'int'
    , 'ems_units': 'int'
    , 'ems_personnel': 'int'
    , 'other_units': 'int'
    , 'other_personnel': 'int'
    , 'first_unit_on_scene': 'text'
    , 'estimated_property_loss': 'int'
    , 'estimated_contents_loss': 'int'
    , 'fire_fatalities': 'int'
    , 'fire_injuries': 'int'
    , 'civilian_fatalities': 'int'
    , 'civilian_injuries': 'int'
    , 'number_of_alarms': 'int'
    , 'primary_situation': 'text'
    , 'mutual_aid': 'text'
    , 'action_taken_primary': 'text'
    , 'action_taken_secondary': 'text'
    , 'action_taken_other': 'text'
    , 'detector_alerted_occupants': 'text'
    , 'property_use': 'text'
    , 'area_of_fire_origin': 'text'
    , 'ignition_cause': 'text'
    , 'ignition_factor_primary': 'text'
    , 'ignition_factor_secondary': 'text'
    , 'heat_source': 'text'
    , 'item_first_ignited': 'text'
    , 'human_factors_associated_with_ignition': 'text'
    , 'structure_type': 'text'
    , 'structure_status': 'text'
    , 'floor_of_fire_origin': 'int'
    , 'fire_spread': 'text'
    , 'no_flame_spead': 'text'
    , 'number_of_floors_with_minimum_damage': 'int'
    , 'number_of_floors_with_significant_damage': 'int'
    , 'number_of_floors_with_heavy_damage': 'int'
    , 'number_of_floors_with_extreme_damage': 'int'
    , 'detectors_present': 'text'
    , 'detector_type': 'text'
    , 'detector_operation': 'text'
    , 'detector_effectiveness': 'text'
    , 'detector_failure_reason': 'text'
    , 'automatic_extinguishing_system_present': 'text'
    , 'automatic_extinguishing_sytem_type': 'text'
    , 'automatic_extinguishing_sytem_perfomance': 'text'
    , 'automatic_extinguishing_sytem_failure_reason': 'text'
    , 'number_of_sprinkler_heads_operating': 'int'
    , 'supervisor_district': 'text'
    , 'neighborhood_district': 'text'
    , 'point': 'point'
}

if __name__ == '__main__':
    query_max = 'SELECT COALESCE(MAX(incident_number),0) as last_id FROM your_schema.fire_incidents;'
    cur.execute(query_max)
    db_last_id = cur.fetchall()[0][0]
    sfgov_last_id = db_last_id

    # feel free to change this limit
    limit_param = 1000
    next_page = True
    while next_page:
        # redundant but safe
        cur.execute(query_max)
        db_last_id = cur.fetchall()[0][0]
        # print(last_id)
        results = client.get("wr8u-xric"
                             , where="incident_number > @last".replace('@last', str(db_last_id))
                             , order="incident_number asc"
                             , limit=limit_param)
        # print(json.dumps(results, indent=4, sort_keys=True))
        rows_array = []
        if results:
            for r in results:
                values_array = []
                for col_name in columns_schema.keys():
                    col_type = columns_schema[col_name]
                    if r.get(col_name):
                        if col_type == 'point':
                            # latitude
                            col_value = str(r.get(col_name).get('coordinates')[0])
                            values_array.append(col_value)
                            # longitude
                            col_value = str(r.get(col_name).get('coordinates')[1])
                            values_array.append(col_value)
                        else:
                            col_value = r.get(col_name)
                            if col_type == 'text':
                                # had to remove quotes in text
                                values_array.append('\''+col_value.replace('\'', ' ')+'\'')
                            else:
                                values_array.append(col_value)
                    # there's some rows with empty point
                    elif col_type == 'point':
                        # latitude
                        values_array.append('NULL')
                        # longitude
                        values_array.append('NULL')
                    else:
                        values_array.append('NULL')
                separator = ','
                insert_values = separator.join(values_array)
                rows_array.append('('+insert_values+')')
                sfgov_last_id = r['incident_number']

            print('from ' + str(db_last_id) + ' to ' + str(sfgov_last_id))
            db_last_id = sfgov_last_id
            separator = ','
            insert_rows = separator.join(rows_array)
            query_str = 'INSERT INTO your_schema.fire_incidents values '+insert_rows+';'
            # print(query_str)
            cur.execute(query_str)
            conn.commit()
        else:
            next_page = False
            print('no new data')

