from lib.entities import KlineData
from lib.entities import PriceMove  
from lib import constants  

def populateKlineList(klines):
        klinelist = []
        for kline in klines:
            klineObj = KlineData.KlineData(
                symbol = constants.SYMBOL,
                OpenTime= kline[0],
                OpenPrice = kline[1],
                HighPrice = kline[2],
                LowPrice = kline[3],
                ClosePrice = kline[4],
                Volume = kline[5],
                CloseTime = kline[6],
                QuoteAssetVol = kline[7],
                NumberOfTrades = kline[8],
            )
            klinelist.append(klineObj)
        return klinelist

def populatePriceMoveList(klinelist):
    listOfMoves = list()
    priceMove = PriceMove.PriceMove()
    for k in klinelist:
        if not priceMove.addKline(k): #if addKline returns false its time to start a new PriceMove
            listOfMoves.append(priceMove)
            priceMove = PriceMove.PriceMove()
            priceMove.addKline(k)
    return listOfMoves

def filterPowerMoves(listOfMoves):
    powerMoves = list()
    for m in listOfMoves:
        if m.isPowerMove():
            print('POWER MOOOOOOOVE')
            powerMoves.append(m)
    return powerMoves
