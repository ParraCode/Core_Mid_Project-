import matplotlib.pyplot as plt
import pandas as pd

def fechaDay_int_transf (core_df):
    core_df = pd.DataFrame(core_df, columns = ['_id','date','totalConfirmed', 'totalDeaths'])
    core_df = core_df.drop(['_id'], axis=1)
    core_df['date'] = core_df['date'].apply(lambda x: list(x.values())[0][0:10])
    core_df['date'] = pd.to_datetime(core_df['date'])
    core_df = core_df.set_index(['date'])
    return core_df

def fechaYW_int_transf (core_df):
    core_df = pd.DataFrame(core_df, columns = ['_id', 'Year-Week','date','confirmedDay', 'deathsDay'])
    core_df = core_df.drop(['_id'], axis=1)
    core_df = core_df.groupby('Year-Week').sum()
    return core_df


def country_location_coord (core_df):
    core_df = pd.DataFrame(core_df, columns = ['latitude', 'longitude'])
    core_df['latitude'] = core_df['latitude'].apply(lambda x: list(x.values())[0]).astype(float)
    core_df['longitude'] = core_df['longitude'].apply(lambda x: list(x.values())[0]).astype(float)
    core_df = core_df.drop_duplicates()
    core_df = core_df.reset_index(drop=True)
    return core_df

    