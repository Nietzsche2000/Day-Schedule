import datetime
import os
import sys
import time
import pyttsx3
import tqdm
from operator import attrgetter


# ADD SOME COLOR: https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# USEFUL HELPER FUNCTIONS
def task_display_time_remain(task_name, end_time):
    present = datetime.datetime.now()
    future = datetime.datetime(end_time[0], end_time[1], end_time[2], end_time[3],
                               end_time[4], end_time[5])  # year, month, day, hours, minutes, seconds
    difference = future - present  # DANGER
    return [task_name, difference]


def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def add_sound(text):
    engine = pyttsx3.init()
    # engine.setProperty('voice', 'com.apple.speech.synthesis.voice.karen') # MAC
    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0') # WINDOWS
    engine.say(text)
    engine.runAndWait()


# THE MEAT OF THE PROBLEM
class Schedule:
    def __init__(self, person_name, description):
        self.tasks = []
        self.to_speak = []
        self.current_status = []
        self.n_of_tasks = 0
        self.person_name = person_name
        self.description = description

    def add_task(self, task_name, end_time):
        self.tasks.append([task_name, end_time])
        self.n_of_tasks += 1

    # FROM SELF.TASKS NOT SELF.CURRENT_STATUS
    def remove_task(self, task_name):
        for task in self.tasks:
            if task[0] == task_name:
                self.tasks.remove(task)
                self.n_of_tasks -= 1
        print(task_name + " TIME UP ")

    def delete_comp_task(self):
        curr_stat_dup = list(self.current_status)
        for task in self.current_status:
            if task[1].days < 0:
                print("DELETED TASK " + task[0])
                self.remove_task(task[0])
                curr_stat_dup.remove(task)
        self.current_status = curr_stat_dup

    def do_countdown(self):
        self.current_status = [task_display_time_remain(task[0], task[1]) for task in self.tasks]
        # SORT ASCENDING
        self.current_status = sorted(self.current_status, key=lambda task: task[1])

    def __str__(self):
        m_data = f" {bcolors.OKGREEN}NAME: {self.person_name}{bcolors.ENDC}\n {bcolors.OKGREEN}DESCRIPTION: {self.description}{bcolors.ENDC}"
        to_show = ""
        curr_time = f" {bcolors.OKCYAN}CURRENT TIME: {datetime.datetime.now()}{bcolors.ENDC}"
        i = 1
        for task in self.current_status:
            to_show = f"{to_show} {bcolors.WARNING} {i}. TASK NAME: {bcolors.ENDC}{bcolors.BOLD}{task[0]}{bcolors.ENDC} | {bcolors.FAIL}TIME REMAINING: {task[1]} {bcolors.ENDC} \n"
            if task[1] <= datetime.timedelta(minutes=5):
                self.to_speak.append(f" TASK NAME: {task[0]} TIME REMAINING: {str(task[1])}")
            # self.progress_bar()
            i += 1
        return m_data + "\n" + curr_time  + "\n\n" + to_show

    def dynamic_refresh(self):
        dtext = self.__str__()
        sys.stdout.write(dtext)
        sys.stdout.flush()

    def countdown(self):
        while self.n_of_tasks > 0:
            self.do_countdown()
            self.delete_comp_task()
            print(self)
            self.speak_now()
            time.sleep(1)
            clear_console()
            self.reset()

    def speak_now(self):
        if len(self.to_speak) != 0:
            for task in self.to_speak:
                add_sound(task)

    def reset(self):
        self.to_speak = []

    def progress_bar(self, input_time):
        total_time = 365 * 24 * 60 * 60
        pbar = tqdm.tqdm(range(total_time))
        pbar.update(total_time - input_time)
        pbar.refresh()
# THE USUAL
if __name__ == "__main__":
    today = Schedule("MONISH WARAN", "SPRING 2022 WORK SCHEDULE")
    today.add_task("CS70 HW 1", [2022, 1, 24, 23, 59, 59])
    today.add_task("Math 104 HW 1", [2022, 2, 2, 23, 59, 59])
    today.add_task("Math 104 HW 2", [2022, 2, 9, 23, 59, 59])
    today.add_task("Math 104 HW 3", [2022, 2, 16, 23, 59, 59])
    today.add_task("Math 104 HW 4", [2022, 2, 23, 23, 59, 59])
    today.add_task("EE16B Signup", [2022, 1, 18, 12, 0, 0])
    today.add_task("EE16B HW 00", [2022, 1, 24, 23, 59, 59])
    today.add_task("DATA C104 Personal Reflection", [2022, 1, 22, 23, 59, 59])
    today.countdown()
