from CountryManager import CountryArrayManager
from CountryData import CountryData

class App:
    def __init__(self, filePath):
        self.countryArrayManager = self.readArrayData(filePath)

    # Thực hiện đọc dữ liệu từ filePath và trả về đối tượng coutryArrayManager
    # Dòng đầu chứa tiêu đề, các trường cách nhau bởi dấu ","

    def readArrayData(self, filePath):
        countryArrayManager = CountryArrayManager()
        with open(filePath, 'r') as file:
            for line in file:
                if line != "":
                    line = line.strip()
                    dataList = line.split(",")
                    if len(dataList) != 6:
                        continue

                    if dataList[0]=="code":
                        continue

                    newCountryData = CountryData(
                            code=dataList[0],
                            name=dataList[1],
                            population=int(dataList[2]),
                            area=float(dataList[3]),
                            gdp=float(dataList[4]),
                            continent=dataList[5])
                    countryArrayManager.append(newCountryData)
        return countryArrayManager
