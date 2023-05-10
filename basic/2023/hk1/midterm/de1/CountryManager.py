class CountryArrayManager:

    # hàm dựng
    def __init__(self):
        # countryDataArray: danh sách các CountryData
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
        # TODO
        pass


    # Sắp xếp dữ liệu theo thứ tự field giảm dần.
    # Params: field - String: Trường dữ liệu
    # Output: countries - list: danh sách các CountryData
    # Requirement: Trả về danh sách các CountryData đã được sắp xếp theo thứ tự giảm dần của field
    #               field có 3 loại:
    #               - "P": Population
    #               - "A": Area
    #               - "G": Gdp
    def sortDecreasingByField(self, field):
        # TODO
        pass

    # Lọc ra những nước ở continent(châu lục)
    # Params: continent - String: tên châu lục
    # Output: countries - list: danh sách các CountryData
    # Requirement: Trả về danh sách các CountryData sau khi lọc bởi continent và được sắp xếp theo thứ tự A-Z theo trường code.
    def filterContinent(self, continent):
        # TODO
        pass

    # Lọc ra những nước theo field
    # Params: - howMany - int: số lượng các nước
    #         - field - String: trường dữ liệu
    # Output: countries - list: danh sách các CountryData
    # Requirement: Trả về danh sách có howMany CountryData sau khi lọc bởi field và được sắp xếp theo thứ tự giảm dần theo field.
    def filterByField(self, field, howMany):
        # TODO
        pass


    # Hàm lấy danh sách các nước theo code
    # Params: - countryDataArray - list: danh sách các CountryData
    #         - length - int: số lượng các nước
    # Output: codes - string: trả về theo định dạng được yêu cầu
    # Requirement: Thực hiện lấy code của các CountryData đã sắp xếp theo thứ tự A-Z và trả về theo định dạng:
    #               [CHN USA VNM]
    def codeOfCountriesToString(self):
        # TODO
        pass


    # In đầy đủ thông tin các nước
    # Params:
    # Output:  - void: in theo định dạng
    # Requirement: Thực hiện in các CountryData đã sắp xếp theo thứ tự A-Z theo định dạng mỗi nước được hiển thị trên 1 dòng như sau:
    # [CountryData: {'code': 'CHN', 'name': 'China', 'population': 1448230728, 'area': 9706961.0, 'gdp': 10434.8, 'continent': 'Asia'}]
    # [CountryData: {'code': 'NZL', 'name': 'New Zealand', 'population': 4896096, 'area': 270467.0, 'gdp': 41441.5, 'continent': 'Oceania'}]

    def printCountryDataArray(self):
        # TODO
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
        # TODO
        pass
