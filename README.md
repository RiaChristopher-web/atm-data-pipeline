# atm-data-pipeline

This project simulates an ATM data ingestion pipeline.

Steps:
1. Fetch ATM data from a simulated API feed.
2. Run pipeline every hour.
3. Apply business rules for state segregation.
4. Store each state's data into separate database tables.

Business Rules
- Data segregated by STATE
- Each state stored in separate database tables
- Pipeline runs every hour

Tech Stack
Python
Pandas
SQLite
AWS

Data Source

This project uses an ATM dataset sourced from Kaggle.

- The dataset was used to simulate a real-time ATM data feed.
- Since a live REST API was not available, the dataset acts as a mock data source for pipeline development and testing.
- The data is processed periodically to mimic hourly ingestion.

Dataset Link: https://www.kaggle.com/datasets/akhshhh/atm-bob-transaction-dataset
