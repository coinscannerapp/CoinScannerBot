from lib import getDataModule as getData
from lib import utilModule as util 
from lib import constants
from lib import helperModule as helper
# external
from binance.client import Client
import json

# key = constants.KEY
# secret = constants.SECRET
# symbol = constants.SYMBOL
# start = constants.START
# end = constants.END

KLINE_INTERVAL = Client.KLINE_INTERVAL_1HOUR
client = Client(constants.KEY, constants.SECRET) # create the Binance client, no need for api key to just read data

def main():
    klines = getData.get_historical_klines(client, constants.SYMBOL, KLINE_INTERVAL, constants.START, constants.END)
    klinelist = helper.populateKlineList(klines)
    # listOfMoves = populatePriceMoveList(klinelist)
    # for move in listOfMoves:
    #     if move.percentDiff() < -10:
    #         print(f'{move.startTime()} has {move.percentDiff()}% drop in {move.durationHours()} hours')
    #     elif move.percentDiff() > 10:
    #         print(f'{move.startTime()} has {move.percentDiff()}% raise in {move.durationHours()} hours')
    
    print(f'LENGTH OF LIST {len(klinelist)}')
    # listOfBases = createBases(klinelist)
    # print(f'LENGTH OF BASES LIST {len(listOfBases)}')
    # for base in listOfBases:
    #     print(f'BASE: {base.startTime()}')
    # util.writeList2File(klinelist, KLINE_INTERVAL)
    powerMoves = helper.filterPowerMoves(helper.populatePriceMoveList(klinelist))
    print(f'LENGTH OF LIST {len(powerMoves)}')

main()
