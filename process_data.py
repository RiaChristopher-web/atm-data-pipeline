def segregate_by_state(df):

    state_tables = {}

    # find all unique states
    states = df["STATE"].unique()

    for state in states:

        state_data = df[df["STATE"] == state]

        # create table name
        table_name = state.lower().replace(" ", "_")

        state_tables[table_name] = state_data

    return state_tables
