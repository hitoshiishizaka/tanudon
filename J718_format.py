#J830
'''
print("私の名前は{}です".format("ごんべい"))
#私の名前はごんべいです

print("今日は{}年{}月{}日{}曜日です".format("2020","7","18","土"))


print("今日は{3:}年{2:}月{1:}日{0:}曜日です".format("土","18","7","2020"))
#今日は2020年7月18日土曜日です

print("{:10.3f}".format(2/3*100))
#____66.667

print("{:*>20s}".format("1234567890"))
#__________1234567890

print("{:,.3f}".format(123456789012345.6789))
#123,456,789,012,345.672

print('{:2}'.format('abcdef'))
print('{:.2}'.format('abcdef'))
print('{:>10}'.format('abcdef'))
print('{:^10}'.format('abcdef'))
print('{:<10}'.format('abcdef'))

print('{:*<10}'.format('abcdef'))
print('{:05d}'.format(100))
'''

print("{:+08.3f}".format(2/3*100))
#+066.667

print("{:+08.3f}".format(-2/3*100))
#-066.667


a=input()


