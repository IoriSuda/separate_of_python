#表記ゆれ
#mapping_dictのループは別で回す? -> 意味ないみたい


mapping_dict = {
    "BOLIVIA" : "BOLIVIA (PLURINATIONAL STATE OF)",
    "CAPE VERDE" : "CABO VERDE",
    "CÔTE D'IVOIRE" : "COTE D'IVOIRE",
    "CZECH REPUBLIC" : "CZECHIA",
    "LIBYAN ARAB JAMAHIRIYA" : "LIBYA",
    "NETHERLANDS" : "NETHERLANDS (KINGDOM OF THE)",
    "SWAZILAND" : "ESWATINI",
    "THE FORMER YUGOSLAV REPUBLIC OF MACEDONIA" : "NORTH MACEDONIA",
    "TURKEY" : "TÜRKÝYE",
    "VENEZUELA" : "VENEZUELA (BOLIVARIAN REPUBLIC OF)"
}






#かつて存在したlist_bにのみ存在する国リスト
only_b_list = [
    "YUGOSLAVIA"
]


file_a = open('a.txt', 'r', encoding='UTF-8')
file_b = open('b.txt', 'r', encoding='UTF-8')

a_list = [line.strip() for line in file_a.readlines()]
b_list = [line.strip() for line in file_b.readlines()]




#print(len(b_list)) -> 少ない方の国名リスト

#表記ゆれの確認

def spelling_discrepancies():
    
    for i in range(len(b_list)):
        
        for key_dict in mapping_dict.keys():
            
            if (key_dict == b_list[i]):
                print(i)
                get_b = b_list[i]
                print("FIND DIFFERENT key_dict:" + str(mapping_dict[key_dict]) +  "  b_list:" + str(get_b))
            # else:
            #    print("DON'T FIND DIFFERENT  key_dict:"  + str(key_dict) + "  b_list:" + str(b_list[i]))    


spelling_discrepancies()
#国名リストの比較。一致しないものがあったときに色々処理をする部分
'''
only_a_list = []
count_a = count_b = 0
for i in range(len(b_list)):
    
    if a_list[count_a] != b_list[count_b]:
        print("FIND DIFFERENT")
        print("a_list:" + str(a_list[count_a]) + "  b_list:" + str(b_list[count_b]))
        only_a_list.append(a_list[count_a])
        substract = i
        for l in range(len(a_list) - substract):
            if a_list[l] == b_list[count_b]:
                count_a = l
                print("count_a: " + str(count_a))
                print("count_b: " + str(count_b))
                continue
            else:
                only_b_list.append(b_list[count_b])     
                count_a += 1
                print("count_a: " + str(count_a))
                print("count_b: " + str(count_b))
        
        
        
        
    else:
        print("DON'T FIND DIFFERENT  a_list:" + str(a_list[i]) + "  b_list:" + str(b_list[i]))
        count_a += 1
        count_b += 1


for i in range(len(only_a_list)):
    print("only_b_list  " + str(i) + ":" + str(only_a_list[i]))

for i in range(len(only_b_list)):
    print("only_b_list  " + str(i) + ":" + str(only_b_list[i]))

'''