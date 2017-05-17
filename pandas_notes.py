#usefu code snippets
#https://gist.github.com/bsweger/e5817488d161f37dcbd2
#http://stackoverflow.com/questions/18969034/parsing-data-from-long-to-wide-format-in-python/19328258#19328258
#https://archive.org/details/pyvideo_305___python-in-quantitative-finance-158



dataheader = ['Date1', 'day', 'time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Position', 'Settlement']
df_main = pd.read_csv('C:/Users/4/Desktop/data_test/min60/Ag(T+D).csv', sep=',', header=0, names=dataheader, skip_blank_lines=True)
df_main['DateTime'] = df_main[['day', 'time']].apply(getDateTimeStr11, axis=1)
df_main[['DateTime', 'Open', 'High', 'Low', 'Close', 'Settlement', 'Position', 'Volume']].to_csv('C:/Users/4/Desktop/data_test/min60/Ag(T+D)11.csv', index=False)
plt.plot(df_main['Close'])

### 读取csv格式文件，并将第一列作为index
df = pd.read_csv("D:/get_data/dataframe0.csv", index_col=0)
#不将第一列作为index
df = pd.read_csv("D:/get_data/dataframe0.csv", index_col=False)

### DataFrame的转秩，即行列互换
df = df.transepose() 或者 df = df.T

### 删除某一列
del df['column_name']

###删除多行或多列
aa = [[234, 44, 55], [657, 77, 77], [33, 55, 457]]
df = pd.DataFrame(aa, columns=['hi','hello','ok'], index=[22, 33, 44])
print(df)
df.drop(['hi', 'hello'], axis=1, inplace=True)  #删除列
df.drop([22, 33], axis=0, inplace=True)       #删除行

### 增加某一列
df['new_column_name'] = Series(np.random.randn(sLength), index=df.index)

###变更index和columns
positions_df.columns = [v2 for (v1, v2) in positions_df.columns.values]
positions_df.index = [str(index).split()[0] for index in positions_df.index]

###读取某一行的值
df.ix['one'] 读取index为one的行的series

### 遍历DataFrame（如果你必须这么做的话）
for index, row in df.iterrows():   # 获取每行的index、row
    index_val = index
    col_val = row['col_name']

df1 = pd.read_csv("e:/get_data/dataframe1.csv")
df2 = pd.read_csv("e:/get_data/dataframe2.csv")
df3 = pd.read_csv("e:/get_data/dataframe3.csv")
df = pd.concat([df1, df2, df3])
df = df.drop_duplicates(subset='datetime')
df = df.sort(columns=['datetime'])
df.to_csv("e:/get_data/dataframe0.csv", index=False)

### 获取列数
len(df.columns)  
df.shape[1]   # faster

### 获取行数
len(df.index)
df.shape[0]   # faster

###获取df所有数值的个数
df.size

### 改变dataframe的列名：
df.rename(columns={'oldName1': 'newName1', 'oldName2': 'newName2'},  inplace=True)
# 或者
df = df.rename(columns={'oldName1': 'newName1', 'oldName2': 'newName2'})

### 改变dataframe的列名，变成大写
df.rename(columns=lambda x: x.decode().upper(), inplace=True)

### 改变dataframe的index成员值：
df.rename(index={'oldIndexName1': 'newIndexName1', 'oldIndexName2': 'newIndexName2'},  inplace=True)

### 改变dataframe的index成员值，变成大写
df.rename(index=lambda x: x.decode().upper(), inplace=True)

### 设置某一列为index
df.set_index('column_name', inplace=True)

### 改变index的名字
df.index.rename('new_index_name', inplace=True)

### 判断index是否已经排序
df.index.is_monotonic
df.index.is_monotonic_increasing
df.index.is_monotonic_decreasing

### 转换series和dataframe
def conversion_func(x):
    if x!=0:
        return int(x)**2
    else:
        return -1

plot_df['y'] = plot_df['y'].map(conversion_func)
plot_df = plot_df.applymap(conversion_func)

###


rng = pd.date_range(start = '2014-01-01',periods = 100)
    df = pd.DataFrame({'Open' : np.random.randint(-10, 10, size=len(rng)),
                       'Close' : np.random.randint(-10, 10, size=len(rng)),
                       'Volume' : np.random.randint(-10, 10, size=len(rng))}, 
                       index=rng)
    df['A'] = df[(df>=4) & (df<=7)].count(axis=1) - df[df<=-4].count(axis=1)
    df['B'] = df[df>=3].count(axis=1) - df[df<=-3].count(axis=1)
    df['C'] = df[df>=2].count(axis=1) - df[df<=-2].count(axis=1)
    df111 = df.loc[:,('A', 'B', 'C')]
    print(df)

http://jingyan.baidu.com/season/43456?pn=0

