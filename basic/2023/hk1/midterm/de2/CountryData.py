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


    # In đầy đủ thông tin theo định dạng dưới đây:
    # [CountryData: {'code': 'NZL', 'name': 'New Zealand', 'population': 4896096, 'area': 270467.0, 'gdp': 41441.5, 'continent': 'Oceania'}]
    # [CountryData: {'code': 'CHN', 'name': 'China', 'population': 1448230728, 'area': 9706961.0, 'gdp': 10434.8, 'continent': 'Asia'}]
    # [CountryData: {'code': 'DNK', 'name': 'Denmark', 'population': 5833742, 'area': 43094.0, 'gdp': 61063.3, 'continent': 'Europe'}]
    def toString(self):
        countryData_dict = dict()
        countryData_dict['code'] = self.getCode()
        countryData_dict['name'] = self.getName()
        countryData_dict['population'] = self.getPopulation()
        countryData_dict['area'] = self.getArea()
        countryData_dict['gdp'] = self.getGdp()
        countryData_dict['continent'] = self.getContinent()
        return "[CountryData: " + str(countryData_dict) + "]"
        pass

