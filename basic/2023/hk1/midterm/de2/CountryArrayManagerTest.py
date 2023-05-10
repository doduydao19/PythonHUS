from CountryManager import CountryArrayManager
from CountryData import CountryData

def testOriginalData():
    countryArrayManager = init()
    codeString = countryArrayManager.codeOfCountriesToString(countryArrayManager.getCountryDataArray(), countryArrayManager.getLength())
    print(codeString)


def testSortIncreasingByPopulation():
    countryArrayManager = init()
    countries = countryArrayManager.sortIncreasingByPopulation()
    codeString = countryArrayManager.codeOfCountriesToString(countries, len(countries))
    print(codeString)

def testSortIncreasingByArea():
    countryArrayManager = init()
    countries = countryArrayManager.sortIncreasingByArea()
    codeString = countryArrayManager.codeOfCountriesToString(countries, len(countries))
    print(codeString)

def testSortIncreasingByGdp():
    countryArrayManager = init()
    countries = countryArrayManager.sortIncreasingByGdp()
    codeString = countryArrayManager.codeOfCountriesToString(countries, len(countries))
    print(codeString)


def testFilterLeastPopulousCountries():
    countryArrayManager = init()
    howMany = 5
    countries = countryArrayManager.filterLeastPopulousCountries(howMany)
    codeString = countryArrayManager.codeOfCountriesToString(countries, howMany)
    print(codeString)


def testFilterSmallestAreaCountries():
    countryArrayManager = init()
    howMany = 5
    countries = countryArrayManager.filterSmallestAreaCountries(howMany)
    codeString = countryArrayManager.codeOfCountriesToString(countries, howMany)
    print(codeString)


def testFilterLowestGdpCountries():
    countryArrayManager = init()
    howMany = 5
    countries = countryArrayManager.filterLowestGdpCountries(howMany)
    codeString = countryArrayManager.codeOfCountriesToString(countries, howMany)
    print(codeString)

def testPrintCoutryData():
    countryArrayManager = init()
    countryArrayManager.printCountryDataArray()

def testFilterContinent(continent):
    countryArrayManager = init()
    countries = countryArrayManager.filterContinent(continent)
    codeString = countryArrayManager.codeOfCountriesToString(countries, len(countries))
    print(codeString)

def testRankingCountryByAreaAndContinent():
    countryArrayManager = init()
    countries = countryArrayManager.rankingCountryByAreaAndContinent()
    print(countries)

def init():
    filePath = "data.csv"
    return readArrayData(filePath)

def readArrayData(filePath):
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


if __name__ == '__main__':
    for i in range(0, 10):
        print("case = test", i)
        print("input =", i)
        print("output =", end=" ")
        match i:
            case 0:
                testPrintCoutryData()
            case 1:
                testOriginalData()
            case 2:
                testSortIncreasingByPopulation()
            case 3:
                testSortIncreasingByArea()
            case 4:
                testSortIncreasingByGdp()
            case 5:
                testFilterLeastPopulousCountries()
            case 6:
                testFilterSmallestAreaCountries()
            case 7:
                testFilterLowestGdpCountries()
            case 8:
                testFilterContinent('Asia')
            case 9:
                testRankingCountryByAreaAndContinent()
        print()


