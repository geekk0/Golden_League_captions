import time
from datetime import datetime
import threading
import requests

def team_score(team_color, squad):
    while True:
        with open(team_color, "w", encoding="utf-8") as red_team_file:
            team_set_score = "взято сетов: 3"
            team_current_points = "взято очков: "+str(datetime.now().time())
            new_block = squad+"\n"+team_set_score+"\n"+str(team_current_points)
            red_team_file.write(new_block)
            red_team_file.close()
        time.sleep(2)



red_team = threading.Thread(None, target=team_score, args=("Красная команда.txt", "Иванов и Петров") )
blue_team = threading.Thread(None, target=team_score, args=("Синяя команда.txt", "Сидоров и Второй"))
print("starting first team")
red_team.start()
print("starting second team")
blue_team.start()


# team_score(team_color="Красная команда.txt", squad="Иванов и Петров")

