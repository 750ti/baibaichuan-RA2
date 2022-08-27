"""
作者：BBC
日期：2022年05月11日

描述：红警有多少颗树？ 遍历txt文本，并逐行判断比对，生成结果

"""


from calendar import c
import time

import re

'''
start = time.time()
# map=open("\\冰天雪地.map")
# map=open("D:\\PyCharm\\Python_RA2\\冰天雪地.map")
map=open(f"D:\PyCharm\Python_RA2\冰天雪地.map")


a=1
for list in map:
    if "=TREE" in list:
        print(f"第{a}颗树，编号+树类型:",list,end="")
        a+=1
    continue

print(f'======成功遍历该地图，发现了【{a}】颗树======')
map.close() # 关闭文件
start2 = time.time()

print(start,start2,start2-start)
#只保留小数点后两位
print(round(start2-start,4))

# 第一版的写法
'''



map=open(f"D:\PyCharm\Python_RA2\冰天雪地.map")

# a=1
# for list in map:
#     # 用正则表达式判断Terrain是否在list中
#     if re.search("Terrain",list):
#         if "[" in list:
#             break
#         if re.search(";",list):
#             continue
#         else:
#             if re.search("=TREE",list):
#                 print(f"第{a}颗树，编号+树类型:",list,end="")
#                 a+=1

a=0
b=1
run = False

# for list in map:
#     if "Terrain" in list:
#         run = 1
#         print("启动")
#     if run:
#         if "Terrain" in list:
#             pass
#         else:
#             if list[0] == "[":
#                 run = 0
#                 print("")
#                 print(f"【脚本结束】本次运行共判断【{b}】次")
#                 print("")
#                 break

#         if ";" in list: 
#             pass
#         else:
#             if "=TREE" in list:
#                 a+=1
#                 print(f"第{a}颗树，编号+树类型:",list,end="")
                
#         b+=1
for list in map:
    if "Terrain" in list:
        run = True
        print("启动")
    if run:
        if "Terrain" not in list and list[0] == "[":
            run = False
            print("")
            print(f"【脚本结束】本次运行共判断【{b}】次")
            print("")
            break
        # lists = list.strip()
        if ";" not in list and "=TREE" in list: 
            a+=1
            print(f"第{a}颗树，编号+树类型:",list,end="")
        b+=1

# print(list)

print(f'============成功遍历地图')
print(f"============判断【{b}】次")
print(f'============发现【{a}】颗树')


map.close() # 关闭文件
# start2 = time.time()


print('off')


'''
最近心血来潮，重写了红警地图找树的逻辑!!

现在已经可以成功截取地图覆盖的[Terrain]片段，再去做判断
并且可以避开注释的行，当到了下一个[节点] 时，程序结束！！

不过依然存在一些bug，比如：



'''
