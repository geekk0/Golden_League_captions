import datetime
import time
import requests


def team_score(score):

    with open("Состав красная команда.txt", "w", encoding="utf-8") as red_squad_file:
        red_squad_file.write(score["red_squad"])
        red_squad_file.close()

    with open("Состав синяя команда.txt", "w", encoding="utf-8") as blue_squad_file:
        blue_squad_file.write(score["blue_squad"])
        blue_squad_file.close()

    with open("Счет партий.txt", "w", encoding="utf-8") as set_score_file:

        new_block = str(score["red_set_score"])+"\n"+str(score["blue_set_score"])

        """new_block = str(score["red_set_score"])+"  "+str(score["red_points_set_1"]) +\
            " "+str(score["red_points_set_2"])+" "+str(score["red_points_set_3"])+"\n" +\
            str(score["blue_set_score"])+"  "+str(score["blue_points_set_1"])+" " +\
            str(score["blue_points_set_2"])+" "+str(score["blue_points_set_3"])"""

        set_score_file.write(new_block)
        set_score_file.close()

    with open("Счет текущей партии.txt", "w", encoding="utf-8") as current_set_score_file:

        active_set = score["active_set"]
        red_points = str(score["red_points_set_"+str(active_set)])
        blue_points = str(score["blue_points_set_"+str(active_set)])

        """if len(red_points) < 2:
            red_points = " "+red_points
        if len(blue_points) < 2:
            blue_points = " "+blue_points"""

        new_block = str(score["red_points_set_"+str(active_set)])+"\n"+str(score["blue_points_set_"+str(active_set)])

        current_set_score_file.write(new_block)

    with open("Подача.txt", "w", encoding="utf-8") as active_inning_file:

        if score["current_inning"] == "red":

            new_block = "●"

        elif score["current_inning"] == "blue":

            new_block = "\n●"

        else:

            new_block = ""

        active_inning_file.write(new_block)
        active_inning_file.close()




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

    url = "http://192.168.77.2/api/Пляжный волейбол/Узнать счет"          # Локальная сеть

    # url = "http://185.18.202.239/api/Пляжный волейбол/Узнать счет"        # Внешняя

    # url = "http://188.225.38.178:4000/api/Пляжный волейбол/Узнать счет"   # VDS

    # url = "http://127.0.0.1:8000/api/Пляжный волейбол/Узнать счет"        # Dev

    # raw_source = requests.get(url, auth=("admin", "123456Qe")).text

    raw_source = requests.get(url, auth=("admin", "MGZJc2SS0eYcUJsXJsq1")).text

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
        with open("Подача красных.txt", "w", encoding="utf-8") as red_inning_file:
            red_inning_file.flush()
        with open("Подача синих.txt", "w", encoding="utf-8") as blue_inning_file:
            blue_inning_file.flush()
        formatted_score = format_score(score_dict)
        team_score(score=formatted_score)

    # print("--- %s seconds ---" % (time.time() - start_time))
