

import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('expand_frame_repr', False)
from api.oanda import OandaApi
from models.trade_settings import TradeSettings
import constants.defs as defs
from technicals.indicators import BollingerBands
from models.trade_decision import TradeDecision

ADDROWS=20


def apply_SL(row,trade_settings:TradeSettings):
    if row.SIGNAL==defs.BUY:
        return row.mid_c - (row.GAIN / trade_settings.riskreward)
    elif row.SIGNAL==defs.SELL:
        return row.mid_c + (row.GAIN / trade_settings.riskreward)
    return 0.0


def apply_TP(row):
    if row.SIGNAL==defs.BUY:
        return row.mid_c + row.GAIN
    elif row.SIGNAL == defs.SELL:
        return row.mid_c - row.GAIN
    return 0.0


def apply_signal(row,trade_settings:TradeSettings): #TODO Change for different strategies

    # if row.DELTA >= 0 and row.DELTA_PREV < 0:
    #     return defs.BUY
    # elif row.DELTA < 0 and row.DELTA_PREV >= 0:
    #     return defs.SELL
    # else:
    #     return defs.NONE


    #BOLLINGER BANDS##
    if row.SPREAD <= trade_settings.maxspread and row.GAIN >= trade_settings.mingain:
        if row.mid_c > row.BB_UP and row.mid_o < row.BB_UP:
            return defs.SELL
        elif row.mid_c < row.BB_LW and row.mid_o > row.BB_LW:
            return defs.BUY
    return defs.NONE
123


def process_candles(df:pd.DataFrame,pair,trade_settings:TradeSettings,log_message):
    df.reset_index(drop=True,inplace=True)
    df["PAIR"]=pair
    df['SPREAD']=df.ask_c - df.bid_c
    df = BollingerBands(df, trade_settings.n_ma, trade_settings.n_std)  # TODO Change for different strategies
    df["GAIN"] = abs(df.mid_c - df.BB_MA)
    df['SIGNAL'] = df.apply(apply_signal, axis=1, trade_settings=trade_settings)
    df["TP"] = df.apply(apply_TP, axis=1)  # TODO Change for different strategies
    df["SL"] = df.apply(apply_SL, axis=1, trade_settings=trade_settings)  # TODO Change for different strategies
    df["LOSS"] = abs(df.mid_c - df.SL)
    log_cols = ["PAIR", "time", "mid_c", "mid_o", "SPREAD", "LOSS", 'SIGNAL', 'GAIN', "SL", "TP"]
    log_message(f"process_candles:\n {df[log_cols].tail()} ", pair)
    return df[log_cols].iloc[-1]
    # # EMA_CROSSOVER
    # make indicator
    # df.reset_index(drop=True, inplace=True)
    # df["PAIR"] = pair
    # df['SPREAD'] = df.ask_c - df.bid_c
    # df["GAIN"]= 2
    # df["EMA_9"]=df.mid_c.ewm(span=100, min_periods=9).mean()
    # df["EMA_20"] = df.mid_c.ewm(span=100, min_periods=20).mean()
    # df["DELTA"] = df.EMA_9 - df.EMA_20
    # df["DELTA_PREV"] = df.DELTA.shift(1)
    # df['SIGNAL'] = df.apply(apply_signal, axis=1, trade_settings=trade_settings)
    # df["TP"]=df.apply(apply_TP,axis=1)
    # df["SL"] = df.apply(apply_SL, axis=1,trade_settings=trade_settings)
    # df["LOSS"] = abs(df.mid_c - df.SL)
    #
    #
    # log_cols = ["PAIR", "time", "mid_c", "mid_o", "SPREAD", "LOSS", 'SIGNAL', 'GAIN', "SL", "TP"]
    # log_message(f"process_candles:\n {df[log_cols].tail()} ", pair)
    # return df[log_cols].iloc[-1]




def fetch_candles(pair,row_count,candle_time, granularity, api:OandaApi, log_message):
    df=api.get_candles_df(pair,count=row_count,granularity=granularity)
    if df is None or df.shape[0]==0:
        log_message("tech_manager fetch_candles failed to get candles",pair)
        return None

    if df.iloc[-1].time != candle_time:
        log_message(f"tech_manager fetch_candles {df.iloc[-1].time} not correct ", pair)
        return None

    return df




def get_trade_decision(candle_time,pair,granularity,api:OandaApi,trade_settings:TradeSettings,log_message):

    max_rows=trade_settings.n_ma + ADDROWS
    log_message(f"tech_manager: max_rows: {max_rows} candle_time:{candle_time} granularity:{granularity}",pair)
    df=fetch_candles(pair,max_rows,candle_time,granularity,api,log_message)
    if df is not None:
        last_row = process_candles(df,pair,trade_settings,log_message)
        if last_row.SIGNAL != defs.NONE:
            return TradeDecision(last_row)
    return None