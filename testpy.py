text = """

Y 
A 
Y 
A 
Y 
Y 
A 
Y 
Y 

Y 
A 
A 
Y 
N 
Y 
Y 
Y 
A 
A 
Y 
Y 
A 
A 
Y 

N 
Y 
A 

Y 
A 

Y 
A 
A 
Y 
A 
Y 
Y 
Y 
N 
Y 
Y 
N 
Y 
Y 


Y 
Y 
A 
A 
A 
N 
Y 

A 
Y 
Y 
Y 
A 
Y 
Y 
Y 
Y 
Y 

Y 
A 
A 
Y 
A 

Y 
Y 
A 
A 
A 
A 
Y 
Y 
Y 
Y 
Y 
A 
A 
Y 

A 
A 
A 
Y 
A 


A 
Y 
Y 
Y 
A 
Y 
A 
Y 
N 
Y 
Y 
A 
Y 
A 
Y 
Y 
A 
Y 

A 
Y 
A 

A 
Y 
Y 
N 

A 
Y 
Y 
A 
A 
Y 
Y 
Y 
Y 
Y 
Y 
Y 
Y 
Y 
Y 
Y 
Y 
N 

Y 


Y 
Y 
Y 
A 
A 
Y 
Y 
Y 
Y 
Y 
Y 


A 

Y 
A 
A 
Y 
Y 
Y 
N 
A 
A 
Y 
A 
Y 
Y 
A 


Y 
A 
Y 
A 
Y 
A 
Y 
Y 
A 
Y 

A 
A 
Y 
A 
"""

# 各行の先頭の1文字だけ取り出して出力
for line in text.splitlines():
    if line: #空行チェック
        if line[0]=="Y" and line[1]==" ":
            print("Y")
        elif line[0]=="N" and line[1]==" ":
            print("N")
        elif line[0]=="A" and line[1]==" ":
            print("A")
        else:
            print("X")