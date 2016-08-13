#!/usr/bin/env python
from core.agents.Parameters import Query
from core.agents.web.Yahoo.Controller import Controller
from strategy.basic import basic
import matplotlib.pyplot as plt
import matplotlib.dates as matplotlibdates


def get_data_from_stock(stock_name):
    query = Query()
    query.add(Controller.PARAM_NAME_STOCK_NAME, stock_name)

    controller = Controller()
    controller.init()
    data = controller.run(query)
    return data

def print_graph(stock_name, stock_prices, dates, capital, buys, sells):
    '''Initialize the fig '''
    plt.figure()


    '''Cargamos las etiquetas, tanto del eje X como del Y'''
    plt.xlabel(r"Stock Price", fontsize = 24, color = (1,0,0))
    plt.ylabel(r"Date", fontsize = 24, color = 'blue')

    '''Cargamos dos plots con una division horizontal'''
    plt.subplot(2,1,1)
    dates = matplotlibdates.datestr2num(dates)
    plt.title("Stock:{stock}".format(stock=stock_name))
    plt.plot_date(dates, stock_prices, fmt="", tz=None, xdate=True)
    plt.subplot(2,1,2)
    plt.title("Capital evolution:{stock}".format(stock=stock_name))
    plt.plot_date(dates, capital, fmt="", tz=None, xdate=True)

    '''Ensenamos el plot final'''
    plt.savefig("img/basic/{stock}".format(stock=stock_name))

def InsertToFile(message):
    with open("result.csv", "a") as myfile:
        myfile.write(message)

def calculate(stock_name):
    data = get_data_from_stock(stock_name)
    capital_inicial = 10000
    capital = 0
    stocks = 0
    stock_prices = []
    dates = []
    profits = []
    b = basic(capital_inicial)
    for d in data:
        stocks, capital = b.run(stocks, d, data)
        stock_prices.append(d.close)
        profits.append(capital)
        dates.append(d.date)

    rdto = (capital / capital_inicial) - 1;
    print_graph(stock_name,stock_prices, dates, profits, None, None)
   
    InsertToFile("Stock:{stock};capital:{capital_inicial};capitalfinal:{capital};rendimiento:{rdto}".format(stock=stock_name, capital_inicial=capital_inicial, capital=capital, rdto=rdto))
    
calculate("TEF")
calculate("MSFT")
calculate("MO")
calculate("TSLA")
calculate("IBM")
calculate("SAN")
calculate("YHOO")
calculate("TFX")
calculate("DIS")
calculate("WFC")
calculate("TWTR")
calculate("BIDU")
calculate("BAC")
calculate("AXP")
calculate("FB")



