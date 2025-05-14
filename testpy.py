from pathlib import Path

# 現在のスクリプトと同じ階層のパスを取得
current_dir = Path(__file__).parent

# 読みたいファイルのパスを作成
file_path = current_dir / "c.txt"

# ファイルを読み込む
content = file_path.read_text(encoding="utf-8")





# 各行の先頭の1文字だけ取り出して出力
for line in content.splitlines():
    if line: #空行チェック
        if line[0]=="Y" and line[1]==" ":
            print("Y")
        elif line[0]=="N" and line[1]==" ":
            print("N")
        elif line[0]=="A" and line[1]==" ":
            print("A")
        else:
            print("X")