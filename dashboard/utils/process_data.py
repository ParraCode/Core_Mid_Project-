import matplotlib.pyplot as plt
import pandas as pd

def covid_cases_graph(data):
    covid_cases_date = pd.DataFrame(data)
    plt.figure(figsize=[20,10])
    columns = [column for column in covid_cases_date.columns[1:]]
    for country in covid_cases_date.values:
        plt.ylabel('Cases')
        plt.xlabel('Date')
        plt.xticks(rotation=75)
        plt.plot(columns, country[1:], label=country[0])
        plt.legend()
    return plt

def fecha_int_transf (core_df):
    core_df = pd.DataFrame(core_df, columns = ['_id','date','confirmedDay'])
    core_df = core_df.drop(['_id'], axis=1)
    core_df['date'] = core_df['date'].apply(lambda x: list(x.values())[0][0:10])
    core_df['date'] = pd.to_datetime(core_df['date'])
    core_df['_id'] = core_df.index
    return core_df