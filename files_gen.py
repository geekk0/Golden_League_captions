import datetime
import time
import requests


def team_score(score):

    with open("Состав команд.txt", "w", encoding="utf-8") as squad_file:
        squad_file.write(score["red_squad"][:32]+"\n"+score["blue_squad"][:32])
        squad_file.close()

    with open("Счет.txt", "w", encoding="utf-8") as red_team_file:

        new_block = str(score["red_set_score"])+" "+str(score["red_points_set_1"]) +\
            " "+str(score["red_points_set_2"])+" "+str(score["red_points_set_3"])+"\n" +\
            str(score["blue_set_score"])+" "+str(score["blue_points_set_1"])+" " +\
            str(score["blue_points_set_2"])+" "+str(score["blue_points_set_3"])

        red_team_file.write(new_block)
        red_team_file.close()

    with open("Подача красных.txt", "w", encoding="utf-8") as red_inning_file:
        with open("Подача синих.txt", "w", encoding="utf-8") as blue_inning_file:
            if score["current_inning"] == "red":
                red_inning_file.write(".")
                red_inning_file.close()
                blue_inning_file.flush()
            elif score["current_inning"] == "blue":
                blue_inning_file.write(".")
                blue_inning_file.close()
                red_inning_file.flush()
            else:
                blue_inning_file.flush()
                red_inning_file.flush()


def show_time():

    with open("Время.txt", "w", encoding="utf-8") as time_file:
        current_time = datetime.datetime.now().time()
        minutes = current_time.minute
        if len(str(minutes)) < 2:
            minutes = "0"+str(minutes)
        time_file.write(str(current_time.hour)+":"+str(minutes))
        time_file.close()


# noinspection PyBroadException
def get_match_data():

    # url = "http://192.168.77.2/api/Пляжный волейбол/Узнать счет"          # Локальная сеть

    # url = "http://185.18.202.239/api/Пляжный волейбол/Узнать счет"        # Внешняя

    # url = "http://188.225.38.178:4000/api/Пляжный волейбол/Узнать счет"   # VDS

    url = "http://127.0.0.1:8000/api/Пляжный волейбол/Узнать счет"        # Dev

    raw_source = requests.get(url, auth=("admin", "123456Qe")).text

    # raw_source = requests.get(url, auth=("admin", "MGZJc2SS0eYcUJsXJsq1")).text

    try:
        score = eval(raw_source)[0]

        return score

    except:
        time.sleep(0.5)


def clear_file(file_name):
    with open(file_name, "w", encoding="utf-8") as file:
        file.flush()
        file.close()
        time.sleep(0.5)


def format_score(score):

    if len(str(score["red_points_set_1"])) > len(str(score["blue_points_set_1"])):
        score["blue_points_set_1"] = " " + str(score["blue_points_set_1"])
    elif len(str(score["red_points_set_1"])) < len(str(score["blue_points_set_1"])):
        score["red_points_set_1"] = " " + str(score["red_points_set_1"])

    if len(str(score["red_points_set_2"])) > len(str(score["blue_points_set_2"])):
        score["blue_points_set_2"] = " " + str(score["blue_points_set_2"])
    elif len(str(score["red_points_set_2"])) < len(str(score["blue_points_set_2"])):
        score["red_points_set_2"] = " " + str(score["red_points_set_2"])

    if len(str(score["red_points_set_3"])) > len(str(score["blue_points_set_3"])):
        score["blue_points_set_3"] = " " + str(score["blue_points_set_3"])
    elif len(str(score["red_points_set_3"])) < len(str(score["blue_points_set_3"])):
        score["red_points_set_3"] = " " + str(score["red_points_set_3"])

    return score

while True:
    # os.system('hide_current_console.exe')

    start_time = time.time()

    score_dict = get_match_data()

    show_time()

    if score_dict:
        formatted_score = format_score(score_dict)
        team_score(score=formatted_score)

    # print("--- %s seconds ---" % (time.time() - start_time))
