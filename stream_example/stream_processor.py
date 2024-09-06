import copy
import random
import threading
import time
from stream_example.stream_prices import StreamBase
from queue import Queue

class PriceProcessor(StreamBase):
    def __init__(self, shared_prices, price_lock: threading.Lock, price_events, logname, pair,work_queue:Queue):
        super().__init__(shared_prices, price_lock, price_events, logname)
        self.pair = pair
        self.work_queue=work_queue
    def process_price(self):
        price= None

        try:
            self.price_lock.acquire()
            price=copy.deepcopy(self.shared_prices[self.pair])
        except Exception as error:
            self.log_message(f"CRASH: {error}")
        finally :
            self.price_lock.release()
        if price is None:
            self.log_message(f"No_price",error=True)

        else:#TODO: The processing of live price comes here
            self.log_message(f"Found Price {price}")
            time.sleep(random.randint(2,5))
            self.log_message(f"Done Processing {price}")
            if random.randint(0,5) ==3:
                self.log_message(f"Adding Work: {price}")
                self.work_queue.put(price)

    def run(self):
        while True:
            self.price_events[self.pair].wait()

            self.process_price() # TODO: add logic for what price events u need
            self.price_events[self.pair].clear()
