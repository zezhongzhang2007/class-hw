import random
import pandas as pd


class Person:
    high = []
    weigh = []
    rankhigh = pd.DataFrame(columns=["Height", "Name"])
    rankweigh = pd.DataFrame(columns=["Weight", "Name"])

    def __init__(self, name):
        self.weightint = random.randint(20, 200)
        self.heightint = random.randint(100, 210)
        self.name = name
        Person.high.append([self.heightint, name])
        Person.weigh.append([self.weightint, name])

    def rank_high(self):
        rank_num = 1
        for i in Person.high:
            for e in Person.high:
                if i > e:
                    rank_num += 1
            Person.rankhigh.loc[rank_num, "Height"] = i[0]
            Person.rankhigh.loc[rank_num, "Name"] = i[1]

            rank_num = 1
        sorted_df = Person.rankhigh.sort_index()
        return sorted_df

    def rank_weight(self):
        rank_num = 1
        for i in Person.weigh:
            for e in Person.weigh:
                if i > e:
                    rank_num += 1
            Person.rankweigh.loc[rank_num, "Weight"] = i[0]
            Person.rankweigh.loc[rank_num, "Name"] = i[1]

            rank_num = 1
        sorted_df = Person.rankweigh.sort_index()
        return sorted_df

    def weigh_averg(self):
        lil_list = []
        for i in Person.weigh:
            lil_list.append(i[0])
        return sum(lil_list) / len(lil_list)


    def height_averg(self):
        lil_list = []
        for i in Person.high:
            lil_list.append(i[0])
        return sum(lil_list) / len(lil_list)


    def weight_diff(self):
        lil_list = []
        result_lis = []
        for i in Person.weigh:
            lil_list.append(i[0])
        miu = sum(lil_list) / len(lil_list)
        for i in lil_list:
            result = pow(i - miu,2)
            result_lis.append(result)
        stand_diff = pow((sum(result_lis)/len(lil_list)),0.5)
        return stand_diff



zhangsan = Person("zhangsan")
lisi = Person("lisi")
wdnmd = Person("wdnmd")
nmsl = Person("nmsl")
print(nmsl.rank_high())
print(nmsl.rank_weight())
print("Height average:", nmsl.height_averg())
print("Weight average:", nmsl.weigh_averg())
print("标准差：",nmsl.weight_diff())
