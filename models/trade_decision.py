class TradeDecision:

    def __init__(self,row):
        self.gain=row.GAIN
        self.loss = row.LOSS
        self.signal = row.SIGNAL
        self.sl = row.SL
        self.tp = row.TP
        self.pair = row.PAIR


    def __repr__(self):
        return f"TradeDecision(): {self.pair} dir:{self.signal} gain:{self.gain} sl:{ self.sl} tp:{self.tp }"
