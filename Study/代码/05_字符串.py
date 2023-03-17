# region 1.字符串格式化
# name = input("请输入你的名称")
# age = input("请输入你的年龄")
# address = input("请输入您的地址")
# weight = float(input("请输入您的体重"))

# %s 字符串占位
# %d 整数占位
# %f 小数占位
# s = "名称%s,年龄%d,地址%s" % (name, int(age), address)
# print(s)
# s1 = "名称{},年龄{},地址{}".format(name, int(age), address)
# print(s1)

# 只需一个赋值时括号可以省略
# s3 = "体重%f" % weight
# print(s3)

# f-string
# s2 = f"名称{name},年龄{int(age)},地址{address}"
# print(s2)
# endregion

# region 2.索引和切片
# s = '欢迎你的到来'
# print(s[3])
# print(s[3:5])
# print(s[:])
# print(s[-3:-1])
# # 第三个-1表示从右往左切
# print(s[-1:-3:-1])
# # 间隔为2 结果“欢你到”
# print(s[::2])
# endregion

# region 3.字符串常规操作
# s = "python"
# s1 = s.capitalize()  # 首字母大写
# print(s1)
#
# s = "i have a apple"
# s1 = s.title()  # 单词首字母大写
# print(s1)
# s1 = s.upper();
# print(s1) # 变成大写字母
#
# # 忽略大小写
# verifyCode = 'xAdW'
# inputVerifyCode = input(f"请输入验证吗{verifyCode}:")
# if inputVerifyCode.upper() == verifyCode.upper():
#     print("验证成功")
# else:
#     print("验证失败")
# endregion

# region 4.替换和切割

# ===============strip================
# s = "   欢迎你们的到来   "
# print(s)
# s1 = s.strip()  # 去除两端空格(空格、\t、\n)
# print(s1)
#
# userName = input("请输入用户名:").strip()
# password = input("请输入密码").strip()
#
# # 案例
# if userName == 'admin':
#     if password == '123456':
#         print('登录成功')
#     else:
#         print('密码错误')
# else:
#     print('用户名错误')

# =============replace 字符替换===============#
# s = "   欢迎  你  们的到  来   "
# s1 = s.replace(" ", "")
# print(s1)
#
# # 案例
# userName = input("请输入用户名:").replace(" ", "")
# password = input("请输入密码").replace(" ", "")
#
# if userName == 'admin':
#     if password == '123456':
#         print('登录成功')
#     else:
#         print('密码错误')
# else:
#     print('用户名错误')

# split() 字符串切割
# s = "欢_迎_你们_的_到来"
# s1 = s.split('_')
# print(s1)

# endregion
