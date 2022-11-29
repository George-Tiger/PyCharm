# while循环
# i = 1
# j = 0
# while i <= 100:
#     j = j + i
#     i = i + 1
#
# print(j);

# break,continue用法
# while True:
#     context = input("请输入内容")
#     if context == "结束":
#         break  # 结束语句
#     elif context == "继续":
#         print("continue")
#         continue  # 终止本次循环,继续下一次循环
#     else:
#         print(context)

# for用法
s = "你好,我是二哈"
for i in s:
    print(i)

for i in range(10):  # 输出0~9
    print(i)

for i in range(14, 17):  # 输出14~16
    print(i)

for i in range(20, 30, 2):  # 输出20,22,24,26,28 间隔:2
    print(i)
