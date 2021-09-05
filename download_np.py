import urllib.request
import json
from bs4 import BeautifulSoup

url_list = [
             "https://npb.jp/bis/2021/calendar/index_04.html",
             "https://npb.jp/bis/2021/calendar/index_05.html",
             "https://npb.jp/bis/2021/calendar/index_06.html",
             "https://npb.jp/bis/2021/calendar/index_07.html",
             "https://npb.jp/bis/2021/calendar/index_08.html",
             "https://npb.jp/bis/2021/calendar/index_09.html",
             "https://npb.jp/bis/2021/calendar/index_10.html"]

yotei_url_list = [
             "https://npb.jp/bis/2021/calendar/index_09.html",
             "https://npb.jp/bis/2021/calendar/index_10.html"]
data = []

result_team = {"ヤ":{"win":0,"lost":0,"even":0}
             ,"デ":{"win":0,"lost":0,"even":0}
             ,"巨":{"win":0,"lost":0,"even":0}
             ,"中":{"win":0,"lost":0,"even":0}
             ,"広":{"win":0,"lost":0,"even":0}
             ,"神":{"win":0,"lost":0,"even":0}
             ,"ロ":{"win":0,"lost":0,"even":0}
             ,"楽":{"win":0,"lost":0,"even":0}
             ,"日":{"win":0,"lost":0,"even":0}
             ,"西":{"win":0,"lost":0,"even":0}
             ,"オ":{"win":0,"lost":0,"even":0}
             ,"ソ":{"win":0,"lost":0,"even":0}
        }

nokori_siai_team = {
        "ヤデ":0,
        "ヤ巨":0,
        "ヤ中":0,
        "ヤ広":0,
        "ヤ神":0,
        #"デヤ":0,
        "デ巨":0,
        "デ中":0,
        "デ広":0,
        "デ神":0,
        #"巨ヤ":0,
        #"巨デ":0,
        "巨中":0,
        "巨広":0,
        "巨神":0,
        #"中ヤ":0,
        #"中デ":0,
        #"中巨":0,
        "中広":0,
        "中神":0,
        #"広ヤ":0,
        #"広デ":0,
        #"広巨":0,
        #"広中":0,
        "広神":0,
        #"神ヤ":0,
        #"神デ":0,
        #"神巨":0,
        #"神中":0,
        #"神広":0,
        "ロ楽":0,
        "ロ日":0,
        "ロ西":0,
        "ロオ":0,
        "ロソ":0,
        #"楽ロ":0,
        "楽日":0,
        "楽西":0,
        "楽オ":0,
        "楽ソ":0,
        #"日ロ":0,
        #"日楽":0,
        "日西":0,
        "日オ":0,
        "日ソ":0,
        #"西ロ":0,
        #"西楽":0,
        #"西日":0,
        "西オ":0,
        "西ソ":0,
        #"オロ":0,
        #"オ楽":0,
        #"オ日":0,
        #"オ西":0,
        "オソ":0,
        #"ソロ":0,
        #"ソ楽":0,
        #"ソ日":0,
        #"ソ西":0,
        #"ソオ":0
        }

for url in url_list:

    res = urllib.request.urlopen(url)
    soup = BeautifulSoup(res, 'html.parser')
    a_list = soup.find_all("a")
    for a_para in a_list:

        if a_para.get("href").find("html") > 0 and a_para.get("href").find("bis") > 0 and a_para.get("href").find("games") > 0:
            #print(a_para.text)
            if a_para.get("href").find("gm2021") > 0:
                data_array = a_para.get("href").split("/")
                tmp_date1 = data_array[4][2:10]
                #print(tmp_date1)
                data.append({"date":tmp_date1,"shiai":[{"win":"","lost":"","even1":"","even2":""},
                                                       {"win":"","lost":"","even1":"","even2":""},
                                                       {"win":"","lost":"","even1":"","even2":""},
                                                       {"win":"","lost":"","even1":"","even2":""},
                                                       {"win":"","lost":"","even1":"","even2":""},
                                                       {"win":"","lost":"","even1":"","even2":""}],
                            "rating":{"ヤ":0,"デ":0,"巨":0,"中":0,"広":0,"神":0,"ロ":0,"楽":0,"日":0,"西":0,"オ":0,"ソ":0}})
                shiai_number = 0

            else:
                data1 = a_para.text.split("-")
                tesu1 = a_para.text.split(" ")
                if data1[0][0:1] == "セ":
                    continue
                if data1[0][0:1] == "パ":
                    continue
                if tesu1[1] == "*":
                    continue
                number = len(data) - 1
                if data1[0][0:1]+data1[1][len(data1[1])-1:len(data1[1])] in nokori_siai_team:
                    nokori_siai_team[data1[0][0:1]+data1[1][len(data1[1])-1:len(data1[1])]] += 1
                elif data1[1][len(data1[1])-1:len(data1[1])]+data1[0][0:1] in nokori_siai_team:
                    nokori_siai_team[data1[1][len(data1[1])-1:len(data1[1])]+data1[0][0:1]] += 1
                #print(a_para.text)
                if int(tesu1[1]) > int(tesu1[3]):
                    #print(data1[0][0:1] + " win " + tesu1[1])
                    #print(data1[1][len(data1[1])-1:len(data1[1])] + " lost " + tesu1[3])
                    data[number]["shiai"][shiai_number]["win"]  = data1[0][0:1]
                    data[number]["shiai"][shiai_number]["lost"] = data1[1][len(data1[1])-1:len(data1[1])]
                    result_team[data1[0][0:1]]["win"] += 1
                    result_team[data1[1][len(data1[1])-1:len(data1[1])]]["lost"] += 1
                elif int(tesu1[1]) < int(tesu1[3]):
                    #print(data1[0][0:1] + " lost " + tesu1[1])
                    #print(data1[1][len(data1[1])-1:len(data1[1])] + " win " + tesu1[3])
                    data[number]["shiai"][shiai_number]["lost"] = data1[0][0:1]
                    data[number]["shiai"][shiai_number]["win"]  = data1[1][len(data1[1])-1:len(data1[1])]
                    result_team[data1[0][0:1]]["lost"] += 1
                    result_team[data1[1][len(data1[1])-1:len(data1[1])]]["win"] += 1
                else:
                    #print(data1[0][0:1] + " even " + tesu1[1])
                    #print(data1[1][len(data1[1])-1:len(data1[1])] + " even " + tesu1[3])
                    data[number]["shiai"][shiai_number]["even1"] = data1[0][0:1]
                    data[number]["shiai"][shiai_number]["even2"] = data1[1][len(data1[1])-1:len(data1[1])]
                    result_team[data1[0][0:1]]["even"] += 1
                    result_team[data1[1][len(data1[1])-1:len(data1[1])]]["even"] += 1
                shiai_number += 1

now_rating = {"ヤ":1500,
              "デ":1500,
              "巨":1500,
              "中":1500,
              "広":1500,
              "神":1500,
              "ロ":1500,
              "楽":1500,
              "日":1500,
              "西":1500,
              "オ":1500,
              "ソ":1500
              }

for day in data:
    #print(day["date"])
    for shiai in day["shiai"]:
        #print(shiai["win"] + " " + shiai["lost"] + " " + shiai["even1"] + " " + shiai["even2"])
        if len(shiai["win"]) > 0:
            tmp_win  = round(now_rating[shiai["win"]]  + 32 * ( (now_rating[shiai["lost"]] - now_rating[shiai["win"]])/800+ 0.5))
            tmp_lost = round(now_rating[shiai["lost"]] - 32 * ( (now_rating[shiai["lost"]] - now_rating[shiai["win"]])/800+ 0.5))
            now_rating[shiai["win"]]  = tmp_win
            now_rating[shiai["lost"]] = tmp_lost

    day["rating"]["ヤ"] = now_rating["ヤ"]
    day["rating"]["デ"] = now_rating["デ"]
    day["rating"]["巨"] = now_rating["巨"]
    day["rating"]["中"] = now_rating["中"]
    day["rating"]["広"] = now_rating["広"]
    day["rating"]["神"] = now_rating["神"]
    day["rating"]["ロ"] = now_rating["ロ"]
    day["rating"]["楽"] = now_rating["楽"]
    day["rating"]["日"] = now_rating["日"]
    day["rating"]["西"] = now_rating["西"]
    day["rating"]["オ"] = now_rating["オ"]
    day["rating"]["ソ"] = now_rating["ソ"]

#print(data)

yotei_url_list = ["https://npb.jp/bis/2021/calendar/index_09.html",
                  "https://npb.jp/bis/2021/calendar/index_10.html"]
yotei_data = []
nokori_siai = {"ヤ":0,
               "デ":0,
               "巨":0,
               "中":0,
               "広":0,
               "神":0,
               "ロ":0,
               "楽":0,
               "日":0,
               "西":0,
               "オ":0,
               "ソ":0}


number = -1
for url in yotei_url_list:
    res = urllib.request.urlopen(url)
    body = res.read().decode("utf-8")
    div_list = body.split("div")
    flag = False
    for div_para in div_list:
        if div_para.find("href") > 0 and div_para.find("gm") > 0 and flag == True:
            #print(div_para[47:55])
            yotei_data.append({"date":div_para[47:55],"shiai":[]})
            number += 1
            #print(number)
        if div_para.find("-") > 0 and div_para.find("：") > 0 and flag == True:
            #print(div_para[1:6])
            #print(div_para[1:2])
            #print(div_para[5:6])
            #print(number)
            nokori_siai[div_para[1:2]] += 1
            nokori_siai[div_para[5:6]] += 1
            if div_para[1:2]+div_para[5:6] in nokori_siai_team:
                nokori_siai_team[div_para[1:2]+div_para[5:6]] += 1
            elif div_para[5:6]+div_para[1:2] in nokori_siai_team:
                nokori_siai_team[div_para[5:6]+div_para[1:2]] += 1
            yotei_data[number]["shiai"].append({"team1":div_para[1:2],"team2":div_para[5:6]})
        if div_para.find("body") > 0:
            flag = True
#print(nokori_siai)
print("登録試合数")
print(nokori_siai_team)
print("")
print("成績")
print(result_team)
print("")
print("レーティング")
print(now_rating)
#print(yotei_data)
f = open('yotei.json', 'w')
f.write(json.dumps(yotei_data))
f.close()

f = open('now_rating.json', 'w')
f.write(json.dumps(now_rating))
f.close()

f = open('result_team.json', 'w')
f.write(json.dumps(result_team))
f.close()

