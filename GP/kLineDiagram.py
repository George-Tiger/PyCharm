import matplotlib
import mplfinance as mpf
matplotlib.use('tkagg')
import tushare as ts
import pandas as pd

token = '97148d83b517a6ad601f74c9953b2c1716c0b85d82346fb4a53b3076'
ts.set_token(token)
pro = ts.pro_api()

# 股票代码是北方稀土的
data = pro.daily(ts_code="600111.SH", start_date='20180701', end_date='20211201')
datawrite = data.iloc[:, 1:]
datawrite['trade_date'] = pd.to_datetime(datawrite['trade_date'])  # 原来的类型为Series
datawrite.set_index('trade_date', inplace=True)

mpf.plot(datawrite.iloc[30:0:-1, 0:4], type='candle')
