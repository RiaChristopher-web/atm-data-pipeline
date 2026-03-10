# atm-data-pipeline

This project simulates an ATM data ingestion pipeline.

Steps:
1. Fetch ATM data from a simulated API feed.
2. Run pipeline every hour.
3. Apply business rules for state segregation.
4. Store each state's data into separate database tables.
5. Ready for AWS and Snowflake integration.

Business Rules
- Data segregated by STATE
- Each state stored in separate database tables
- Pipeline runs every hour

Tech Stack
Python
Pandas
SQLite
AWS
Snowflake
