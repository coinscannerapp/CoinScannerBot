import binanceApp
from lib.entities.kline_data import *
from lib.entities.price_move import *
from datetime import datetime

kline1 = KlineData(
    symbol = 'BTCUSDT',
    open_time= 1527480000000,
    open_price = '7000.00000000',
    high_price = '7400.00000000',
    low_price = '7000.00000000',
    close_price = '7400.00000000',
    volume = '1763.2933430',
    close_time = 1527483599999,
    quote_asset_vol = '12944855.34880205',
    number_of_trades = 15272,
)
kline2 = KlineData(
    symbol = 'BTCUSDT',
    open_time= 1527483600000,
    open_price = '7400.00000000',
    high_price = '7800.00000000',
    low_price = '7300.00000000',
    close_price = '7800.00000000',
    volume = '1763.2933430',
    close_time = 1527487199999,
    quote_asset_vol = '12944855.34880205',
    number_of_trades = 15272,
)
kline3 = KlineData(
    symbol = 'BTCUSDT',
    open_time= 1527487200000,
    open_price = '7800.00000000', 
    high_price = '7500.00000000',
    low_price = '7300.00000000',
    close_price = '7500.00000000', #low 7500 fall -300
    volume = '1763.2933430',
    close_time = 1527490799999,
    quote_asset_vol = '12944855.34880205',
    number_of_trades = 15272,
)
kline4 = KlineData(
    symbol = 'BTCUSDT',
    open_time= 1527490800000,
    open_price = '7500.00000000', 
    high_price = '7500.00000000',
    low_price = '6700.00000000',
    close_price = '6800.00000000', #low -1000, fall -700
    volume = '1763.2933430',
    close_time = 1527494399999,
    quote_asset_vol = '12944855.34880205',
    number_of_trades = 15272,
)
kline5 = KlineData(
    symbol = 'BTCUSDT',
    open_time= 1527494400000,
    open_price = '6800.00000000', 
    high_price = '7100.00000000',
    low_price = '6800.00000000',
    close_price = '7100.00000000', 
    volume = '1763.2933430',
    close_time = 1527497999999,
    quote_asset_vol = '12944855.34880205',
    number_of_trades = 15272,
)
kline6 = KlineData(
    symbol = 'BTCUSDT',
    open_time= 1527498000000,
    open_price = '7100.00000000', 
    high_price = '7100.00000000',
    low_price = '7100.00000000',
    close_price = '7100.00000000', 
    volume = '1763.2933430',
    close_time = 15275015999999,
    quote_asset_vol = '12944855.34880205',
    number_of_trades = 15272,
)
kline7= KlineData(
    symbol = 'BTCUSDT',
    open_time= 1527501600000,
    open_price = '7100.00000000', 
    high_price = '8100.00000000',
    low_price = '7100.00000000',
    close_price = '8000.00000000', 
    volume = '1763.2933430',
    close_time = 1527501959999,
    quote_asset_vol = '12944855.34880205',
    number_of_trades = 15272,
)


def test_is_first_kline():
    price_move_obj = PriceMove()
    result = price_move_obj.is_first_kline()
    expected = True
    assert expected == result 

def test_not_first_kline():
    price_move_obj = PriceMove()
    price_move_obj.add_kline(kline1)
    result = price_move_obj.is_first_kline()
    result = price_move_obj.is_first_kline()
    expected = False
    assert expected == result

def test_price_diff():
    price_move_obj = PriceMove()
    price_move_obj.add_kline(kline1)
    price_move_obj.add_kline(kline2)
    result = price_move_obj.price_diff()
    expected = 800
    assert expected == result

def test_price_diff_negative():
    price_move_obj = PriceMove()
    price_move_obj.add_kline(kline3)
    price_move_obj.add_kline(kline4)
    result = price_move_obj.price_diff()
    expected = -1000
    assert expected == result

def test_percent_diff():
    price_move_obj = PriceMove()
    price_move_obj.add_kline(kline1)
    price_move_obj.add_kline(kline2)
    result = price_move_obj.percent_diff()
    expected = 11.43
    assert expected == float(result)

def test_percent_diff_negative():
    price_move_obj = PriceMove()
    price_move_obj.add_kline(kline3)
    price_move_obj.add_kline(kline4)
    result = price_move_obj.percent_diff()
    expected = -12.82
    assert expected == float(result)

def test_price_diff_several():
    price_move_obj = PriceMove()
    price_move_obj.add_kline(kline1)
    price_move_obj.add_kline(kline2)
    price_move_obj.add_kline(kline3)
    # priceMove.addKline(kline4)
    result = price_move_obj.price_diff()
    expected = 800 # third kline is not added since its going in opposite direction
    assert expected == result

def test_same_direction():
    price_move_obj = PriceMove()
    price_move_obj.add_kline(kline1)
    result = price_move_obj.kline_is_same_direction(kline2)
    expected = True
    assert expected == result

def test_not_same_direction():
    price_move_obj = PriceMove()
    price_move_obj.add_kline(kline1)
    price_move_obj.add_kline(kline2)
    result = price_move_obj.kline_is_same_direction(kline3)
    expected = False
    assert expected == result

# def test_NotSameDirTwice():
#     priceMove = price_move.PriceMove()
#     priceMove.addKline(kline1)
#     priceMove.addKline(kline2)
#     priceMove.addKline(kline3)
#     result = priceMove.klineIsSameDirection(kline4) #Should be false since changes from positive
#     expected = False
#     assert expected == result
#     priceMove.addKline(kline4)
#     result = priceMove.klineIsSameDirection(kline5) #After kline4 the priceMove is overall negative
#     assert expected == result

def test_impact():
    price_move_obj = PriceMove()
    price_move_obj.add_kline(kline1)
    result = price_move_obj.kline_impact(kline2)
    expected = 100
    assert expected == result

def test_negative_impact():
    price_move_obj = PriceMove()
    price_move_obj.add_kline(kline1)
    price_move_obj.add_kline(kline2)
    result = price_move_obj.kline_impact(kline3)
    expected = -37.5
    assert expected == float(result)

def test_duration_secs():
    price_move_obj = PriceMove()
    price_move_obj.add_kline(kline1)
    price_move_obj.add_kline(kline2)
    result = price_move_obj.duration_secs()
    # expected = datetime.timedelta(hours=1, minutes=59, seconds=59, milliseconds=999) #when returning datetime.timedelta
    expected = 60*60*2 # 2 hours
    assert expected == result

def test_duration_hours():
    price_move_obj = PriceMove()
    price_move_obj.add_kline(kline1)
    price_move_obj.add_kline(kline2)
    result = price_move_obj.duration_hours()
    expected = 2
    assert expected == result

def test_overloaded_plus_operator():
    price_move1 = PriceMove()
    price_move1.add_kline(kline1)
    price_move1.add_kline(kline2)
    price_move2 = PriceMove()
    price_move2.add_kline(kline3)
    price_move2.add_kline(kline4)
    combined = price_move1 + price_move2
    result = combined.duration_hours()
    expected = 4
    # assert expected == result
    assert combined.start_price() == 7000
    assert combined.end_price() == 6800
    assert datetime.fromtimestamp(1527480000000/1000) == combined.start_time()
    assert datetime.fromtimestamp(1527494399999/1000) == combined.end_time()
    assert combined.low_price() == 6700
    assert combined.high_price() == 7800

def test_is_power_move():
    price_move_obj = PriceMove()
    price_move_obj.add_kline(kline1)
    price_move_obj.add_kline(kline2)
    result = price_move_obj.is_power_move()
    expected = True
    assert expected == result

def test_not_power_move():
    price_move_obj = PriceMove()
    price_move_obj.add_kline(kline5)
    price_move_obj.add_kline(kline6)
    result = price_move_obj.is_power_move()
    expected = False
    assert expected == result

def test_hours_appart():
    price_move1 = PriceMove()
    price_move2 = PriceMove()
    price_move1.add_kline(kline1)
    price_move2.add_kline(kline3)
    result = price_move2.hours_appart(price_move1)
    expected = 1
    assert expected == result

def test_is_power_raise():
    price_move1 = PriceMove()
    price_move1.add_kline(kline5)
    price_move1.add_kline(kline6) 
    price_move1.add_kline(kline7) #Now its a powerraise
    assert price_move1.start_price() == 6800.0
    assert price_move1.end_price() == 8000.0
    assert price_move1.percent_diff() > 10
    assert price_move1.duration_hours() < 5
    assert price_move1.is_power_raise() == True

def test_create_base():
    price_move1 = PriceMove()
    price_move2 = PriceMove()
    price_move1.add_kline(kline3)
    price_move1.add_kline(kline4) #Now its a powerdrop
    price_move2.add_kline(kline5)
    price_move2.add_kline(kline6) 
    price_move2.add_kline(kline7) #Now its a powerraise
    base = price_move2.create_base(price_move1)
    assert price_move2.is_power_raise() == True
    assert price_move1.is_power_drop() == True
    assert base != None