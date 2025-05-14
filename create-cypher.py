# matchとcreate文を作りたい
# MATCH (cn:Country{name:""})->193回
# MATCH (rn:Relation{Relation:"", Identifer:""})->4回
# CREATE (c)-[YNANv]-(r) を各国 -> 193回
# 各国の名前は各リストから拾ってこよう

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


#フォルダの上から順に出力する
for i in range(folder_count):
    readfile = files[i]
    content = readfile.read_text(encoding="utf-8").rstrip()
    print(content)
    print("MATCH (c" str(c_number) + ":Country" + "{" + "name:" + '"' + content '"' + "})")






print("\nサブフォルダの数:", folder_count)












print("MATCH (c{c_number}:Country" + "{" + "name:" + '"' + "{country}" '"' + "})")

print("MATCH (r{r_number}:Resolution)" + "{" + "Resolution:" + "{Resolution}" + ", " + "Identifer:" + identifer)


print("CREATE (c)-[]->()")




