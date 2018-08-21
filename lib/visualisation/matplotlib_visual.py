import matplotlib.pyplot as plt
from lib import constants


def create_plot(kline_list):

    # Labels
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.title("Market for\n" +constants.SYMBOL)  # Which coin we are trading
    plt.legend()

    # Sort plot data
    y = sort_y(kline_list)
    x = sort_x(kline_list)

    # Plot
    plt.plot(x, y, label="test")
    plt.show()


def sort_y(kline_list):
    """ Sort all close prices for y-axis for the visualisation of graph
    params: 
    array : kline_list
    return : array of y
    """

    y = []
    for kline in kline_list:
        y.append(kline.closePrice())

    return y   


def sort_x(kline_list):
    """ Sort all close times for x-axis for visualisation of graph
    """

    x = []

    for kline in kline_list:
        x.append(kline.closeTime())

    return x
