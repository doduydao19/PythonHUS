import CountryManager

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
        countryData_dict = dict()
        countryData_dict['code'] = self.getCode()
        countryData_dict['name'] = self.getName()
        countryData_dict['population'] = self.getPopulation()
        countryData_dict['area'] = self.getArea()
        countryData_dict['gdp'] = self.getGdp()
        countryData_dict['continent'] = self.getContinent()
        return "[CountryData: " + str(countryData_dict) + "]"
        pass

class CountryArrayManager:

    # hàm dựng
    # countryDataArray: Chứa danh sách các CountryData
    def __init__(self):
        self.countryDataArray = self.readArrayData(filePath='data.csv')

    # Thực hiện đọc dữ liệu từ tệp tin
    # Params: filePath - String: đường dẫn tệp tin
    # Output: countries - list: danh sách các CountryData
    # Requirement: Đọc tệp tin filePath, các trường dữ liệu được phân tách bởi dấu phẩy.
    #              Dòng đầu: code,country,population,area,gdp,continent
    #              Dòng cuối: dòng trắng -> kết thúc việc đọc
    #              Các dòng còn lại: NZL,New Zealand,4896096,270467,41441.5,Oceania
    #                                CHN,China,1448230728,9706961,10434.8,Asia
    def readArrayData(self, filePath):
        r = []
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
                    r.append(newCountryData)
        return r



    # Sắp xếp dữ liệu theo thứ tự field giảm dần.
    # Params: field - String: Trường dữ liệu
    # Output: countries - list: danh sách các CountryData
    # Requirement: Trả về danh sách các CountryData đã được sắp xếp theo thứ tự giảm dần của field
    #               field có 3 loại:
    #               - "P": Population
    #               - "A": Area
    #               - "G": Gdp
    def sortDecreasingByField(self, field):
        data = self.countryDataArray.copy()
        if field == "P":
            data.sort(key=lambda x: -x.getPopulation())
        if field == "A":
            data.sort(key=lambda x: -x.getArea())
        if field == "G":
            data.sort(key=lambda x: -x.getGdp())
        return data
    pass

    # Lọc ra những nước ở continent(châu lục)
    # Params: continent - String: tên châu lục
    # Output: countries - list: danh sách các CountryData
    # Requirement: Trả về danh sách các CountryData sau khi lọc bởi continent và được sắp xếp theo thứ tự A-Z theo trường code.
    def filterContinent(self, continent):
        result = []
        for country in self.countryDataArray:
            if country.getContinent() == continent:
                result.append(country)
        result.sort(key=lambda x: x.getCode())
        return result
        pass

    # Lọc ra những nước theo field
    # Params: - howMany - int: số lượng các nước
    #         - field - String: trường dữ liệu
    # Output: countries - list: danh sách các CountryData
    # Requirement: Trả về danh sách có howMany CountryData sau khi lọc bởi field và được sắp xếp theo thứ tự giảm dần theo field.
    def filterByField(self, field, howMany):
        countries = self.sortDecreasingByField(field)[:howMany]
        return countries
        pass


    # Hàm lấy danh sách các nước theo code
    # Params: - countryDataArray - list: danh sách các CountryData
    #         - length - int: số lượng các nước
    # Output: codes - string: trả về theo định dạng được yêu cầu
    # Requirement: Thực hiện lấy code của các CountryData đã sắp xếp theo thứ tự A-Z và trả về theo định dạng:
    #               [CHN USA VNM]
    def codeOfCountriesToString(self):
        codes = []
        for i in range(len(self.countryDataArray)):
            codes.append(self.countryDataArray[i].getCode())
        codes_string = " ".join(codes)
        return "["+ codes_string+ "]"
        pass


    # In đầy đủ thông tin các nước
    # Params:
    # Output:  - void: in theo định dạng
    # Requirement: Thực hiện in các CountryData đã sắp xếp theo thứ tự A-Z theo định dạng mỗi nước được hiển thị trên 1 dòng như sau:
    # [CountryData: {'code': 'CHN', 'name': 'China', 'population': 1448230728, 'area': 9706961.0, 'gdp': 10434.8, 'continent': 'Asia'}]
    # [CountryData: {'code': 'NZL', 'name': 'New Zealand', 'population': 4896096, 'area': 270467.0, 'gdp': 41441.5, 'continent': 'Oceania'}]

    def printCountryDataArray(self):
        for c in self.countryDataArray:
            print(c.toString())
        pass

    # Sắp xếp các nước theo GDP:
    # Params:
    # Output: codes - list: danh sách các code của CountryData theo định dạng được yêu cầu
    # Requirement: 1. Thực hiện gom nhóm các CountryData theo từng continent.
    #              2. Thực hiện sắp xếp các CountryData trong cùng 1 contient theo GDP
    #              3. Thực hiện lưu các code của CountryData theo đúng thứ tự vừa sắp xếp theo GDP
    #              4. Thực hiện sắp xếp các nhóm continent theo tổng GDP của toàn bộ các CountryData thuộc continent tương ứng
    #              5. Trả về theo định dạng
    #              ví dụ:
    #               [[Europe, [UKR RUS ESP ITA FRA]], [South America, [BRA ARG]]]
    def rankingCountryByGDPAndContinent(self):
        contients = set()
        for countryData in self.countryDataArray:
            continent = countryData.getContinent()
            contients.add(continent)

        result = dict()
        for continent in contients:
            countries = self.filterContinent(continent)
            countries.sort(key=lambda x: x.getGdp())
            gdps = [country.getGdp() for country in countries]
            codes = [country.getCode() for country in countries]
            result[continent] = {'codes': codes, 'gpds': sum(gdps)}

        sorted_dict = [[k, v['codes']] for k, v in sorted(result.items(), key=lambda item: -item[1]['gpds'])]

        return sorted_dict


if __name__ == '__main__':
    countryArrayManager_teacher = CountryArrayManager()
    countryDataArray_teacher =  countryArrayManager_teacher.countryDataArray

    countryArrayManager_student = CountryManager.CountryArrayManager()

    for i in range(1, 8):
        if i == 1:
            print("case = test readArrayData, printCountryDataArray")
            print("input =", 1)
            print("output =", end=" ")
            # countryArrayManager_student.printCountryDataArray()
            countryArrayManager_teacher.printCountryDataArray()


        if i == 2:
            print("case = test sortDecreasingByField")
            field = "G"
            print("input =", 2)
            print("output =", end=" ")
            countryArrayManager_student.countryDataArray = countryDataArray_teacher
            # countries = countryArrayManager_student.sortDecreasingByField(field)

            countries = countryArrayManager_teacher.sortDecreasingByField(field)

            for i in countries:
                print(i.getCode(), end=", ")

        if i == 3:
            print("case = test filterContinent")
            continent = "Asia"
            print("input =", 3)

            print("output =", end=" ")
            countryArrayManager_student.countryDataArray = countryDataArray_teacher
            # countries = countryArrayManager_student.filterContinent(continent)

            countries = countryArrayManager_teacher.filterContinent(continent)

            for i in countries:
                print(i.getCode(), end=', ')
        if i == 4:
            print("case = test filterByField")
            field = "G"
            howMany = 5
            print("input =", 4)

            print("output =", end=" ")
            countryArrayManager_student.countryDataArray = countryDataArray_teacher
            # countries = countryArrayManager_student.filterByField(field, howMany)

            countries = countryArrayManager_teacher.filterByField(field, howMany)

            for i in countries:
                print(i.getCode(), end= ', ')
        if i == 5:
            print("case = test codeOfCountriesToString")
            print("input =", 5)

            print("output =", end=" ")
            countryArrayManager_student.countryDataArray = countryDataArray_teacher
            # countries = countryArrayManager_student.codeOfCountriesToString()

            countries = countryArrayManager_teacher.codeOfCountriesToString()
            print(countries)

        if i == 6:
            print("case = test rankingCountryByGDPAndContinent")
            print("input =", 6)
            print("output =", end=" ")
            countryArrayManager_student.countryDataArray = countryDataArray_teacher
            # countries = countryArrayManager_student.rankingCountryByGDPAndContinent()

            countries = countryArrayManager_teacher.rankingCountryByGDPAndContinent()

            print(countries)
        print()
        print()
