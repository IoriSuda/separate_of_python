import requests
from bs4 import BeautifulSoup
import re

# 対象のURL
url = 'https://digitallibrary.un.org/record/3959039?ln=en'

# HTTPリクエストを送信
response = requests.get(url)

# ステータスコードをチェック
if response.status_code == 200:
    # HTMLのパース
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # タイトルを取得
    value_elements = soup.find_all('span', class_="value")


    for i, elem in enumerate(value_elements, start=1):
        if i != 7:
            #print(f"{i}番目のvalue要素:")
            print(elem.text.strip())  # テキストだけを表示（空白削除）
            #print('-' * 40)
        else:
            text = elem.text.strip()
            number_ynanv = re.findall(r'\d+', text)
            for num in number_ynanv:
                print(num)



    #print(f'ページのタイトル: {content_div}')
else:
    print(f'ページの取得に失敗しました (ステータスコード: {response.status_code})')
