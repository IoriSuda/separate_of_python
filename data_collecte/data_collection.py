import os


#Yesを配列に保管。後にまとめて出力
y_list = []
def Y_ans(y_data):
    y_list.append(y_data)
    return y_list




#Noを配列に保管。後にまとめて出力
n_list = []
def N_ans(n_data):
    n_list.append(n_data)
    return n_list




#Abstentionを配列に保管。後にまとめて出力
a_list = []
def A_ans(a_data):
    a_list.append(a_data)
    return a_list





#Non_Votingを配列に保管。後にまとめて出力
non_list = []
def non_vote(non_data):
    non_list.append(non_data)
    return non_list



#分別する処理
def separate():
    with open('sample.txt', 'r') as f:
        lines = f.read().splitlines()
        for x in range(len(lines)):

            #変数iに読み込んだ文字列をそのまま入れて、条件分岐にかける
            i = lines[x]

            #読み込んだ文字列の先頭が'Y'、'N'、'A'いずれかで、且つ、二文字目が空白だった場合
            if i[0] == 'Y' and i[1] == ' ' :
                i = i[2:]
                Y_ans(i)
            elif i[0] == 'N' and i[1] == ' ':
                i = i[2:]
                N_ans(i)
            elif i[0] == 'A' and i[1] == ' ' :
                i = i[2:]
                A_ans(i)

            #読み込んだ文字列の先頭がY'、'N'、'A'いずれかではない、もしくは、二文字目が空白でない場合(国名のみ場合は無投票)
            else:
                non_vote(i)
            x += 1


#分別したものを各ファイルに出力する
def output():
    filename = ['y_list', 'n_list', 'a_list', 'non_vote_list']
    l = [y_list, n_list, a_list, non_list]
    l_index = 0

    #lの長さ分だけループする
    for i in range(len(l[l_index])):
        if i < len(l):

            #各listの中身を出力する処理
            os.makedirs('sample_output', exist_ok=True)
            with open(os.path.join('sample_output', str(filename[i]) + '.txt'), 'w') as f:
                for j in l[l_index]:
                    f.write(j + '\n')
            
            l_index += 1
        else:
            break