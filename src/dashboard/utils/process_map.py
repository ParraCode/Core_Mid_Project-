import pandas as pd

# dashboard Covid
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

