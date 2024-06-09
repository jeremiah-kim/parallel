import pandas as pd
from fredapi import Fred

# load fred api using personal key
fr = Fred(api_key="450a3a63a4015a44797d1c94fa5efd75")

# load the BLS series ids list
series_ids = pd.read_fwf('data/generations/series_ids.txt', headers=None, Index=0)['series_ids'].to_list()

START_DATE = '1/1/1990'
END_DATE = '1/1/2022'


def fred_request():
    data = {}
    for series_id in series_ids:
        series = fr.get_series(series_id, observation_start=START_DATE, observation_end=END_DATE, frequency="a")
        data[series_id] = series
    df = pd.DataFrame(data)
    return df


df = fred_request()

nces_df = pd.read_csv('data/generations/nces_data.csv', index_col=0)
nces_df.index = df.index

df = pd.merge(df, nces_df, left_index=True, right_index=True)
df.to_csv('data/generations/gen_data.csv')
