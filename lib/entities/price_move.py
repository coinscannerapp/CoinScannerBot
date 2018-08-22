from lib import constants
import datetime

class PriceMove(object): # This should probably be a super type of the Kline class so that the plus operator could be overloaded to add pricemoves to each other. 
    def __init__(self, low_price = 0, high_price = 0, start_price = 0, end_price = 0, start_time = 0, end_time = 0):
        self._start_price = start_price
        self._end_price = end_price
        self._low_price = low_price
        self._high_price = high_price
        self._start_time = start_time
        self._end_time = end_time
    def start_time(self):
        return self._start_time
    def start_price(self):
        return self._start_price
    def end_time(self):
        return self._end_time
    def end_price(self):
        return self._end_price
    def high_price(self):
        return self._high_price
    def low_price(self):
        return self._low_price
    def price_diff(self):
        self._price_diff = self._end_price - self._start_price 
        return self._price_diff

    def percent_diff(self):
        if(self.start_price()!=0):
            self._percent_diff = self.price_diff()/self.start_price()*100
            # print(f'percentDiff: priceDiff={self._priceDiff} and startPrice = {self._startPrice}')
        else:
            self._percent_diff = 0
        return round(self._percent_diff, 2)

    def duration_secs(self):
        self._time_diff = self._end_time - self._start_time
        seconds = round(self._time_diff.total_seconds(),0)
        return seconds
    
    def duration_hours(self):
        return self.duration_secs()/(60*60)

    def is_green(self):
        self._is_green = True if self.price_diff() > 0 else False
        return self._is_green
    
    def is_power_move(self):
        return self.is_power_drop() or self.is_power_raise()

    def is_power_drop(self):
        return self.duration_hours() < constants.MAX_DURATION and self.percent_diff() < constants.MIN_PRICE_DIFF*-1

    def is_power_raise(self):
        return (self.duration_hours() < constants.MAX_DURATION and self.percent_diff() > constants.MIN_PRICE_DIFF)
        # return self.durationHours() < constants.MAX_DURATION
        # return self.percentDiff() > constants.MIN_PRICE_DIFF
    
    def create_base(self, other):
        if self.is_power_raise() and other.is_power_drop():
            if self.hours_appart(other) <= constants.MAX_HOURS_APPART:
                return PriceMove(
                    low_price=other.low_price(), 
                    high_price=self.high_price(), 
                    start_price=other.start_price(), 
                    end_price=self.end_price(), 
                    start_time=other.start_time(), 
                    end_time=self.end_time())
                

    def hours_appart(self, other):
        return round(datetime.timedelta.total_seconds(self.start_time() - other.end_time())/(60*60), 0)

    def add_kline(self, k): # returns bool to tell if adding the kline strengthend the priceMove or reverse
        # print(f'Just into Add Kline: priceDiff={self.priceDiff()} and startPrice = {self._startPrice}')
        if self.is_first_kline():
            self._start_time = k.open_time()
            self._start_price = k.open_price()
            self._end_time = k.close_time()
            self._end_price = k.close_price()
            self._low_price = k.low_price() 
            self._high_price = k.high_price()
        # Is the kline good to incorporate?
        if self.kline_is_same_direction(k) and self.kline_impact(k) > constants.MAX_ALLOWED_NEG_IMPACT : # negative impact comes as a negative number
            self._end_time = k.close_time()
            self._end_price = k.close_price()
            self._end_time = k.close_time()
            self._end_price = k.close_price()
            self._low_price = k.low_price() if k.low_price() < self.low_price() else self.low_price()
            self._high_price = k.high_price() if k.high_price() > self.high_price() else self.high_price()
            return True
        else:
            return False
        
    def kline_is_same_direction(self, k):
        if self.price_diff() == 0.0:
            return True
        if (k.is_green() and self.is_green()):
            return True
        if not k.is_green():
            if not self.is_green():
                return True
        return False

    def is_first_kline(self):
        if self._start_price == 0: 
            return True
        return False

    def kline_impact(self, kline):
        kline_diff = kline.price_diff()
        this_diff = self.price_diff()
        percentage_impact = 0 if this_diff == 0 else round(kline_diff/this_diff*100, 2)
        return percentage_impact
    def __add__(self, other): # overloading the + operator (to be able to add klines value differences to each other)
        start_time = self.start_time() if self.start_time() < other.start_time() else other.start_time()
        end_time = self.end_time() if self.end_time() > other.end_time() else other.end_time()
        start_price = self.start_price() if self.start_time() < other.start_time() else other.start_price()
        end_price = other.end_price() if self.start_time() < other.start_time() else other.end_price()
        low_price = self.low_price() if self.low_price() < other.low_price() else other.low_price()
        high_price = self.high_price() if self.high_price() > other.high_price() else other.high_price()

        return PriceMove(low_price=low_price, high_price=high_price, 
                        start_price=start_price, end_price=end_price,
                        start_time=start_time, end_time=end_time
                        )

# end of module: entitiesModule.py
