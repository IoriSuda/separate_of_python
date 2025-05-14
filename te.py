# matchとcreate文を作りたい
# MATCH (cn:Country{name:""})->193回
# MATCH (rn:Relation{Relation:"", Identifer:""})->4回
# CREATE (c)-[YNANv]-(r) を各国 -> 193回
# 各国の名前は各リストから拾ってこよう



from pathlib import Path







r_number = 1
identifer = ["Yes", "No", "Abstention", "Non-Vothing"]




###各国をリストごとにもってくる処理###


# 対象のフォルダパス
target_dir = Path(__file__).parent / "sample_output"

# ファイルの一覧を取得（サブフォルダは含まない）
files = [f for f in target_dir.iterdir() if f.is_file()]
#print(files) path名で取得する


#ファイルの数を取得
folder_count = len(files)
print(folder_count)



#各リストの行数をカウントするカウンター
total_lines = 0
country = []
for i in range(folder_count):

    #指定したフォルダに格納されているファイルを読みこみ、パスを出力する処理
    readfile = files[i]
    #print(readfile)


    #国名出力
    content = readfile.read_text(encoding="utf-8").rstrip()
    #print(content)


    #ファイルの行数をカウント、出力する処理    
    line_count = len(readfile.read_text(encoding="utf-8").splitlines())
    total_lines += line_count


    #取得したcountryをリスト化する
    country_lines = content.split("\n")
    country.extend(country_lines)




#cyphercodeを作る#
c_number = 1
for i in range(total_lines):
    print("MATCH (c"+ str(c_number) + ":Country" + "{" + "name:" + '"' + country[i] + '"' + "})")
    c_number += 1










##出力したいcypherのコード##


#print("MATCH (c{c_number}:Country" + "{" + "name:" + '"' + "{country}" '"' + "})")

#print("MATCH (r{r_number}:Resolution)" + "{" + "Resolution:" + "{Resolution}" + ", " + "Identifer:" + identifer)

#print("CREATE (c)-[]->()")
