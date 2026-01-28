#円卓の席取り問題
# ポイント
# 1. 着席フラグをリストで管理する
# 2. 円卓のため、座席番号が最後まで行ったら最初に戻る必要がある
# →%演算子を使う
# 席番号は1から始めずに、0から始めると％で扱いやすい

input_1, input_2 = input().split(" ")
num_chair = int(input_1) 
num_group = int(input_2) 
print(f"席数は{num_chair}, グループ数は{num_group}")

#受け取った座席数で、着席フラグを保持するリストを作る
#flag_is_person = [i*0 for i in range(num_chair)]

flag_is_person = {i+1:0 for i in range(num_chair)}

for i in range(num_group):
    input_1, input_2 = input().split(" ")
    num_person = int(input_1)
    start = int(input_2)
    print(f"来店の人数は{num_person}, 一人目の席番号は{start}")
    
    for j in range(num_person):
        check = ((start+j-1)%num_chair)+1
        if flag_is_person[check] == 1: #リストの位置とは１つずれることに注意
            break
    else: #正常終了した場合に以下の処理が走る
        for p in range(num_person):
            sitting = ((start+p-1)%num_chair)+1
            flag_is_person[sitting] = 1
    print(f"着席した席番号は{list(flag_is_person.values())}")

print(list(flag_is_person.values()).count(1))

#####円卓を直列で表現しようとして失敗したコード

input_1, input_2 = input().split(" ")
num_chair = int(input_1) ##6
num_group = int(input_2) ##3

#受け取った座席数で、着席フラグを保持するリストを作る
#flag_is_person = [i*0 for i in range(num_chair)]

flag_is_person = [0]*num_chair*2


for i in range(num_group):
    input_1, input_2 = input().split(" ")
    num_person = int(input_1)
    start = int(input_2)
    
    for j in range(num_person):
        if flag_is_person[start-1+j] == 1: #リストの位置とは１つずれることに注意
            break
    else: #正常終了した場合に以下の処理が走る
        for p in range(num_person):
            sitting = start-1+p
            flag_is_person[sitting] = 1
            flag_is_person[sitting+num_chair] = 1
    print(flag_is_person)

#debug
print(f"席数は{num_chair}, グループ数は{num_group}")
print(f"来店の人数は{num_person}, 一人目の席番号は{start}")

print(flag_is_person[:num_chair].count(1))

#####模範解答コード#####
n, m = map(int, input().split())
print(f"席数は{n}, グループ数は{m}")

vacant = [True] * n
for _ in range(m):
    a, b = map(int, input().split())
    print(f"来店の人数は{a}, 一人目の席番号は{b}")

    can_sit = True
    for i in range(b, b + a):
        if not vacant[i % n]:
            can_sit = False
            break

    if not can_sit:
        continue

    for i in range(b, b + a):
        vacant[i % n] = False

ans = 0
for v in vacant:
    if not v:
        ans += 1

print(ans)