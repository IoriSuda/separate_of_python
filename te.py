from pathlib import Path






c_number = 1
r_number = 1
identifer = ["Yes", "No", "Abstention", "Non-Vothing"]




###各国をリストごとにもってくる処理###


# 対象のフォルダパス
target_dir = Path(__file__).parent / "sample_output"

# ファイルの一覧を取得（サブフォルダは含まない）
files = [f for f in target_dir.iterdir() if f.is_file()]

#ファイルの数を取得
folder_count = len(files)

total_lines = 0

#フォルダの上から順に出力する
for i in range(folder_count):
    readfile = files[i]
    content = readfile.read_text(encoding="utf-8").rstrip()
    #print(content)
    line_count = len(readfile.read_text(encoding="utf-8").splitlines())
    print(line_count)
    total_lines += line_count
    

    #print("MATCH (c" + str(c_number) + ":Country" + "{" + "name:" + '"' + content + '"' + "})")
print(total_lines)