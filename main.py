import datetime
import os
import time

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
    difference = future - present
    return [task_name, difference]

def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

# THE MEAT OF THE PROBLEM
class Schedule:
    def __init__(self):
        self.tasks = []
        self.current_status = []
        self.n_of_tasks = 0

    def add_task(self, task_name, end_time):
        self.tasks.append([task_name, end_time])
        self.n_of_tasks += 1

    def remove_task(self, task_name):
        for task in self.tasks:
            if task[0] == task:
                self.tasks.remove(task)
                self.n_of_tasks -= 1
        print(task_name + " TIME UP ")

    def delete_comp_task(self):
        for task in self.current_status:
            if task[1] <= 0:
                print("DELETED TASK " + task[0])
                self.remove_task(task[0])

    def do_countdown(self):
        self.current_status = [task_display_time_remain(task[0], task[1]) for task in self.tasks]

    def __str__(self):
        to_show = ""
        for task in self.current_status:
            to_show = f"{bcolors.FAIL}{to_show} TASK NAME: {task[0]}{bcolors.ENDC} | {bcolors.OKGREEN}TIME REMAINING: {str(task[1])}{bcolors.ENDC} \n"
        return to_show

    def countdown(self):
        while self.n_of_tasks > 0:
            self.do_countdown()
            print(self)
            time.sleep(1)
            clear_console()


# THE USUAL
if __name__ == "__main__":
    today = Schedule()
    today.add_task("Discussion Signup", [2022, 1, 17, 12, 0, 0])
    today.countdown()
