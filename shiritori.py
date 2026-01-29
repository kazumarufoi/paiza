# 難しすぎるので一回断念（20260129）
#しりとり

num_person, num_words, num_round = map(int, input().split(" "))

flag_dead = [1]*num_person
people = [i for i in range(num_person)]

words = []

for i in range(num_words):
    words.append(input())

# チェック用
def check_connect(a, b):
    if (a == -1):
        return False
    elif talks[a][-1] != talks[b][0]:
        return True
    else:
        return False
    
def check_end(word):
    if word[-1] == "z":
        return True
    else:
        return False

# ゲーム開始
restart = False
talks = []
for i in range(num_round):
    talks.append(input())

for i in range(num_round):
    if talks[i] not in words:
        people[i%num_person] = 0
        restart = True
    elif (check_end(talks[i])):
        people[i%num_person] = 0
        restart = True
        words.remove(talks[i])
    elif (restart == False):
        if (check_connect(i-1, i)):
            people[i%num_person] = 0
            restart = True
            words.remove(talks[i])
        else:
            restart = False
            words.remove(talks[i])
    else:
        restart = False
        words.remove(talks[i])

print(people.count(1))
for i in range(len(people)):
    if (people[i] == 1):
        print(i+1)



        



# ゲームの流れ
# wordsから単語を選ぶ　→　単語が無い場合、プレイヤー削除　→　次のプレイヤーへ
# ↓
# 選んだ単語をリストから削除
# ↓
# チェック
# ・ｚで終わってないか　→　だめならプレイヤー削除
# ↓
# 一人前の失敗フラグを見る　→　フラグありならチェックスルー
# ↓
# ・前と繋がっているか　→　だめならプレイヤー削除
# ↓
# 次のプレイヤーへ

# ラウンド数が達したらゲーム終了
# 残っている人の数と番号出力




# 3人 6単語 7回

#単語
# a
# aloha
# app
# az 
# paiza 
# warp

# 結果
# app 1
# paiza 2
# a 3 
# aloha 1
# az 2 @
# warp 3
# paiza 1 @

# 4人、4単語、4回
# 単語
# abacus
# banana
# candy
# yankee

# 結果
# banana 0
# candies 1 @
# candies 2 @
# yankee 3
# candy 0
# abucus 3

# 5 5 5
# jaa 
# rqgipn
# yxdkcd
# diwnwwgzj
# jwduez

# rqgipn 1
# rqgipn 2 @
# yxdkcd 3
# diwnwwgzj 4
# jwduez 5 @

