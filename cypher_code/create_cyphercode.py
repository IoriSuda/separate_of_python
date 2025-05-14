from pathlib import Path



###各国をリストごとにもってくる処理###

def getCountryList():
    # 持ってくる対象のフォルダパス
    target_dir = Path(__file__).parent / "sample_output"

    # ファイルの一覧を取得（サブフォルダは含まない）
    files = [f for f in target_dir.iterdir() if f.is_file()]

    #ファイルの数を取得 -> 4
    folder_count = len(files)

    #各リストの行数をカウントするカウンター -> 193
    total_lines = 0

    #各国の名前をリストに格納して、出力する
    country = []


    #フォルダの上から順に出力する
    for i in range(folder_count):

        #指定したフォルダに格納されているファイルを読み込み、パスを取得する処理
        readfile = files[i]


        #国名出力
        content = readfile.read_text(encoding="utf-8").rstrip()



        #ファイルの行数をカウント、出力する処理    
        line_count = len(readfile.read_text(encoding="utf-8").splitlines())
        total_lines += line_count

        #取得したcountryをリスト化する
        country_lines = content.split("\n")
        country.extend(country_lines)


    return country, total_lines    




def CypherCode_MATCH(country, total_lines):
    c_number = 1
    for i in range(total_lines):
        print("MATCH (c"+ str(c_number) + ":Country" + "{" + "name:" + '"' + country[i] + '"' + "})")
        c_number += 1







