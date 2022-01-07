import matplotlib.pyplot as plt
import pandas as pd

def variants_map (core_df,var):
    import pandas as pd
    core_df = pd.DataFrame(core_df, columns = ['date', 'country','variant', 'year', 'longitude', 'latitude','continentExp'])
    core_df = core_df.drop(['year','continentExp','country','date'],axis=1)
    #core_df['date'] = core_df['date'].apply(lambda x: list(x.values())[0][0:10])
    core_df['latitude'] = core_df['latitude'].apply(lambda x: list(x.values())[0]).astype(float)
    core_df['longitude'] = core_df['longitude'].apply(lambda x: list(x.values())[0]).astype(float)
    core_df['variant'] = core_df['variant'].astype(str)
    #core_df['date'] = pd.to_datetime(core_df['date'])
    filter_fecha_final = core_df['variant'] == var
    core_df = core_df[filter_fecha_final]
    core_df = core_df.drop(['variant'],axis=1)
    core_df = core_df.reset_index(drop=True)
    return core_df

def country_location_coord (core_df):
    core_df = pd.DataFrame(core_df, columns = ['latitude', 'longitude'])
    core_df['latitude'] = core_df['latitude'].apply(lambda x: list(x.values())[0]).astype(float)
    core_df['longitude'] = core_df['longitude'].apply(lambda x: list(x.values())[0]).astype(float)
    core_df = core_df.drop_duplicates()
    core_df = core_df.reset_index(drop=True)
    return core_df

def variant_db_TR (core_df):
    import pandas as pd
    core_df = pd.DataFrame(core_df, columns = ['date', 'country','variant', 'year', 'latitude','longitude','continentExp'])
    core_df['date'] = core_df['date'].apply(lambda x: list(x.values())[0][0:10])
    core_df['latitude'] = core_df['latitude'].apply(lambda x: list(x.values())[0]).astype(float)
    core_df['longitude'] = core_df['longitude'].apply(lambda x: list(x.values())[0]).astype(float)
    core_df['year'] = core_df['year'].astype(int)
    core_df['variant'] = core_df['variant'].astype(str)
    core_df['continentExp'] = core_df['continentExp'].astype(str)
    core_df['date'] = pd.to_datetime(core_df['date'])
    return core_df

def country_one_var_df_map (core_df,var):
    columnas = ['country','population',var]
    core_df = pd.DataFrame(core_df, columns = columnas)
    core_df['country'] = core_df['country'].astype(str)

    if var in ['totalDeaths','totalConfirmed','totalTest']:
        core_df[var] = core_df[var].astype(int)
        core_df = core_df.drop(['population'], axis=1)
        core_df = core_df.drop_duplicates(subset='country', keep='last')
        core_df = core_df.reset_index(drop=True)

    if var in ['confirmedDay','deathsDay','icuPatients','hospPatients','newVaccinations']:
        core_df[var] = core_df[var].astype(int)
        core_df[var] = core_df[var] / core_df['population']
        core_df[var] = core_df[var] * 100_000
        core_df = core_df.drop(['population'], axis=1)
        core_df = core_df.groupby(['country']).sum().reset_index()

    if var in ['positiveRate','testsPerCase','vaccinatedPerHundred','fullyVaccinatedPerHundred']:
        core_df[var] = core_df[var].apply(lambda x: list(x.values())[0]).astype(float)
        core_df = core_df.drop(['population'], axis=1)
        core_df = core_df.groupby(['country']).mean().reset_index()
    
    filter_zero = core_df[var] > 0
    core_df = core_df[filter_zero]
    core_df = core_df.sort_values(var)
    return core_df

def top_10_map (core_df):
    core_df = core_df.set_index('country')
    return core_df.tail(10)