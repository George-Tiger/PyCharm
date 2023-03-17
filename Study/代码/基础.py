import datetime

curDate = datetime.date(2022,12,23)
futrueDate = curDate + datetime.timedelta(days=186)
print("日期{}".format(futrueDate))