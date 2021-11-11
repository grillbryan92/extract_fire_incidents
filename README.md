
This script is meant to be executed on demand or on a daily basis as preferred. It will work correctly either way.\
I used a MySql MariaDB database as it was the option I already had installed locally, although I would have preferred using redshift and S3 for bulk inserts.\
I assumed that no row at the source is edited after published, so the ETL works incrementally without any deletions at destiny.\
It's a single file script for the sake of simplicity and avoid import issues which vary with python versions or os (mine is python3).\
Would have been nicer to have credentials on a config file and also the column's schema on a separate file.\
At the file setup.sql you'll find the due DDL for the final table.\
Also you'll have to replace 'your_schema' for the correct one on the script.

Work process:\
    1. Configure credentials and socrata client to get a first sample of the data.\
    2. Create a first version of the target table by copying the schema from the doc.\
    3. Parse a data sample and generate an INSERT statement.\
    4. Configure request to order and filter by incident number.\
    5. Iterate incrementally by playing with offset and limit, then discarded offset to use always the last id from the database.\
    6. In parallel troubleshooting data issues such as empty fields (which json omits from the schema), removing quotes and finding the right datatype for the db table. 

The file incidents_report.sql contains averages of arrival time and injuries/fatalities segmented by month and district for the current year.\
I thought there could be an interesting correlation although luckily the injuries and fatalities are almost always 0.
