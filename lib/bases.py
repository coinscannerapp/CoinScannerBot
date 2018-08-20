from lib.entities import KlineData
from lib.entities import PriceMove

def createBases(klinelist):
    listOfBases = list()
    priceMove = PriceMove.PriceMove()
    lastPowerMove = None
    for k in klinelist:
        if not priceMove.addKline(k): #if addKline returns false its time to start a new PriceMove
            if priceMove.isPowerMove():
                print('POWERMOVE')
                if lastPowerMove != None:
                    print('NOT None')
                    base = priceMove.createBase(lastPowerMove)
                    if(base != None):
                        listOfBases.append(base)
                lastPowerMove = priceMove
                priceMove = PriceMove.PriceMove()
                priceMove.addKline(k)
    return listOfBases