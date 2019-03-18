# 要关闭import socket
# # import time
# # import urllib
# #
# # timeout = 20
# # socket.setdefaulttimeout(timeout)#这里对整个socket层设置超时时间。后续文件中如果再使用到socket，不必再设置
# # sleep_download_time = 10
# # time.sleep(sleep_download_time) #这里时间自己设定
# # request = urllib.request.urlopen('http://127.0.0.1/')#这里是要读取内容的url
# # content = request.read()#读取，一般会在这里报异常
# # request.close()#记得
# 5. 写一个自己的max函数，获取指定序列中元素的最大值。如果序列是字典，取字典值的最大值
# # #
# # #     ```python
# # #     例如: 序列:[-7, -12, -1, -9]    结果: -1
# # #          序列:'abcdpzasdz'    结果: 'z'
# # #          序列:{'小明':90, '张三': 76, '路飞':30, '小花': 98}   结果: 98


# def zp_max(*args, **kwargs):
#
#     # print(a)
#
#     # a = 0
#     #     # for i in args[0]:
#     #     #     if args[0][i]>a:
#     #     #         a = args[0][i]
#     #     # print(a)
#
#     a = args[0]
#     if type(a) != 'dict':
#         m = a[0]
#         for i in range(1, len(a)):
#             if a[i] > m:
#                 m = a[i]
#
#     else:
#         for i in a:
#             m = a[i]
#             break
#         for i in range(1, len(a)):
#             if a[i] > m:
#                 m = a[i]
#
#     print(m)
#
# zp_max({'小明':90, '张三': 76, '路飞':30, '小花': 98})