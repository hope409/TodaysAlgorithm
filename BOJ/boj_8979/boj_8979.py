'''
4 3
1 1 2 0
2 0 1 0
3 0 1 0
4 0 0 1
'''
# 2

'''
4 2
1 3 0 0
3 0 0 2
4 0 2 0
2 0 2 0
'''
# 2

n, rank = map(int, input().split()) # 국가의 수, 원하는 나라
country_li = [0] * n
for x in range(n):
    country, gold, silver, cooper = map(int, input().split())
    if country == rank:
        idx = country
    country_info = {
        'country_num' : country,
        'gold' : gold,
        'silver' : silver,
        'cooper' : cooper,
    }
    country_li[x] = country_info

sort_country_li = sorted(country_li, key= lambda x : (-x['gold'], -x['silver'], -x['cooper']))

pre_rank = 1
pre_info = [-1, -1, -1]
k_rank = 0
for idx, country in enumerate(sort_country_li):
    num, *medal = country.values()
    if medal != pre_info:
        pre_rank = idx + 1

    if num == rank:
        k_rank = pre_rank
        break
    pre_info = medal

print(k_rank)

# n, country_num = map(int, input().split())
# country_medal = [0] * n
# for i in range(n):
#     cn, *country_medal[i] = list(map(int, input().split()))
#     if cn == country_num:
#         gold, silver, cooper = country_medal[i]
# rank = 1
# count = 0
# for medal_info in country_medal:
#     if medal_info[0] > gold:
#         count += 1
#     elif medal_info[0] == gold:
#         if medal_info[1] > silver:
#             count += 1
#         elif medal_info[1] == silver:
#             if medal_info[2] > cooper:
#                 count += 1
# print(rank + count)