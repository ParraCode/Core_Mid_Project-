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

def alldb (core_df):
    core_df = pd.DataFrame(core_df, columns = ['date', 'continent','country', 'totalConfirmed', 'confirmedDay',
    'deathsDay','icuPatients', 'hospPatients','positiveRate','newVaccinations','vaccinatedPerHundred','fullyVaccinatedPerHundred'])
    core_df = core_df.drop(['continent','country'],   axis=1)
    core_df['date'] = core_df['date'].apply(lambda x: list(x.values())[0][0:10])
    core_df['positiveRate'] = core_df['positiveRate'].apply(lambda x: list(x.values())[0])
    core_df['vaccinatedPerHundred'] = core_df['vaccinatedPerHundred'].apply(lambda x: list(x.values())[0])
    core_df['fullyVaccinatedPerHundred'] = core_df['fullyVaccinatedPerHundred'].apply(lambda x: list(x.values())[0])
    core_df['date'] = pd.to_datetime(core_df['date'])
    core_df['totalConfirmed'] = core_df['totalConfirmed'].astype(int)
    core_df['confirmedDay'] = core_df['confirmedDay'].astype(int)
    core_df['deathsDay'] = core_df['deathsDay'].astype(int)
    core_df['icuPatients'] = core_df['icuPatients'].astype(int)
    core_df['hospPatients'] = core_df['hospPatients'].astype(int)
    core_df['positiveRate'] = core_df['positiveRate'].astype(float)
    core_df['newVaccinations'] = core_df['newVaccinations'].astype(int)
    core_df['vaccinatedPerHundred'] = core_df['vaccinatedPerHundred'].astype(float)
    core_df['fullyVaccinatedPerHundred'] = core_df['fullyVaccinatedPerHundred'].astype(float)
    return core_df

    