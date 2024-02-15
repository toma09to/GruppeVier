import data

hoge = data.Data()

while True:
    print(hoge.txt())

    if not hoge.isQuestion():
        break
    ans = int(input())

    if ans == 0:
        hoge.yes()
    else:
        hoge.no()
