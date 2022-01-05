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

def lista_variables (var):
    lista = list(var[0].keys())
    lista_delete = ['date','country','continent','latitude','longitude',
                    'Year','Month','Week','Day','Year-Week']
    for x in lista_delete:
        if x in lista:
            lista.remove(x)
    return lista

def limpieza_variables_pais (var):
    lista = list(var[0].keys())
    lista_delete = ['continent','latitude','longitude',
                    'Year','Month','Week','Day','Year-Week']
    for x in lista_delete:
        if x in lista:
            lista.remove(x)
    return lista


def country_one_var_df (core_df,var):
    columnas = limpieza_variables_pais(core_df)
    core_df = pd.DataFrame(core_df, columns = columnas)
    core_df = core_df.drop(core_df.columns.difference(['date','country',var]),axis=1)
   
    core_df['date'] = core_df['date'].apply(lambda x: list(x.values())[0][0:10])
    core_df[var] = core_df[var].astype(float)
    core_df['country'] = core_df['country'].astype(str)

    country_name = core_df['country'][0]
    core_df = core_df.rename(columns={var: country_name})
    
    core_df = core_df.drop(['country'],axis=1)
    core_df['date'] = pd.to_datetime(core_df['date'])

    #filter_fecha_inicial = core_df['date'] >= fecha_inicial
    #core_df = core_df[filter_fecha_inicial]
    #filter_fecha_final = core_df['date'] <= fecha_final
    #core_df = core_df[filter_fecha_final]
    
    return core_df

def merge_country_data(df1,df2):
    df = pd.merge(df1, df2 , how='inner', on='date')
    df = df.set_index('date')
    return df

# -------------------------------------------------------------------------------------------------------------------------------------------------
# VARIANTS

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

def variant_TR (core_df):
    core_df = pd.DataFrame(core_df, columns = ['date', 'country','variant', 'year', 'latitude','longitude','continentExp'])
    core_df = core_df.drop(['date', 'country', 'year', 'latitude','longitude','continentExp'], axis=1)
    core_df['variant'] = core_df['variant'].astype(str)
    core_df = core_df.drop_duplicates()
    return list(core_df['variant'])
    