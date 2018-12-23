import pandas

df = pandas.read_csv(r'D:\Test_Projects\SearchAPI\data\data.csv')
# df1=df2=df3=df
# df1 = df
# print df.head()
# print df.filter(like = 'But', axis = 0)
# df1= df1[df1['givenName'].str.contains('el',case=False)]
# df2 = df2[df2['middleName'].str.contains('el',case=False)]
# df3 = df3[df3['surname'].str.contains('el',case=False)]
# # print df1[['givenName']]
# df2['length'] = df2['givenName'].apply(lambda x: len(x))
# df2['startswith'] =  df2['givenName'].apply(lambda x: 1 if x.startswith('el') else 0)
# print df2[['middleName', 'length','startswith']]
# # print df3['surname']
# # print (df[df['givenName'].str.contains('el',case=False) | df['middleName'].str.contains('el',case=False) | df['surname'].str.contains('el',case=False)])
final_df = pandas.DataFrame()
dict = {0:'givenName', 1:'middleName', 2:'surname'}
for i in xrange(3):
	col_name = dict[i]
	print col_name
	temp = df
	temp= temp[temp[col_name].str.contains('emer',case=False)]
	temp['length'] = temp[col_name].apply(lambda x: len(x))
	temp['startswith'] =  temp['givenName'].apply(lambda x: 1 if x.lower().startswith('emer') else 0)
	final_df = final_df.append(temp, ignore_index=True)
final_df.sort_values(['startswith', 'length'], ascending=[False, False], inplace=True)
# print final_df
print final_df.shape[0]