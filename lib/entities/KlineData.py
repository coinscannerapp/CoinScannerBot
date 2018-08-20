from lib import utilModule as util
from lib import constants
from decimal import Decimal

class KlineData(object):
    def __init__(self, symbol, **params):
        self._symbol = symbol
        self._openTime = util.ms2date(params["OpenTime"])
        self._openPrice = Decimal(params["OpenPrice"])
        self._highPrice = Decimal(params["HighPrice"])
        self._lowPrice = Decimal(params["LowPrice"])
        self._closePrice = Decimal(params["ClosePrice"])
        self._volume = params["Volume"]
        self._closeTime = util.ms2date(params["CloseTime"])
        self._quoteAssetVolume = params["QuoteAssetVol"]
        self._numberOfTrades = params["NumberOfTrades"]        

    def openTime(self, t = None): 
        if t: self._openTime = t 
        return self._openTime

    def closeTime(self, t = None): 
        if t: self._closeTime = t 
        return self._closeTime

    def openPrice(self, t = None): 
        if t: self._openPrice = t 
        return self._openPrice

    def closePrice(self):
        return self._closePrice
        
    def highPrice(self, t = None): 
        if t: self._highPrice = t 
        return self._highPrice

    def lowPrice(self, t = None): 
        if t: self._lowPrice = t 
        return self._lowPrice

    def volume(self, t = None): 
        if t: self._volume = t 
        return self._volume

    def priceDiff(self): 
        self._priceDiff = self._closePrice - self._openPrice
        return self._priceDiff

    def isGreen(self):
        self._isGreen = True if self.priceDiff() > 0 else False
        return self._isGreen

    def __str__(self):
        # return f'{symbol} start time: {self._openTime}, close time: {self._closeTime}, highest price: {self._highPrice}, lowest price: {self._lowPrice}'
        return f'{self._symbol} start time: {self._openTime}, close time: {self._closeTime}, price difference: {self.priceDiff()} isGreen: {self.isGreen()}'
