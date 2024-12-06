# -*- coding: utf-8 -*-
"""じゃん拳
"""

# 次の行で random モジュールをインポートします。
import random
# count_rock、count_paper、count_scissors 変数を作成し、それらの初期値を 0 に設定します。
count_rock = 0
count_paper = 0
count_scissors = 0

# update_counts() 関数を作成します。
def update_counts(user_input):
  global count_rock, count_paper, count_scissors
  if user_input == 0:
    count_rock = count_rock + 1
  elif user_input == 1:
    count_paper = count_paper + 1
  elif user_input == 2:
    count_scissors = count_scissors + 1
  else:
    print("0(グー), 1(パー), または 2(チョキ)を入力してください。.")

# predict() 関数を作成します。
def predict():
  if count_rock > count_paper and count_rock > count_scissors:
    pred = 0
  elif count_paper > count_rock and count_paper > count_scissors:
    pred = 1
  elif count_scissors > count_rock and count_scissors > count_paper:
    pred = 2
  else:
    pred = random.randint(0, 2)
  return pred

# player_score と comp_score 変数を作成します。
player_score = 0
comp_score = 0

# update_scores() 関数を作成します。
def update_scores(user_input):
  global player_score, comp_score
  # グーはチョキに勝ち、チョキはパーに勝ち、パーはグーに勝ちます。
  pred = predict()

  # ケース 1, 2, 3 のコード
  if user_input == 0:
    if pred == 0:
      print("\nあなたはグー、コンピュータはグーを出しました。")
      print("\nコンピュータのスコア: ", comp_score, "\nあなたのスコア: ", player_score)
    elif pred == 1:
      print("\nあなたはグー、コンピュータはパーを出しました。")
      comp_score += 1
      print("\nコンピュータのスコア: ", comp_score, "\nあなたのスコア: ", player_score)
    else:
      print("\nあなたはグー、コンピュータはチョキを出しました。")
      player_score += 1
      print("\nコンピュータのスコア: ", comp_score, "\nあなたのスコア: ", player_score)

  # ケース 4, 5, 6 のコード
  elif user_input == 1:
    if pred == 1:
      print("\nあなたはパー、コンピュータはパーを出しました。")
      print("\nコンピュータのスコア: ", comp_score, "\nあなたのスコア: ", player_score)
    elif pred == 0:
      print("\nあなたはパー、コンピュータはグーを出しました。")
      player_score += 1
      print("\nコンピュータのスコア: ", comp_score, "\nあなたのスコア: ", player_score)
    else:
      print("\nあなたはパー、コンピュータはチョキを出しました。")
      comp_score += 1
      print("\nコンピュータのスコア: ", comp_score, "\nあなたのスコア: ", player_score)

  else:
    # ケース 7, 8, 9 をカバーするための else 文のコード
    if pred == 2:
      print("\nあなたはチョキ、コンピュータはチョキを出しました。")
      print("\nコンピュータのスコア: ", comp_score, "\nあなたのスコア: ", player_score)
    elif pred == 0:
      print("\nあなたはチョキ、コンピュータはグーを出しました。")
      comp_score += 1
      print("\nコンピュータのスコア: ", comp_score, "\nあなたのスコア: ", player_score)
    else:
      print("\nあなたはチョキ、コンピュータはパーを出しました。")
      player_score += 1
      print("\nコンピュータのスコア: ", comp_score, "\nあなたのスコア: ", player_score)

# 1. リスト ['0', '1', '2'] を作成し、valid_entries という変数に格納します。例: valid_entries = ['0', '1', '2']
valid_entries = ['0', '1', '2']

# 2. 無限ループを作成します。このループの中で、user_input という変数を作成し、プレイヤーの入力を格納します。
while True:
  # 3. input() 関数を使用してプレイヤーから入力を取得します。
  # input() 関数内に「グーは0、パーは1、チョキは2を入力してください:」という文を記述して、プレイヤーに表示します。
  user_input = input("グーは0、パーは1、チョキは2を入力してください: ")
  # 4. 内部ループを作成して、プレイヤーが提供した入力が valid_entries リストに存在するかを確認します。
  while user_input not in valid_entries:
    # 5. プレイヤーが提供した入力が valid_entries リストに存在しない場合、「無効な入力です！」というメッセージを表示します。
    # 次の行で、user_input = input("グーは0、パーは1、チョキは2を入力してください: ") 文を再記述します。
    print("\n無効な入力です！")
    user_input = input("グーは0、パーは1、チョキは2を入力してください: ")

  # 6. 内部ループの外で、int() 関数を使用して user_input の値を整数値に変換します。
  user_input = int(user_input)
  # 7. update_scores() 関数を user_input を引数として呼び出し、プレイヤーとコンピュータのスコアを更新します。
  update_scores(user_input)
  # 8. update_counts() 関数を user_input を引数として呼び出し、プレイヤーの入力をカウントします。
  update_counts(user_input)

  # 9. if 文を記述して、どちらかのスコアが 10 に達したかを確認します。
  if player_score == 10:
    print("おめでとうございます、あなたの勝ちです！")
    break
  elif comp_score == 10:
    print("コンピュータが勝ちました！")
    break
  # comp_score == 10 の場合、「コンピュータが勝ちました！」というメッセージを表示してループを終了します。
 # player_score == 10 の場合、「おめでとうございます、あなたの勝ちです！」というメッセージを表示してループを終了します。

