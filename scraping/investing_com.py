from bs4 import BeautifulSoup
import pandas as pd
import requests
import datetime as dt
import time
import cloudscraper
pd.set_option("display.max_columns", None)
from constants import defs

data_keys = [
    'pair_name',
    'ti_buy',
    'ti_sell',
    'ma_buy',
    'ma_sell',
    'S1',
    'S2',
    'S3',
    'pivot',
    'R1',
    'R2',
    'R3',
    'percent_bullish',
    'percent_bearish'
]

df = pd.DataFrame(columns=data_keys)
data = []


def investing_com_summary(tf):
    # data = [investing_com_fetch(12, 3600)]
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0"}
    resp = requests.get("https://investing.com/technical/technical-summary")
    soup = BeautifulSoup(resp.content, "html.parser")
    rows = soup.select("technical_summary_container")
    table = soup.find('table', class_='technicalSummaryTbl')
    data = []

    # Variables to hold temporary data for each currency pair
    currency_pair = ''
    value = ''

    # Iterate through the rows of the table body
    for row in table.tbody.find_all('tr'):
        row_type = row.get('data-row-type')

        if row_type == 'movingAverages':
            # Extract currency pair name and value
            currency_pair = row.find('a').get_text().replace('/', '_')
            value = row.find('p').get_text()
            moving_averages = [cell.get_text(strip=True) for cell in row.find_all('td')[2:]]
        elif row_type == 'indicators':
            indicators = [cell.get_text(strip=True) for cell in row.find_all('td')[1:]]
        elif row_type == 'summary':
            summary = [cell.get_text(strip=True) for cell in row.find_all('td')[1:]]

            # Store the extracted data in a dictionary
            if tf == "M5":
                data.append({
                    'Currency_Pair': currency_pair,
                    'Value': value,
                    'Moving Average': moving_averages[0],
                    'Indicator': indicators[0],
                    'Summary': summary[0],
                })
            if tf == "M15":
                data.append({
                    'Currency_Pair': currency_pair,
                    'Value': value,
                    'Moving Average': moving_averages[1],
                    'Indicator': indicators[1],
                    'Summary': summary[1],
                })
            if tf == "H1":
                data.append({
                    'Currency_Pair': currency_pair,
                    'Value': value,
                    'Moving Average': moving_averages[2],
                    'Indicator': indicators[2],
                    'Summary': summary[2],
                })
            if tf == "D":
                data.append({
                    'Currency_Pair': currency_pair,
                    'Value': value,
                    'Moving Average': moving_averages[3],
                    'Indicator': indicators[3],
                    'Summary': summary[3],
                })

    return pd.DataFrame.from_dict(data)
    # for row in table.tbody.find_all('tr'):
    #     if row.get('data-row-type') == 'movingAverages':
    #         # Extract currency pair name and value
    #         currency_pair = row.find('a').get_text()
    #         value = row.find('p').get_text()
    #     analysis_type = row.find('td', class_='type').get_text(strip=True)
    #     time_frames = [cell.get_text(strip=True) for cell in row.find_all('td')[2:]]
    #
    #     # Store the extracted data in a dictionary
    #     if tf == "M5":
    #         data.append({
    #             'Currency Pair': currency_pair.replace('/', '_'),
    #             'Value': value,
    #             'Analysis Type': analysis_type,
    #             'M5': time_frames[0] if len(time_frames) > 0 else '',
    #
    #         })
    #     if tf == "M15":
    #         data.append({
    #             'Currency Pair': currency_pair.replace('/', '_'),
    #             'Value': value,
    #             'Analysis Type': analysis_type,
    #
    #             'M15': time_frames[1] if len(time_frames) > 1 else '',
    #
    #         })
    #
    #     if tf == "H1":
    #         data.append({
    #             'Currency Pair': currency_pair.replace('/', '_'),
    #             'Value': value,
    #             'Analysis Type': analysis_type,
    #
    #             'H1': time_frames[2] if len(time_frames) > 2 else '',
    #
    #         })
    #     if tf == "D":
    #         data.append({
    #             'Currency Pair': currency_pair.replace('/', '_'),
    #             'Value': value,
    #             'Analysis Type': analysis_type,
    #             'D': time_frames[3] if len(time_frames) > 3 else '',
    #         })
    #
    #
    #
    # return pd.DataFrame.from_dict(data)


def get_key(val):
    for key, value in defs.TFS.items():
        if val == value:
            return key


def pivot_points(tf):
    tfs = 300
    if tf == "M5":
        tfs = 300
    elif tf == "M15":
        tfs = 900
    elif tf == "H1":
        tfs = 3600
    elif tf == "D":
        tfs = 86400
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0"}
    resp = requests.post("https://www.investing.com/technical/pivot-points", data={"period": tfs})
    soup = BeautifulSoup(resp.content, "html.parser")
    table = soup.find('table', id='curr_table')

    # Extract headers
    headers = [th.get_text(strip=True) for th in table.thead.find_all('th')]

    # Extract data rows
    data_rows = []
    for tr in table.tbody.find_all('tr'):
        cells = tr.find_all('td')
        data_row = [cell.get_text(strip=True) for cell in cells]
        data_rows.append(data_row)

    # Print the extracted data
    data_new = pd.DataFrame.from_dict(data_rows)
    data_new.columns = ["Currency_Pair", 'S3', 'S2', 'S1', 'Pivot Point', "R1", "R2", "R3"]
    data_new["Currency_Pair"]=data_new["Currency_Pair"].str.replace("/","_")
    return data_new

def investing_com(tf):
    df_s = investing_com_summary(tf)
    df_t = pivot_points(tf)
    df_merged = df_s.merge(df_t[['Currency_Pair', 'S3', 'S2', 'S1', 'Pivot Point', "R1", "R2", "R3"]])
    df_merged.reset_index(drop=True, inplace=True)
    return df_merged

def get_pair(pair_name,tf):

    df = investing_com(tf)


    if pair_name in defs.INVESTING_COM_PAIRS:
        df_n = df.where(df["Currency_Pair"] == pair_name)
        df_n = df_n.dropna()

    else:
        print("No pair exists")
    # for i, r in df_n.iterrows():
    #     my_list=[r]
    new_df = df_n.iloc[0].to_dict()

    return new_df

