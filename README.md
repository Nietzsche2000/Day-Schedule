# Day Scheduler

**Programming Language:** Python

## Inspiration

In Spring 2022, with the shift to online classes due to COVID-19 and a burgeoning rowing schedule with the California Lightweight Rowing team, managing time became challenging. The need for an automated system became clear when sleep deprivation led to missing an online lecture. As a remedy, I crafted a Python program that serves as a vocal reminder for my commitments.

## Project Overview

This Day Scheduler is a Python application designed to organize and vocalize daily tasks. It took approximately 2 hours to develop and serves as a personal assistant to prevent oversleeping or missing important events.

## Features

- **Personalized Schedule Management**: Tracks and updates a user's daily tasks.
- **Audio Alerts**: Provides audible reminders for upcoming tasks.

## The `Schedule` Class

At the heart of the program is the `Schedule` class, which is structured as follows:

- `self.tasks`: A dynamic list that holds tasks and their end times.
- `self.to_speak`: Queues up tasks for audible announcements.
- `self.current_status`: Monitors the current status of all tasks.
- `self.n_of_tasks`: Counts the total number of tasks in the schedule.

Each task is represented as a list with the format `[task_name, end_time]`.

## Helper Functions

Several functions streamline the scheduling process:

- `task_display_time_remain()`: Calculates the remaining time for a given task.
- `clear_console()`: Clears the command line interface for a fresh display of tasks.
- `add_sound()`: Initiates audio playback for task reminders.

## Setup and Usage

1. Create a `main.py` file.
2. Insert the code from the snippet provided.
3. Modify the `add_sound(text)` function for compatibility with your operating system.
4. Execute the script with the command: `python main.py`

## Example

Here's a snapshot of the Day Scheduler in action:

![Day Scheduler Example Run](https://paper-attachments.dropboxusercontent.com/s_28708D72545886A725E5C1AAA908ACCFF1A01305E8184B2EADEB2763730EA4AE_1680857082987_Screen+Shot+2023-04-07+at+1.44.39+AM.png)


## Acknowledgements

This tool was inspired by the challenges faced during an unprecedented time and the determination to leverage technology for effective time management.
