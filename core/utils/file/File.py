import os
import re

class File:
    
    def __init__(self):
        self.__stock_name_directory = os.path.join(self.__get_current_directory(), "stocks")
        self.__check_directory(self.__stock_name_directory)

    def save(self, stockName, data):
        name = "{stock_name}.{suffix}".format(stock_name=stockName, suffix="sck")
        file_name = os.path.join(self.__stock_name_directory,name)      
        saveFile= open(file_name,'w')
        for d in data:
            saveFile.writelines(self.__get_line_from_data(d))
        saveFile.close()
            
    def __get_line_from_data(self, d):
        data = None
        cDate = None
        for k in d:
            data = d[k]
            cDate = k
        return "{date};{open};{high};{low};{close};{volume}\n\r".format(date=cDate,
                        open=data["Open"],
                        high=data["High"],
                        low=data["Low"],
                        close=data["Close"],
                        volume=data["Volume"])

    def read(self, stockName):
        name = "{stock_name}.{suffix}".format(stock_name=stockName, suffix="sck")
        file_name = os.path.join(self.__stock_name_directory,name)

        stock_values= {}

        try:
            data = self.__open_file(file_name)
        except Exception as e:
            data = []

        for iter in range(0,len(data)):
            lineString = data[iter]
            if lineString == "":
                continue
            values = lineString.split(";")

            result = {}
            result["Open"] = values[1]
            result["High"] = values[2]
            result["Low"] = values[3]
            result["Close"] = values[4]
            result["Volume"] = values[5]

            stock_values[values[0]] = result

        return stock_values

    def __check_directory(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)

    def __get_current_directory(self):
        return os.getcwd()

    def __open_file(self, file_name):
        'opens a file for the data that the program needs'
        inputFile= open(file_name,'r')
        inputData =inputFile.readlines()
        inputFile.close()
        'cleans up the input data from unwanted characters like new line'
        cleanedData =[]
        pattern = re.compile(r'\n',  re.IGNORECASE)
        pattern_r = re.compile(r'\r',  re.IGNORECASE)
        for iter in inputData:
            cleaned = pattern_r.sub('', iter)
            cleanedData.append(pattern.sub('', cleaned))
        return cleanedData
