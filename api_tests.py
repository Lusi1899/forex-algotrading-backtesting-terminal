from api.oanda import OandaApi
from models.candle_timing import CandleTiming
from Infrastructure.instrument_collection import instrumentCollection
from bot.trade_risk_calculator import get_trade_units
from constants import defs
def lm(msg, pair):
    # print(msg, pair)
    pass

if __name__ == '__main__':
    api = OandaApi()
    instrumentCollection.LoadInstruments("./data")


    print(get_trade_units(api,"EUR_USD",defs.BUY,0.4,60,lm))
    print(get_trade_units(api, "AUD_CAD", defs.BUY, 0.004, 20, lm))
    print(get_trade_units(api, "USD_CAD", defs.BUY, 0.004, 20, lm))








    # api.place_trade("EUR_USD",100,1)


    #### THIS CODE PART MAKES H1_H4_M5 PKL FILES FOR SELECTED PAIRS #######
    # api = OandaApi()
    # instrumentCollection.LoadInstruments("./data")
    # run_collection(instrumentCollection,api)
    #####       END OF THIS PART      ######
    # run_ema_macd(instrumentCollection)

    # run_ema_macd(instrumentCollection)

    # run_ma_sim()

    # instrumentCollection.CreateFile(api.get_instruments(),"./data")
    # instrumentCollection.LoadInstruments("./data")
    # instrumentCollection.PrintInstruments()

    ##### THIS CODE HERE BELOW IS FOR PLOTING MA'S 10,20,50,100,200 ######

    # pair = "EUR_USD"
    # granularity = "H4"
    # MA_LIST = [10, 20, 50, 100, 200]
    # df = pd.read_pickle(f"./data/{pair}_{granularity}.pkl")
    # df['sTime'] = [dt.datetime.strftime(x, "s%y-%m-%d %H:%M") for x in df.time]
    # df_ma = df[['sTime', 'mid_o', 'mid_h', 'mid_l', 'mid_c']].copy()
    # for ma in MA_LIST:
    #     df_ma[f"MA_{ma}"] = df_ma.mid_c.rolling(window=ma).mean()
    #
    # df_ma = df_ma.dropna()
    # df_ma.reset_index(inplace=True, drop=True)
    # traces = [f"MA_{x}" for x in MA_LIST]
    # df_plot = df_ma.iloc[:500]
    # cp=CandlePlot(df_plot)
    # cp.show_plot(line_traces=traces)

    ####### THE CODE OF MA'S ENDS HERE##########

    # data=api.get_account_summary()
    # print(data)
    # instrumentCollection.LoadInstruments("./data")
    # instrumentCollection.PrintInstruments()


