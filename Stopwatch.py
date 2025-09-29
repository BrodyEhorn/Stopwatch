import time
import msvcrt
import tkinter as tk






def timer():
    seconds = int(input("Enter the time in seconds: "))
    elapsed = 0
    start_time = time.time()
    while(elapsed <= seconds):
        time.sleep(1)
        elapsed = time.time() - start_time
        print(round(elapsed))

def stopwatch():
    input("Press Enter to start the stopwatch")
    start_time = time.time()
    flag = True

    while(flag):
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'l':
                print("                     Lap: ", round(time.time() - start_time, 1))
            else:
                flag = False
        time.sleep(.1)
        elapsed = time.time() - start_time
        print(round(elapsed, 1))

def get_time(start_time):
    return time.time() - start_time

def start_stopwatch(elapsed_time):
    global running
    running = True
    start_time = time.time() - elapsed_time
    switch_button()
    update_stopwatch(start_time)

def update_stopwatch(start_time):
    global running
    if running:
        time_label.config(text=str(round(get_time(start_time), 1)))
        root.after(100, update_stopwatch, start_time)

def stop_stopwatch():
    global running
    running = False
    switch_button()


def switch_button():
    if start_button.cget("text") == "Start":
        start_button.config(text="Stop", command=stop_stopwatch)
    else:
        start_button.config(text="Start", command=lambda: start_stopwatch(float(time_label.cget("text"))))

global running
running = True
start_time = 0



root = tk.Tk()
root.title("Stopwatch")
root.geometry("400x400")

time_label = tk.Label(root, text="0.0", font=("Helvetica", 30))
time_label.pack(pady=20)

start_button = tk.Button(root, text="Start", font=("Helvetica", 20),command=lambda: start_stopwatch(float(time_label.cget("text"))))
start_button.pack(pady=10)

# stop_button = tk.Button(root, text="Stop",font=("Helvetica", 20),command=stop_stopwatch)
# stop_button.pack(pady=10)

# lap_button = tk.Button(root, text="Lap")
# lap_button.pack(pady=10)

clear_button = tk.Button(root, text="Clear", font=("Helvetica", 20), command=lambda: time_label.config(text="0.0"))
clear_button.pack(pady=10)

    
    



root.mainloop()













