import time
import msvcrt
import tkinter as tk

# Console-based timer, not part of the GUI application
def timer_console():
    seconds = int(input("Enter the time in seconds: "))
    elapsed = 0
    start_time = time.time()
    while(elapsed <= seconds):
        time.sleep(1)
        elapsed = time.time() - start_time
        print(round(elapsed))

# Console-based stopwatch, not part of the GUI application. May not work
def stopwatch_console():
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

# GUI-based stopwatch application

# Returns the elapsed time since start_time
def get_time(start_time):
    return time.time() - start_time


# Starts the stopwatch, adjusting for any previously elapsed time
def start_stopwatch(elapsed_time):
    global running
    running = True
    start_time = time.time() - elapsed_time
    switch_button()
    update_stopwatch(start_time)

# Updates the stopwatch display every 100 milliseconds
def update_stopwatch(start_time):
    global running
    if running:
        time_label.config(text=str(round(get_time(start_time), 1)))
        root.after(100, update_stopwatch, start_time)

# Stops the stopwatch, function switches button functions and text
def stop_stopwatch():
    global running
    running = False
    switch_button()

# Switches the button text and command based on the stopwatch state
def switch_button():
    if start_button.cget("text") == "Start":
        start_button.config(text="Stop", command=stop_stopwatch)
        clear_button.config(text="Lap", command=add_lap)
    else:
        start_button.config(text="Start", command=lambda: start_stopwatch(float(time_label.cget("text"))))
        clear_button.config(text="Clear", command=clear_all)

# Adds a lap entry to the lap listbox
def add_lap():
    if(running):
        global lap_num
        lap_num += 1
        lap_listbox.insert(0, "Lap " + str( lap_num) + ":      " + time_label.cget("text"))

# Clears all laps and resets the stopwatch display
def clear_all():
    global lap_num
    lap_num = 0
    lap_listbox.delete(0, tk.END)
    time_label.config(text="0.0")

# Initialize global variables
global running, lap_num
lap_num = 0
running = True
start_time = 0

# Set up the main application window, labels, buttons, and listbox
root = tk.Tk()
root.title("Stopwatch")
root.geometry("400x500")

time_label = tk.Label(root, text="0.0", font=("Helvetica", 30))
time_label.pack(pady=20)

start_button = tk.Button(root, text="Start", font=("Helvetica", 20),command=lambda: start_stopwatch(float(time_label.cget("text"))))
start_button.pack(pady=10)

clear_button = tk.Button(root, text="Clear", font=("Helvetica", 20), command=clear_all)
clear_button.pack(pady=10)


lap_frame = tk.Frame(root)
lap_frame.pack(pady=10, padx=(10, 0), fill=tk.BOTH, expand=True)
lap_listbox = tk.Listbox(lap_frame, height=10, font=("Helvetica", 15))
lap_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar = tk.Scrollbar(lap_frame, orient='vertical')
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
lap_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=lap_listbox.yview)
    
# Start the Tkinter event loop
root.mainloop()