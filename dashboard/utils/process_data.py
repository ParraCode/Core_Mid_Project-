import pandas as pd

# dasboard EDA
def alldb (core_df):
    core_df = pd.DataFrame(core_df, columns = ['date', 'continent','country', 'totalConfirmed', 'confirmedDay',
    'deathsDay','icuPatients', 'hospPatients','positiveRate','newVaccinations','vaccinatedPerHundred','fullyVaccinatedPerHundred'])
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

# dashboard Covid
def lista_variables (var):
    lista = list(var[0].keys())
    lista_delete = ['date','country','continent','latitude','longitude',
                    'Year','Month','Week','Day','Year-Week']
    for x in lista_delete:
        if x in lista:
            lista.remove(x)
    return lista
# dashboard Covid
def limpieza_variables_pais (var):
    lista = list(var[0].keys())
    lista_delete = ['continent','latitude','longitude',
                    'Year','Month','Week','Day','Year-Week']
    for x in lista_delete:
        if x in lista:
            lista.remove(x)
    return lista

# dashboard Covid
def country_one_var_df (core_df,var,fecha_inicial,fecha_final):
    #def country_one_var_df (core_df,var):
    columnas = limpieza_variables_pais(core_df)
    core_df = pd.DataFrame(core_df, columns = columnas)
    core_df = core_df.drop(core_df.columns.difference(['date','country',var]),axis=1)
    core_df['date'] = core_df['date'].apply(lambda x: list(x.values())[0][0:10])
    if var in ['positiveRate','vaccinatedPerHundred','fullyVaccinatedPerHundred']:
        core_df[var] = core_df[var].apply(lambda x: list(x.values())[0]).astype(float)
    core_df['country'] = core_df['country'].astype(str)
    country_name = core_df['country'][0]
    core_df = core_df.rename(columns={var: country_name})
    core_df = core_df.drop(['country'],axis=1)
    core_df['date'] = pd.to_datetime(core_df['date'])
    core_df['fecha_inicial'] = fecha_inicial
    filter_fecha_inicial = core_df['date'] >= core_df['fecha_inicial']
    core_df = core_df[filter_fecha_inicial]
    core_df['fecha_final'] = fecha_final
    filter_fecha_final = core_df['date'] <= core_df['fecha_final']
    core_df = core_df[filter_fecha_final]
    core_df = core_df.drop(['fecha_final','fecha_inicial'],   axis=1)
    return core_df

# dashboard Covid
def merge_country_data(df1,df2):
    df = pd.merge(df1, df2 , how='inner', on='date')
    df = df.set_index('date')
    return df

# dashboard Covid
def top_10_map (core_df):
    core_df = core_df.set_index('country')
    return core_df.tail(10)