import core
import datetime
from datetime import date, datetime, timedelta
from yahoo_finance import Share
from core.agents import iController
from core.utils.file.File import File
from core.data.stock import stock

class Controller:
    PARAM_NAME_STOCK_NAME = "stock_name"
    #PARAM_NAME_INIT_DATE = "init_date"

    def init(self):
        pass

    def run(self, query):
        stock_name = query.get(Controller.PARAM_NAME_STOCK_NAME)
        data = self.__read_from_offline_stock(stock_name)
        if(data == {}):
            data = self.__save_on_filesystem(stock_name, self.__online_historical_data(stock_name))
        return self.__create_data(data)
    
    def __create_data(self, data):
        data_return = []
        for date in data:
            try:
                dataappend = stock(date, data[date]["Close"], data[date]["Open"], data[date]["High"], data[date]["Low"], data[date]["Volume"])
                data_return.append(dataappend)
            except:
                print "error"            

        return sorted(data_return, key=lambda stock:stock.date)
                

    def __save_on_filesystem(self, stock, data_from_web):
        data_to_store = []
        for data in data_from_web:
            stock_result = {}
            result = {}
            
            result["Open"] = data["Open"]
            result["High"] = data["High"]
            result["Low"] = data["Low"]
            result["Close"] = data["Close"]
            result["Volume"] = data["Volume"]    

            stock_result[data["Date"]] = result
            data_to_store.append(stock_result)
        file_controller = File()
        file_controller.save(stock, data_to_store)
        return data_to_store

    def __read_from_offline_stock(self, stock):
        file_controller = File()
        return file_controller.read(stock)

    def __online_historical_data(self, stock):
        yahoo = Share(stock)
        result = yahoo.get_historical('2011-08-01', '2016-08-01')
        return result