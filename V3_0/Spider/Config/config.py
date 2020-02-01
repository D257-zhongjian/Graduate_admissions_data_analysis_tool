from V3_0.Storer.GetData.api import getPickleFileData
from V3_0.Storer.Config.api import getDataBasePath
from V3_0.Storer.WriteData.api import writeDataToPickleFile

_domain = 'http://yz.chsi.com.cn'
_headers = {'User-Agent':
				'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6814.400 QQBrowser/10.3.3005.400'
			}


def getDomain(): return _domain


def getHeaders(): return _headers


pklPath = getDataBasePath() + '\\CountData.pkl'


class Config:
	count, errCount, errNum, errMax, count2 = 0, 0, 0, 0, 0
	smallestFileSize = 999999999


def getCount(): return Config.count


def setCount(c): Config.count = c


def getErrCount(): return Config.errCount


def setErrCount(c): Config.errCount = c


def getErrNum(): return Config.errNum


def setErrNum(c): Config.errNum = c


def getErrMax(): return Config.errMax


def setErrMax(c): Config.errMax = c


def getCount2(): return Config.count2


def setCount2(c): Config.count2 = c


def getSmallestFileSize(): return Config.smallestFileSize


def setSmallestFileSize(c): Config.smallestFileSize = c


def initCount():
	try:
		data = getPickleFileData(pklPath)
	except Exception as err:
		print(err)
	else:
		setCount(data['count'])
		setErrCount(data['errCount'])
		setErrCount(data['errNum'])
		setErrMax(data['errMax'])
		setCount2(data['count2'])
		setSmallestFileSize(data['smallestFileSize'])


def saveCount():
	dic = {}
	dic.update({'count': getCount()})
	dic.update({'errCount': getErrCount()})
	dic.update({'errNum': getErrNum()})
	dic.update({'errMax': getErrMax()})
	dic.update({'count2': getCount2()})
	dic.update({'smallestFileSize': getSmallestFileSize()})
	print('saving ')
	writeDataToPickleFile(pklPath, dic)