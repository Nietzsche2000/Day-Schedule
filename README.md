# Day Scheduler
Programming Language: Python 

## A bit of historical note to what inspired me to build this system. 

During the Spring of 2022, due to the aftermath of COVID-19, all my classes were moved online. With taking 5 classes, my schedule was dense. In addition, I also began my training as part of the California Lightweight Rowing. As a rower, I had to wake up at 4:45 AM for morning training on the water. 
As my life became more busy, due to a cumulation of lack of sleep, at one point, during the beginning of the semester, I accidentally slept through one of the online lectures. Something had to be done. 
As a coder, what better way to utilize one of my innocent, unused old computers to run a computer program that pretty much yells, ***yes! the program speaks***, at me when it is time for lectures. And so it began.
Written in python, it took me about 2hrs to complete this project. 


    # THE MEAT OF THE PROBLEM
    class Schedule:
        def __init__(self, person_name, description):
            self.tasks = []
            self.to_speak = []
            self.current_status = []
            self.n_of_tasks = 0
            self.person_name = person_name
            self.description = description

The `Schedule` class contains all the necessary fields for this program to work smoothly. 

1. The `self.tasks` contains the list of tasks that have been pushed on.
2. A task is an abstract idea that is implemented as a list; it contains the name of the task and the corresponding end time. `[task_name, end_time]`


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

These are some useful helper functions. 

1. The `def task_display_time_remain(task_name, end_time)` is responsible for making a task which will then be pushed on and kept track of.
2. The `def clear_console()` is used since the entire program runs on the command line, and, though not the best way to accomplish updates, to update after the first iteration of the countdown timer of each task, the entire screen is cleared and reprinted with all the remaining tasks. Doing this fast, we can see smooth updates. 
3. The `def add_sound(text)` is written to add sound to the system. It will run differently on different machines. Uncommenting the mac line for mac systems and likewise for windows. 

**The entire code is here.** 

1. Create a file `main.py`
2. Add the following code.
3. If windows, uncomment the windows line and comment the mac line in the function `add_sound(text)` and otherwise do the exact opposite. 
4. Run `python main.py`


    import datetime
    import os
    import sys
    import time
    import pyttsx3
    import tqdm
    from operator import attrgetter
    
    
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
        today.add_task("Task 1", [2023, 3, 24, 23, 59, 59])
        today.add_task("Task 2", [2023, 4, 24, 23, 59, 59])
        today.add_task("Task 3", [2023, 5, 24, 23, 59, 59])
        today.add_task("Task 4", [2023, 6, 24, 23, 59, 59])
        today.add_task("Task 5", [2023, 7, 24, 23, 59, 59])
        today.countdown()
    

Example Run.

![](https://paper-attachments.dropboxusercontent.com/s_28708D72545886A725E5C1AAA908ACCFF1A01305E8184B2EADEB2763730EA4AE_1680857082987_Screen+Shot+2023-04-07+at+1.44.39+AM.png)


