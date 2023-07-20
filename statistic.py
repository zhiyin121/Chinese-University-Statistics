import pandas as pd

file_2023_china_uni = "China_uni_2023.xlsx"
file_top_uni = "top_uni.xlsx"

df_2023_china_uni = pd.read_excel(io=file_2023_china_uni) 
df_top_uni = pd.read_excel(io=file_top_uni) 

code_to_origin = {}
for i in range(len(df_2023_china_uni)):
    code = str(df_2023_china_uni.loc[i].loc["学校代码"])
    city = df_2023_china_uni.loc[i].loc["所属城市"]
    province = df_2023_china_uni.loc[i].loc["省/直辖市"]
    code_to_origin[code] = {"city":city, "province":province}

code_to_level = {}
for i in range(len(df_top_uni)):
    code = str(df_top_uni.loc[i].loc["学校代码"])
    nine_eight_five = df_top_uni.loc[i].loc["985"]
    two_one_one = df_top_uni.loc[i].loc["211"]
    top_uni = df_top_uni.loc[i].loc["一流学校"]
    top_subject = df_top_uni.loc[i].loc["一流专业"]
    code_to_level[code] = {"985":nine_eight_five, "211":two_one_one, "一流学校": top_uni, "一流专业":top_subject}


def combine(df_dataframe, code_to_origin, code_to_level, save_filename):
    for i in range(len(df_dataframe)):
        code = str(df_dataframe.loc[i, "院校代码"])
        if code in code_to_origin:
            df_dataframe.loc[i,"所属城市"] = code_to_origin[code]["city"]
            df_dataframe.loc[i,"省/直辖市"] = code_to_origin[code]["province"]
        else:
            df_dataframe.loc[i,"所属城市"] = "NaN"
            df_dataframe.loc[i,"省/直辖市"] = "NaN"
        if code in code_to_level:
            df_dataframe.loc[i,"985"] = code_to_level[code]["985"]
            df_dataframe.loc[i,"211"] = code_to_level[code]["211"]
            df_dataframe.loc[i,"一流学校"] = code_to_level[code]["一流学校"]
            df_dataframe.loc[i,"一流专业"] = code_to_level[code]["一流专业"]
        else:
            df_dataframe.loc[i,"985"] = "NaN"
            df_dataframe.loc[i,"211"] = "NaN"
            df_dataframe.loc[i,"一流学校"] = "NaN"
            df_dataframe.loc[i,"一流专业"] = "NaN"

    print(df_dataframe)
    df_dataframe.to_excel(save_filename) 

if __name__ == "__main__":
    file_2023_physics = "./广东省2023年本科批次投档情况/广东省2023年本科普通类（物理）投档情况.xlsx"
    file_2022_physics = "./广东省2022年本科批次投档情况/广东省2022年本科普通类（物理）投档情况.xlsx"
    
    file_2023_history = "./广东省2023年本科批次投档情况/广东省2023年本科普通类（历史）投档情况.xlsx"
    file_2022_history = "./广东省2022年本科批次投档情况/广东省2022年本科普通类（历史）投档情况.xlsx"
    
    file_2023_painting = "./广东省2023年本科批次投档情况/广东省2023年本科美术类统考投档情况.xlsx"
    file_2022_painting = "./广东省2022年本科批次投档情况/广东省2022年本科美术类统考投档情况.xlsx"

    file_2022_physics_zhuanke = "广东省2022年专科普通类（物理）投档情况.xlsx"


    file_name = file_2022_physics_zhuanke
    df_dataframe = df_top_uni = pd.read_excel(io=file_name)

    save_filename = "2022_专科物理.xlsx"
    combine(df_dataframe, code_to_origin, code_to_level, save_filename)