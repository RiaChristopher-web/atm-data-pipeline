import sqlite3

def save_to_database(state_tables):

    conn = sqlite3.connect("atm_database.db")

    for table_name, data in state_tables.items():

        data.to_sql(table_name, conn, if_exists="replace", index=False)

    conn.close()
