import pandas as pd

class SearchProcessor:

	def __init__(self, search_str):
		self.CSVFile = r'D:\Test_Projects\SearchAPI\data\data.csv'
		self.df = self.readFile()
		self.search_str = search_str 

	def readFile(self):
		df = pd.read_csv(self.CSVFile)
		return df

	def startSearch(self):
		final_df = pd.DataFrame()
		dict = {0:'givenName', 1:'middleName', 2:'surname'}
		for i in xrange(3):
			col_name = dict[i]
			temp = self.df
			temp= temp[temp[col_name].str.contains(self.search_str,case=False)]
			temp['length'] = temp[col_name].apply(lambda x: len(x))
			temp['startswith'] =  temp['givenName'].apply(lambda x: 1 if x.lower().startswith(self.search_str) else 0)
			final_df = final_df.append(temp, ignore_index=True)
		final_df.sort_values(['startswith', 'length'], ascending=[False, False], inplace=True)
		return final_df[['givenName','middleName','surname']]