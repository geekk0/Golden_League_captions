import datetime
import json
import time
import requests
import itertools


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

        if active_set < 4:
            new_block = str(score["red_points_set_"+str(active_set)])+"\n" + \
                        str(score["blue_points_set_"+str(active_set)])
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

    with open("AceOut.txt", "w", encoding="utf-8") as aceout_file:

        if score["red_ace_out"] != " ":

            ace_out = " "+score["red_ace_out"]+" "

        elif score["blue_ace_out"] != " ":

            ace_out = " "+score["blue_ace_out"]+" "

        else:
            ace_out = ""

        aceout_file.write(ace_out)
        aceout_file.close()


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

    url = "https://www.golden-league-stream.tk/api/Пляжный волейбол/Узнать счет"        # VDS

    raw_source = requests.get(url, auth=("referee", "ref12345")).text

    try:
        score = json.loads(raw_source)[0]

        dict(itertools.islice(score.items(), 20))

        return score

    except:
        time.sleep(1)
        print("api не доступен")


def clear_file(file_name):
    with open(file_name, "w", encoding="utf-8") as file:
        file.flush()
        file.close()
        time.sleep(0.5)


while True:
    # os.system('hide_current_console.exe')

    try:
        start_time = time.time()

        score_dict = get_match_data()

        show_time()

    except Exception as e:
        print(e)

    if score_dict:
        with open("Подача красных.txt", "w", encoding="utf-8") as red_inning_file:
            red_inning_file.flush()
        with open("Подача синих.txt", "w", encoding="utf-8") as blue_inning_file:
            blue_inning_file.flush()
        team_score(score=score_dict)
    else:
        time.sleep(1)

    # print("--- %s seconds ---" % (time.time() - start_time))
