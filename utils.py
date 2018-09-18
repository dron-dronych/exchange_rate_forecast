from pandas import read_excel, concat
import re

class ExchangeRatesReader(object):
    """" reads .xls data and puts them in one dataframe """
    
    def __init__(self, filename):
        self._data = read_excel(filename ,sheet_name=None)
        
    def to_dataframe(self):
        self.sheetnames = []
        # Search with regex to match sheet names that are digits only. Either a year from the 1990-s or the 2000s and further on
        regex = re.compile('(199+[0-9])|(2+[0-9]{3})')
        
        for key in self._data.keys():
            result = regex.match(key)

            if result:
                self.sheetnames.append(key)

            else:
                continue

        return concat(self._data)
