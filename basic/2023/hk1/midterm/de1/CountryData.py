class CountryData:
    def __init__(self, code,
                       name,
                       population,
                       area,
                       gdp,
                       continent):
        self.__code = code
        self.__name = name
        self.__population = population
        self.__area = area
        self.__gdp = gdp
        self.__continent = continent
    

    def getCode(self):
        return self.__code

    def getName(self):
        return self.__name

    def getPopulation(self):
        return self.__population

    def getArea(self):
        return self.__area

    def getGdp(self):
        return self.__gdp

    def getContinent(self):
        return self.__continent


    # Lấy đầy đủ thông tin theo định dạng dưới đây:
    # Params:
    # Output: info - String: trả về theo định dạng được yêu cầu
    # Requirement: Thực hiện trả về xâu ký tự chứa đầy đủ thông tin của CountryData theo định dạng như sau:
    # [CountryData: {'code': 'CHN', 'name': 'China', 'population': 1448230728, 'area': 9706961.0, 'gdp': 10434.8, 'continent': 'Asia'}]
    def toString(self):
        # TODO
        pass

