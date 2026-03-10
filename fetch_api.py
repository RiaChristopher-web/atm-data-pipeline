import pandas as pd

def get_atm_data():

    # Read ATM dataset
    df = pd.read_excel("BOB_Source.xlsx")

    return df
