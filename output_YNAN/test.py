def load_list(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

def compare_country_lists(a_list, b_list, mapping_dict):
    i, j = 0, 0
    difflist_a_only = []
    difflist_b_only = []

    while i < len(a_list) and j < len(b_list):
        a_country = a_list[i]
        b_country = b_list[j]

        # 2-2: 名前が違うが、同じ国
        if (a_country == b_country) or (mapping_dict.get(a_country) == b_country or mapping_dict.get(b_country) == a_country):
            i += 1
            j += 1

        # 2-1: aにしかない
        elif b_country not in a_list[i:]:
            difflist_a_only.append(a_country)
            i += 1

        # 2-3: bにしかない（独立前の国など）
        elif a_country not in b_list[j:]:
            difflist_b_only.append(b_country)
            j += 1

        # 不一致：aだけ先に進めて様子を見る（2-1の可能性高い）
        else:
            difflist_a_only.append(a_country)
            i += 1

    # aが残っていたら aにしかない
    while i < len(a_list):
        difflist_a_only.append(a_list[i])
        i += 1

    # bが残っていたら bにしかない
    while j < len(b_list):
        difflist_b_only.append(b_list[j])
        j += 1

    return difflist_a_only, difflist_b_only


a_list = load_list('a.txt')
b_list = load_list('b.txt')

# 表記ゆれの対応辞書（必要に応じて追加）
mapping_dict = {
    'CZECHIA': 'CZECH REPUBLIC',
    'CABO VERDE': 'CAPE VERDE',
    'NORTH MACEDONIA': 'THE FORMER YUGOSLAV REPUBLIC OF MACEDONIA',
    'ESWATINI': 'SWAZILAND',
    'MYANMAR': 'BURMA',
}

a_only, b_only = compare_country_lists(a_list, b_list, mapping_dict)

print("aにしかない国:")
for c in a_only:
    print("  ", c)

print("\nbにしかない国:")
for c in b_only:
    print("  ", c)
