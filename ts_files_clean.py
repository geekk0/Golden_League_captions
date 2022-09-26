import os
import time
import datetime


current_path = os.getcwd()
suffix = ".ts"
deleted_files = 0
optimized_memory = 0
delete_list = []


def create_delete_list(suffix):

    global delete_list

    for i in os.walk(current_path):

        for j in i[2]:

            if j.endswith(suffix):
                path = os.path.join(os.path.abspath(i[0]), j)
                file_create_date = time.ctime(os.path.getctime(path))

                converted_file_created = datetime.datetime.strptime(file_create_date, '%a %b %d %H:%M:%S %Y')
                now = datetime.datetime.now()

                time_check = datetime.timedelta(seconds=90)

                if (now - converted_file_created) >= time_check:
                    delete_list.append(j)

    return delete_list


def run_delete():

    global delete_list

    for i in os.walk(current_path):
        for j in i[2]:
            if j in delete_list:

                cache_memory = os.path.getsize(os.path.join(os.path.abspath(i[0]), j))/1000000000
                del_file_path = os.path.join(os.path.abspath(i[0]), j)
                os.remove(del_file_path)

                global deleted_files
                global optimized_memory

                deleted_files += 1
                optimized_memory += cache_memory


if __name__ == "__main__":

    """suffix = get_suffix()
    interval = get_interval()
    count = get_count()"""

    while True:
        delete_list = create_delete_list(".ts")
        if delete_list:
            run_delete()
        print(datetime.datetime.now().date(), flush=True)
        print(str(datetime.datetime.now().time().hour) + ":" + str(datetime.datetime.now().time().minute), flush=True)
        print("Файлов удалено: " + str(deleted_files), flush=True)
        print("Освободилось памяти: " + str(optimized_memory) + " Гб", flush=True)
        deleted_files = 0
        optimized_memory = 0
        delete_list.clear()
        time.sleep(30)


