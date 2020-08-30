with open('a.txt', 'w') as f:
    print('文字列を画面ではなく、ファイルに書き込む例', file=f)

with open('b.txt', 'w') as f:
    for i in range(10):
        print('文字列を画面ではなく、ファイルに書き込む例', file=f)

f = open('c.txt','w')
print('文字列を画面に出力する例')
print('文字列を画面ではなく、c.txtファイルに書き込む例', file=f)
f.close()

print('ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー')
with open('a.txt', 'r') as f:
    s=f.readlines()
    print(s)

print('ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー')
with open('b.txt', 'r') as f:
    s=f.readlines()
    print(s)

print('ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー')
with open('c.txt', 'r') as f:
    s=f.readlines()
    print(s)
print('ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー')


a=input()
