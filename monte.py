import json
import random
import copy

json_open = open('yotei.json', 'r')
yotei = json.load(json_open)

yotei.append({"date": "20211025", "shiai": [{"team1": "ヤ", "team2": "デ"}, {"team1": "ロ", "team2": "日"}, {"team1": "楽", "team2": "オ"}]})
yotei.append({"date": "20211026", "shiai": [{"team1": "ヤ", "team2": "広"}, {"team1": "ロ", "team2": "日"}, {"team1": "楽", "team2": "ソ"}]})
yotei.append({"date": "20211027", "shiai": [{"team1": "ロ", "team2": "日"}]})
yotei.append({"date": "20211028", "shiai": [{"team1": "ロ", "team2": "日"}]})
yotei.append({"date": "20211029", "shiai": [{"team1": "日", "team2": "西"}]})

json_open = open('now_rating.json', 'r')
now_rating = json.load(json_open)

json_open = open('result_team.json', 'r')
result_team = json.load(json_open)


loop = 3000
monte_data = []
monte_data_rating = []

for i in range(loop):
    monte_result_team = copy.deepcopy(result_team)
    monte_now_rating  = copy.deepcopy(now_rating)
    for yotei_para in yotei:
        for shiai in yotei_para["shiai"]:
            team1_rating = monte_now_rating[shiai["team1"]]
            team2_rating = monte_now_rating[shiai["team2"]]
            wab = (team1_rating - team2_rating)/800 + 0.5
            ran = random.random()
            if ran <= wab:
                monte_result_team[shiai["team1"]]["win"]  += 1
                monte_result_team[shiai["team2"]]["lost"] += 1
                tmp_win  = round(monte_now_rating[shiai["team1"]] + 32 * ( (monte_now_rating[shiai["team2"]] - monte_now_rating[shiai["team1"]])/800+ 0.5))
                tmp_lost = round(monte_now_rating[shiai["team2"]] - 32 * ( (monte_now_rating[shiai["team2"]] - monte_now_rating[shiai["team1"]])/800+ 0.5))
                monte_now_rating[shiai["team1"]] = tmp_win
                monte_now_rating[shiai["team2"]] = tmp_lost

            else:
                monte_result_team[shiai["team1"]]["lost"] += 1
                monte_result_team[shiai["team2"]]["win"]  += 1
                tmp_win  = round(monte_now_rating[shiai["team2"]] + 32 * ( (monte_now_rating[shiai["team1"]] - monte_now_rating[shiai["team2"]])/800+ 0.5))
                tmp_lost = round(monte_now_rating[shiai["team1"]] - 32 * ( (monte_now_rating[shiai["team1"]] - monte_now_rating[shiai["team2"]])/800+ 0.5))
                monte_now_rating[shiai["team2"]] = tmp_win
                monte_now_rating[shiai["team1"]] = tmp_lost
    #############
    monte_data.append(copy.deepcopy(monte_result_team))
    monte_data_rating.append(copy.deepcopy(monte_now_rating))
#print(monte_data)
#print(monte_data_rating)
c_array = ["ヤ","デ","巨","中","広","神"]
p_array = ["ロ","楽","日","西","オ","ソ"]
result_c = {
         "ヤ":[0,0,0,0,0,0]
        ,"デ":[0,0,0,0,0,0]
        ,"巨":[0,0,0,0,0,0]
        ,"中":[0,0,0,0,0,0]
        ,"広":[0,0,0,0,0,0]
        ,"神":[0,0,0,0,0,0]
        }
result_p = {
         "ロ":[0,0,0,0,0,0]
        ,"楽":[0,0,0,0,0,0]
        ,"日":[0,0,0,0,0,0]
        ,"西":[0,0,0,0,0,0]
        ,"オ":[0,0,0,0,0,0]
        ,"ソ":[0,0,0,0,0,0]
        }

tmp_win_c = {
         "ヤ":0
        ,"デ":0
        ,"巨":0
        ,"中":0
        ,"広":0
        ,"神":0
        }
tmp_win_p = {
         "ロ":0
        ,"楽":0
        ,"日":0
        ,"西":0
        ,"オ":0
        ,"ソ":0
        }
for monte_1 in monte_data:
    for c in c_array:
        tmp_win_c[c] = monte_1[c]["win"]/(monte_1[c]["win"] + monte_1[c]["lost"])
    for c in p_array:
        tmp_win_p[c] = monte_1[c]["win"]/(monte_1[c]["win"] + monte_1[c]["lost"])
    c_sorted = sorted(tmp_win_c.items(), key=lambda x:x[1],reverse=True)
    #print(c_sorted)
    p_sorted = sorted(tmp_win_p.items(), key=lambda x:x[1],reverse=True)
    #print(p_sorted)
    count = 0
    #print(c_sorted[0].items())
    for c in c_sorted:
        #print(c[0])
        result_c[c[0]][count] += 1
        count += 1
    count = 0
    for c in p_sorted:
        #print(c[0])
        result_p[c[0]][count] += 1
        count += 1

#jyuni_c
jyuni_c = {}
jyuni_p = {}
for c in result_c:
    #print(c)
    temp_p = (result_c[c][0]*1 + result_c[c][1]* 2 + result_c[c][2] * 3 + result_c[c][3] * 4 + result_c[c][4] * 5 + result_c[c][5] * 6)/loop
    #print(temp_p)
    jyuni_c[c] = temp_p
for c in result_p:
    #print(c)
    temp_p = (result_p[c][0]*1 + result_p[c][1]* 2 + result_p[c][2] * 3 + result_p[c][3] * 4 + result_p[c][4] * 5 + result_p[c][5] * 6)/loop
    #print(temp_p)
    #jyuni_p.append({c:temp_p})
    jyuni_p[c] = temp_p

#print(jyuni_c) 
#print(jyuni_p) 
c_jyuni = sorted(jyuni_c.items(), key=lambda x:x[1])
p_jyuni = sorted(jyuni_p.items(), key=lambda x:x[1])
print("セリーグ順位予想")
print("team  1       2       3       4       5       6")
for team in c_jyuni:
    #print(result_c[team[0]])
    #print(team[0] + "   " + str(round(result_c[team[0]][0]/3000*100,1)) + "   " + str(round(result_c[team[0]][1]/3000*100,1)) + "   " + 
    #                str(round(result_c[team[0]][2]/3000*100,1)) + "   " + str(round(result_c[team[0]][3]/3000*100,1)) +
    #          "   " + str(round(result_c[team[0]][4]/3000*100,1)) + "   " + str(round(result_c[team[0]][5]/3000*100,1)))
    #formatted_msg = '%s %2.1f %2.1f %2.1f %2.1f %2.1f %2.1f' % \
    #        (team[0],round(result_p[team[0]][0]/3000*100,1),round(result_p[team[0]][1]/3000*100,1),
    #                round(result_p[team[0]][2]/3000*100,1),round(result_p[team[0]][3]/3000*100,1),
    #                round(result_p[team[0]][4]/3000*100,1),round(result_p[team[0]][5]/3000*100,1))
    format_msg = '%s   % 2.1f   % 2.1f   % 2.1f   % 2.1f   % 2.1f   % 2.1f' % (team[0],round(result_c[team[0]][0]/3000*100,1),round(result_c[team[0]][1]/3000*100,1),
            round(result_c[team[0]][2]/3000*100,1),round(result_c[team[0]][3]/3000*100,1),round(result_c[team[0]][4]/3000*100,1),round(result_c[team[0]][5]/3000*100,1))
    print(format_msg)

print("")
print("パリーグ順位予想")
print("team  1       2       3       4        5       6")
    
for team in p_jyuni:
    #print(result_p[team[0]])
    #print(team[0] + "   " + str(round(result_p[team[0]][0]/3000*100)) + "   " + str(round(result_p[team[0]][1]/3000*100)) + "   " + 
    #                str(round(result_p[team[0]][2]/3000*100)) + "   " + str(round(result_p[team[0]][3]/3000*100)) +
    #          "   " + str(round(result_p[team[0]][4]/3000*100)) + "   " + str(round(result_p[team[0]][5]/3000*100)))
    format_msg = '%s   % 2.1f   % 2.1f   % 2.1f   % 2.1f   % 2.1f   % 2.1f' % (team[0],round(result_p[team[0]][0]/3000*100,1),round(result_p[team[0]][1]/3000*100,1),
            round(result_p[team[0]][2]/3000*100,1),round(result_p[team[0]][3]/3000*100,1),round(result_p[team[0]][4]/3000*100,1),round(result_p[team[0]][5]/3000*100,1))
    print(format_msg)


#print(result_c)
#print(result_p)


    





