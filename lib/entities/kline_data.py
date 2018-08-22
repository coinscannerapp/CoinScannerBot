import datetime
from decimal import Decimal

from lib.helper_modules import util_module as util


class KlineData(object):
    def __init__(self, symbol, **params):
        self._symbol = symbol
        self._open_time = util.ms2date(params["open_time"])
        self._open_price = Decimal(params["open_price"])
        self._high_price = Decimal(params["high_price"])
        self._low_price = Decimal(params["low_price"])
        self._close_price = Decimal(params["close_price"])
        self._volume = params["volume"]
        self._close_time = util.ms2date(params["close_time"])
        self._quote_asset_volume = params["quote_asset_vol"]
        self._number_of_trades = params["number_of_trades"]
        
        

    def open_time(self, t = None): 
        if t: self._open_time = t 
        return self._open_time
    def close_time(self, t = None): 
        if t: self._close_time = t 
        return self._close_time
    def open_price(self, t = None): 
        if t: self._open_price = t 
        return self._open_price
    def close_price(self):
        return self._close_price
    def high_price(self, t = None): 
        if t: self._high_price = t 
        return self._high_price
    def low_price(self, t = None): 
        if t: self._low_price = t 
        return self._low_price
    def volume(self, t = None): 
        if t: self._volume = t 
        return self._volumen
    def price_diff(self): 
        self._price_diff = self._close_price - self._open_price
        return self._price_diff
    def is_green(self):
        self._is_green = True if self.price_diff() > 0 else False
        return self._is_green
    def __str__(self):
        # return f'{symbol} start time: {self._openTime}, close time: {self._closeTime}, highest price: {self._highPrice}, lowest price: {self._lowPrice}'
        return f'{self._symbol} start time: {self._open_time}, close time: {self._close_time}, price difference: {self.price_diff()} is_green: {self.is_green()}'
