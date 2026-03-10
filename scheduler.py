import time

from fetch_api import get_atm_data
from process_data import segregate_by_state
from database import save_to_database

while True:

    print("Fetching ATM data...")

    data = get_atm_data()

    print("Applying business rules...")

    state_tables = segregate_by_state(data)

    print("Saving to database...")

    save_to_database(state_tables)

    print("Pipeline complete. Waiting 1 hour...")

    time.sleep(3600)
