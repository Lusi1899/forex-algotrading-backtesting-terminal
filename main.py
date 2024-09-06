
from api.oanda import OandaApi
import pandas as pd
from db.db import DataDB
import datetime as dt
from dateutil import parser
from exploration.ploting import CandlePlot
from Infrastructure.instrument_collection import instrumentCollection
from Infrastructure.collect_data import run_collection
from simulation.ma_cross import run_ma_sim
from simulation.ema_macd_mp import run_ema_macd
from stream_example.streamer import run_streamer
def db_test():
    d=DataDB()  
    # d.add_many(collection=DataDB.SAMPLE_COLL, list_ob=[dict(age=13,name='sam',eyes='yellow'),dict(age=14,name='Gaam',eyes='Pink')])
    print(d.query_distinct(DataDB.SAMPLE_COLL,"age"))
if __name__ == '__main__':
    api = OandaApi()
    # instrumentCollection.LoadInstruments("./data")
    # # stream_prices(["EUR_USD","USD_JPY"])
    # instrumentCollection.LoadInstrumentsDB()
    # print(instrumentCollection.instruments_dict)
    run_ma_sim()
    # run_streamer(zz)
    # instrumentCollection.CreateDB(api.get_instruments())
    # d=DataDB()
    # d.test_connection()
    # db_test()