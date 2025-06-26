import unicodedata

def normalize(s):
    return unicodedata.normalize('NFKC', s.strip())




#表記ゆれ
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

print(len(b_list))
#2-1から条件分岐かけていく？

count_a = count_b = roop_counter = 0



# ...

while roop_counter < len(b_list):
    print(roop_counter)
    a_item = normalize(a_list[roop_counter])
    b_item = normalize(b_list[roop_counter])
    print(repr(a_item))
    print(repr(b_item))

    for dict_key in mapping_dict.keys():
        key = normalize(dict_key)
        print(repr(key))
        if a_item == key or b_item == key:
            print("一致！")
            break

    roop_counter += 1


'''

listは0から始まるので、whileで回すときは、(行数-1)回ループするようにする

#表記ゆれの国かどうか一行ずつ確認する。表記ゆれでない場合、次の処理に進む。
while roop_counter < len(b_list):
    
    for map_keys in mapping_dict.keys():
        #表記ゆれの国なら...
        if (a_list[count_a] == map_keys) or (b_list[count_b] == map_keys):
            print(a_list[count_a])
            print(b_list[count_b])
            print(map_keys)
            count_a += 1
            count_b += 1
            roop_counter += 1
            
        else:
            count_a += 1
            count_b += 1
            roop_counter += 1


'''


