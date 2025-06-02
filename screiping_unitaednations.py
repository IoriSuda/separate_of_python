import requests
from bs4 import BeautifulSoup

# スクレイピング対象のURL
url = 'https://example.com'

# 1. requestsでHTMLを取得
response = requests.get(url)

# ステータスコードを確認（200は成功）
if response.status_code == 200:

    # HTMLのパース
    soup = BeautifulSoup(response.text, 'html.parser')

    # タイトルを取得
    value_elements = soup.find_all('span', class_="value")


    # 2. BeautifulSoupでHTMLを解析
    soup = BeautifulSoup(html, 'html.parser')

    # 3. 必要な要素を抽出（例：h1タグの中身を取得）
    span_tags1 = soup.find_all('title')
    #span_tags2 = soup.find_all('value')
    for tag in span_tags1:
        print(tag.text)
        #print(tag.text)
else:
    print(f"取得失敗: ステータスコード {response.status_code}")
