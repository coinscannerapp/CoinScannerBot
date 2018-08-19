from lib import constants
import datetime

class PriceMove(object): # This should probably be a super type of the Kline class so that the plus operator could be overloaded to add pricemoves to each other. 
    def __init__(self, lowPrice = 0, highPrice = 0, startPrice = 0, endPrice = 0, startTime = 0, endTime = 0):
        self._startPrice = startPrice
        self._endPrice = endPrice
        self._lowPrice = lowPrice
        self._highPrice = highPrice
        self._startTime = startTime
        self._endTime = endTime
    def startTime(self):
        return self._startTime
    def startPrice(self):
        return self._startPrice
    def endTime(self):
        return self._endTime
    def endPrice(self):
        return self._endPrice
    def highPrice(self):
        return self._highPrice
    def lowPrice(self):
        return self._lowPrice
    def priceDiff(self):
        self._priceDiff = self._endPrice - self._startPrice 
        return self._priceDiff

    def percentDiff(self):
        if(self.startPrice()!=0):
            self._percentDiff = self.priceDiff()/self.startPrice()*100
            # print(f'percentDiff: priceDiff={self._priceDiff} and startPrice = {self._startPrice}')
        else:
            self._percentDiff = 0
        return round(self._percentDiff, 2)

    def durationSecs(self):
        self._timeDiff = self._endTime - self._startTime
        seconds = round(self._timeDiff.total_seconds(),0)
        return seconds
    def durationHours(self):
        return self.durationSecs()/(60*60)

    def isGreen(self):
        self._isGreen = True if self.priceDiff() > 0 else False
        return self._isGreen
    
    def isPowerMove(self):
        return self.isPowerDrop() or self.isPowerRaise()
    def isPowerDrop(self):
        return self.durationHours() < constants.MAX_DURATION and self.percentDiff() < constants.MIN_PRICE_DIFF*-1
    def isPowerRaise(self):
        return (self.durationHours() < constants.MAX_DURATION and self.percentDiff() > constants.MIN_PRICE_DIFF)
        # return self.durationHours() < constants.MAX_DURATION
        # return self.percentDiff() > constants.MIN_PRICE_DIFF
    
    def createBase(self, other):
        if self.isPowerRaise() and other.isPowerDrop():
            if self.hoursAppart(other) <= constants.MAX_HOURS_APPART:
                return PriceMove(
                    lowPrice=other.lowPrice(), 
                    highPrice=self.highPrice(), 
                    startPrice=other.startPrice(), 
                    endPrice=self.endPrice(), 
                    startTime=other.startTime(), 
                    endTime=self.endTime())
                

    def hoursAppart(self, other):
        return round(datetime.timedelta.total_seconds(self.startTime() - other.endTime())/(60*60), 0)

    def addKline(self, k): # returns bool to tell if adding the kline strengthend the priceMove or reverse
        # print(f'Just into Add Kline: priceDiff={self.priceDiff()} and startPrice = {self._startPrice}')
        if self.isFirstKline():
            self._startTime = k.openTime()
            self._startPrice = k.openPrice()
            self._endTime = k.closeTime()
            self._endPrice = k.closePrice()
            self._lowPrice = k.lowPrice() 
            self._highPrice = k.highPrice()
        # Is the kline good to incorporate?
        if self.klineIsSameDirection(k) and self.klineImpact(k) > constants.MAX_ALLOWED_NEG_IMPACT : # negative impact comes as a negative number
            self._endTime = k.closeTime()
            self._endPrice = k.closePrice()
            self._endTime = k.closeTime()
            self._endPrice = k.closePrice()
            self._lowPrice = k.lowPrice() if k.lowPrice() < self.lowPrice() else self.lowPrice()
            self._highPrice = k.highPrice() if k.highPrice() > self.highPrice() else self.highPrice()
            return True
        else:
            return False
        
    def klineIsSameDirection(self, k):
        if self.priceDiff() == 0.0:
            return True
        if (k.isGreen() and self.isGreen()):
            return True
        if not k.isGreen():
            if not self.isGreen():
                return True
        return False

    def isFirstKline(self):
        if self._startPrice == 0: 
            return True
        return False

    def klineImpact(self, kline):
        klineDiff = kline.priceDiff()
        thisDiff = self.priceDiff()
        percentageImpact = 0 if thisDiff == 0 else round(klineDiff/thisDiff*100, 2)
        return percentageImpact
    def __add__(self, other): # overloading the + operator (to be able to add klines value differences to each other)
        startTime = self.startTime() if self.startTime() < other.startTime() else other.startTime()
        endTime = self.endTime() if self.endTime() > other.endTime() else other.endTime()
        startPrice = self.startPrice() if self.startTime() < other.startTime() else other.startPrice()
        endPrice = other.endPrice() if self.startTime() < other.startTime() else other.endPrice()
        lowPrice = self.lowPrice() if self.lowPrice() < other.lowPrice() else other.lowPrice()
        highPrice = self.highPrice() if self.highPrice() > other.highPrice() else other.highPrice()

        return PriceMove(lowPrice=lowPrice, highPrice=highPrice, startPrice=startPrice, endPrice=endPrice, startTime=startTime, endTime=endTime)
# end of module: entitiesModule.py
