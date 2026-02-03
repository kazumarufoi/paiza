x, y, z = map(int, input().split(" "))

array = [["."] * y for _ in range(z)]

for i in range(z):
    for j in range(x):
        line = input()
        for k in range(y):
            if line[k] == "#":
                array[i][k] = "#"
    input()
for i in range(len(array) - 1, -1, -1):
    output = "".join(array[i])
    print(output)

### 要復習
# 1. 文字列内の文字のインデックスを調べる方法
# find() メソッド - 見つからない場合は -1 を返す
# index() メソッド - 見つからない場合は ValueError を発生
# 2. 複数の#をすべて見つける方法
# enumerate() を使用したリスト内包表記が最も効率的
# →index, valueの順で取得できる。
# 3. Y*Zの二次元配列を作成
# 4. ループ内での配列の状態追跡
# 各ループで array[i][k] に値を代入していく過程を確認
# 5. ループ変数の上書き問題の修正
# for z in range(z) → for i in range(z) に変更
# 元の変数名と混同しないようにループ変数を別名に変更
# 6. 逆順出力の修正
# range(0, len(array), -1) は空なので range(len(array) - 1, -1, -1) に修正
# 最終的なコードは二次元配列に「#」を記録し、逆順で出力する処理になっています。