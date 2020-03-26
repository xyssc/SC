#coding:utf-8
'''
if判断：通过条件的来确定是否需要执行子代码块，
        当条件为True或非空字符则执行子代码块，
        当条件为False、0、空数据时，则不执行子代码块
        流程控制语句必须拥有子代码块（if,for,while，else）
if 条件：
    子代码块
elif:
    子代码块
else：当if的条件不成立时，则执行else内的子代码块
input()函数：输入函数:捕获键盘输入的值,输出的值为字符串格式，可以通过数据类型的转化运用于数据比较
'''
# num = float(input('请输入数字'))
# if num>1:
#     print('数字大于1')
# elif num<0:   #num<=1
#     print('数字小于1')
# elif num == 5:
#     print('数字为5')
# else: #0< num <= 1
#     print('数字等于1')
# 例题1：
# 需求根据用户输入的成绩分档，要求如下：
# 1. 如果成绩大于等于60分，输出“及格”
# 2. 如果成绩大于等于70分，输出“良”
# 3. 如果成绩大于等于80分，输出“好”
# 4. 如果成绩大于等于90分，输出“优秀”
# 5. 否则输出“你要努力了”
# score = float(input('请输入分数：'))
# if score>100 or score<0:
#     print('请输入正确的分数（0--100）')
# elif score >=90:      #分数的范围0<=score<=100
#     print('优秀')
# elif score >=80:       #0<=score<90
#     print('好')
# elif score >=70:       #0<=score<80
#     print('良')
# elif score >=60:       #0<=score<70
#     print('及格')
# else:       #0<=score<60
#     print('你要努力了')
# day = int(input('输入数字日期：'))
# if day>7 or day<1:
#     print('请输入正确的数字')
# elif day >= 6:
#     print('周末')
# else:
#     print('工作日')
'''
if 判断的嵌套
if 条件：
    if 条件：
        子代码块
    else:
        子代码块
elif 条件：
    if 条件：
        子代码块
else:
    if 条件：
        子代码块
'''
# 例题2：
# 判断登录功能。默认验证码为：1111
# 用户名为：admin
# 密码为：admin123
# 当账号 密码 验证码同时正确 则登录成功
# 账号错误 输出 账号错误
# 账号正确 密码错误 则输出密码错误
# 账号密码正确 验证码错误 则输出验证码错误
# account = input('请输入账号：')
# password = input('请输入密码：')
# yzm = input('请输入验证码:')
# if account == 'admin':
#     if password == 'admin123':
#         if yzm == '1111':
#             print('登录成功')
#         elif yzm == '':
#             print('验证码不能为空')
#         else:
#             print('验证码错误')
#     else:
#         print('密码错误')
# else:
#     print('账号错误')
# print('现在时间为白天')
# print('时间段为上午')

time = int(input('请输入时间'))
if time>24 or time<0:
    print('请输入正确的时间')
elif 8<=time<=18:
    print('现在时间为白天')
    if time<=12:
        print('时间段为上午')
    elif time<=14:
        print('时间段为中午')
    else:
        print('时间段为下午')
else: #0-7 19-24
    print('现在时间为晚上')
    if time<=7 or time == 24:
        print('时间段为半夜')
    else:
        print('时间段为夜晚')哒哒哒哒哒哒多多多多多多多多多多多多多多多多多多多
