from lib.data_fetch_modules import get_data_module
from lib.helper_modules import util_module as util
from lib.entities import kline_data
from lib.entities import price_move
from lib import constants
from lib.visualisation import matplotlib_visual
# external
from binance.client import Client
import json

# key = constants.KEY
# secret = constants.SECRET
# symbol = constants.SYMBOL
# start = constants.START
# end = constants.END

KLINE_INTERVAL = Client.KLINE_INTERVAL_1HOUR
# create the Binance client, no need for api key to just read data
client = Client(constants.KEY, constants.SECRET)


def main():
    klines = get_data_module.get_historical_klines(
        client, constants.SYMBOL, KLINE_INTERVAL, constants.START, constants.END)
    kline_list = populate_kline_list(klines)
    # listOfMoves = populatePriceMoveList(klinelist)
    # for move in listOfMoves:
    #     if move.percentDiff() < -10:
    #         print(f'{move.startTime()} has {move.percentDiff()}% drop in {move.durationHours()} hours')
    #     elif move.percentDiff() > 10:
    #         print(f'{move.startTime()} has {move.percentDiff()}% raise in {move.durationHours()} hours')

    print(f'LENGTH OF LIST {len(kline_list)}')
    # listOfBases = createBases(kline_list)
    # print(f'LENGTH OF BASES LIST {len(listOfBases)}')
    # for base in listOfBases:
    #     print(f'BASE: {base.startTime()}')
    # util.writeList2File(kline_list, KLINE_INTERVAL)
    power_moves = filter_power_moves(populate_price_move_list(kline_list))

    if(constants.VISUALIZE):
        matplotlib_visual.create_plot(kline_list)

    print(f'LENGTH OF LIST {len(power_moves)}')


def populate_kline_list(klines):
    kline_list = []
    for kline in klines:
        klineObj = kline_data.KlineData(
            symbol=constants.SYMBOL,
            OpenTime=kline[0],
            OpenPrice=kline[1],
            HighPrice=kline[2],
            LowPrice=kline[3],
            ClosePrice=kline[4],
            Volume=kline[5],
            CloseTime=kline[6],
            QuoteAssetVol=kline[7],
            NumberOfTrades=kline[8],
        )
        kline_list.append(klineObj)
    return kline_list


def populate_price_move_list(kline_list):
    list_of_moves = list()
    price_move_Obj = price_move.PriceMove()
    for k in kline_list:
        # if addKline returns false its time to start a new PriceMove
        if not price_move_Obj.addKline(k):
            list_of_moves.append(price_move_Obj)
            price_move_Obj = price_move.PriceMove()
            price_move_Obj.addKline(k)
    return list_of_moves


def filter_power_moves(list_of_moves):
    power_moves = list()
    for m in list_of_moves:
        if m.isPowerMove():
            print('POWER MOOOOOOOVE')
            power_moves.append(m)
    return power_moves


def create_bases(kline_list):
    list_of_bases = list()
    price_move_Obj = price_move.PriceMove()
    last_power_move = None
    for k in kline_list:
        # if addKline returns false its time to start a new PriceMove
        if not price_move_Obj.addKline(k):
            if price_move_Obj.isPowerMove():
                print('POWERMOVE')
                if last_power_move != None:
                    print('NOT None')
                    base = price_move_Obj.createBase(last_power_move)
                    if(base != None):
                        list_of_bases.append(base)
                last_power_move = price_move_Obj
                price_move_Obj = price_move.PriceMove()
                price_move_Obj.addKline(k)
    return list_of_bases


if __name__ == '__main__':
    main()
