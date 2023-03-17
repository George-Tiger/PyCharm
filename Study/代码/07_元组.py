# region 输出
t = ('上海','北京')
print(t)

# 元组中的元素不可变
# t[0]='广州' #object does not support item assignment
# print(t)

# 元组中只有一个元素的时候，默认是str类型，可以在元素后加逗号正确识别
t=('上海',)
print(type(t))
# endregion