class CountryArrayManager:
    # Hàm dựng
    def __init__(self):
        self.countryDataArray = list()


    def getLength(self):
        return len(self.countryDataArray)


    def getCountryDataArray(self):
        return self.countryDataArray


    # Thêm dữ liệu vào vị trí cuối.
    def append(self, countryData):
        self.countryDataArray.append(countryData)
        pass


    # Sắp xếp dữ liệu theo thứ tự dân số (population) tăng dần.
    # Hàm sắp xếp không nên làm thay đổi mảng dữ liệu gốc.
    # Vì vậy cấn cấp phát một mảng mới, copy dữ liệu gốc sang mảng mới,
    # sau đó sắp xếp trên mảng mới, và trả ra ngoài hàm mảng mới đã được sắp xếp.
    # Nếu cần in thông tin theo dân số tăng dần, in thông tin từ mảng dữ liệu mới này.
    # Việc sắp xếp có thể sử dụng các thuật toán sắp xếp, như sellection sort, bubble sort, insertion sort.
    def sortIncreasingByPopulation(self):
        data = self.countryDataArray.copy()
        data.sort(key=lambda x: x.getPopulation())
        return data
        pass
    

    # Sắp xếp dữ liệu theo thứ tự diện tích (area) tăng dần.
    # Hàm sắp xếp không nên làm thay đổi mảng dữ liệu gốc.
    # Vì vậy cấn cấp phát một mảng mới có độ dài là length, copy dữ liệu gốc sang mảng mới,
    # sau đó sắp xếp trên mảng mới, và trả ra ngoài hàm mảng mới đã được sắp xếp.
    # Nếu cần in thông tin theo dân số tăng dần, in thông tin từ mảng dữ liệu mới này.
    # Việc sắp xếp có thể sử dụng các thuật toán sắp xếp, như sellection sort, bubble sort, insertion sort.
    def sortIncreasingByArea(self):
        data = self.countryDataArray.copy()
        data.sort(key=lambda x: x.getArea())
        return data
        pass


    # Sắp xếp dữ liệu theo thứ tự gdp tăng dần.
    # Hàm sắp xếp không nên làm thay đổi mảng dữ liệu gốc.
    # Vì vậy cấn cấp phát một mảng mới có độ dài là length, copy dữ liệu gốc sang mảng mới,
    # sau đó sắp xếp trên mảng mới, và trả ra ngoài hàm mảng mới đã được sắp xếp.
    # Nếu cần in thông tin theo dân số tăng dần, in thông tin từ mảng dữ liệu mới này.
    # Việc sắp xếp có thể sử dụng các thuật toán sắp xếp, như sellection sort, bubble sort, insertion sort.
    def sortIncreasingByGdp(self):
        data = self.countryDataArray.copy()
        data.sort(key=lambda x: x.getGdp())
        return data
        pass


    # Lọc ra những nước ở vùng continent (ví dụ, Châu Á).
    def filterContinent(self, continent):
        result = []
        for country in self.countryDataArray:
            if country.getContinent() == continent:
                result.append(country)
        return result
        pass

      # Lọc ra howMany nước có dân số ít nhất.
    def filterLeastPopulousCountries(self, howMany):
        countries = self.sortIncreasingByPopulation()[:howMany]
        return countries
        pass


    # Lọc ra howMany nước có diện tích nhỏ nhất.
    def filterSmallestAreaCountries(self, howMany):
        countries = self.sortIncreasingByArea()[:howMany]
        return countries
        pass


    # Lọc ra howMany nước có GDP thấp nhất.
    def filterLowestGdpCountries(self, howMany):
        countries = self.sortIncreasingByGdp()[:howMany]
        return countries
        pass

    # Hàm lấy danh sách các nước theo code, là String có format dạng, ví dụ [USA VNM].
    def codeOfCountriesToString(self, countryDataArray, length):
        codes = []
        for i in range(length):
            codes.append(countryDataArray[i].getCode())
        codes_string = " ".join(codes)
        return "["+ codes_string+ "]"
        pass


    # In đầy đủ thông tin các nước trong một mảng, mỗi mảng in trên 1 dòng.
    # Ví dụ:
    # [CountryData: {'code': 'NZL', 'name': 'New Zealand', 'population': 4896096, 'area': 270467.0, 'gdp': 41441.5, 'continent': 'Oceania'}]
    # [CountryData: {'code': 'CHN', 'name': 'China', 'population': 1448230728, 'area': 9706961.0, 'gdp': 10434.8, 'continent': 'Asia'}]
    # [CountryData: {'code': 'DNK', 'name': 'Denmark', 'population': 5833742, 'area': 43094.0, 'gdp': 61063.3, 'continent': 'Europe'}]
    def printCountryDataArray(self):
        for c in self.countryDataArray:
            print(c.toString())
        pass

    # xếp hạng các nước theo diện tích giảm dần và khu vực theo định dạng từ điển:
    # key: continent được sắp xếp tắng dần theo tổng area của cả khu vực
    # value: danh sách code của các nước đã sắp xếp giảm dần theo diện tích
    # ví dụ:
    # {'Oceania': '[AUS NZL]', 'North America': '[CAN USA MEX]', 'South America': '[BRA ARG]', 'Africa': '[DZA NGA]', 'Europe': '[RUS UKR FRA ESP SWE DEU ITA GBR DNK NLD CHE]', 'Asia': '[CHN IND KAZ IDN PAK THA JPN VNM BGD QAT SGP]'}
    def rankingCountryByAreaAndContinent(self):
        contients = set()
        for countryData in self.countryDataArray:
            continent = countryData.getContinent()
            contients.add(continent)

        result = dict()
        for continent in contients:
            countries = self.filterContinent(continent)
            countries.sort(key=lambda x: -x.getArea())
            areas = [country.getArea() for country in countries]
            codes = self.codeOfCountriesToString(countries, len(countries))
            result[continent] = {'codes': codes, 'areas': sum(areas)}

        sorted_dict = {k: v['codes'] for k, v in sorted(result.items(), key=lambda item: item[1]['areas'])}
        return sorted_dict



