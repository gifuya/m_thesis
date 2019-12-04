# Python 3.5.2 にて動作を確認
# MySQLdb をインポート
import MySQLdb

# データベース接続とカーソル生成
connection = MySQLdb.connect(
    host='localhost', user='root', passwd='agasahana1', db='cookpad_data', charset='utf8')
cursor = connection.cursor()
 
# エラー処理（例外処理）
try:
    cursor.execute("select * from steps limit 1000")
    print(cursor.fetchall())
 
except MySQLdb.Error as e:
    print('MySQLdb.Error: ', e)
 
# 保存を実行（忘れると保存されないので注意）
connection.commit()

# 接続を閉じる
connection.close()