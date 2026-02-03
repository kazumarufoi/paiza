n, k, m = map(int, input().split()) # 人数, 単語数, ラウンド数
ikiteru = [1] * n # 生きている人のリスト
data = set() # 使用可能な単語の集合
jun = 0 # プレイヤーを指すインデックス
data2 = set() # 使用済みの単語の集合
flag = False # 直前の発言が有効かどうか
old_s = " " # 直前の発言

# 単語リストの作成
for i in range(k):
    data.add(input())

# 4人、4単語、4回
# 単語
# abacus
# banana
# candy
# yankee

# 結果
# banana 0 @
# candies 1 @
# candies 2 @
# yankee 3

# ゲーム開始
for i in range(m):
    # 次の生きている人を探す@
    while True:
        if ikiteru[jun % n] == 1:
            break
        jun += 1

    new_s = input()

    if new_s in data2:
        ikiteru[jun % n] = 0 # 生きている人リストを更新
        flag = False # 直前の発言を無効にする
        continue

    if new_s[0] != old_s[-1] and flag:
        ikiteru[jun % n] = 0
        flag = False
        continue

    if not (new_s in data):
        ikiteru[jun % n] = 0
        flag = False
        continue

    if new_s[-1] == "z":
        ikiteru[jun % n] = 0
        flag = False
        continue

    data2.add(new_s)
    flag = True
    old_s = new_s
    jun += 1

# 結果出力
print(ikiteru.count(1))

for i in range(n):
    if ikiteru[i] == 1:
        print(i + 1)