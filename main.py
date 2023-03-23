import tkinter as tk
from tkinter import ttk

class PomodoroTimer(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Pomodoro Timer")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        container = ttk.Frame(self)
        container.grid()
        container.columnconfigure(0, weight=1)

        timer_frame = Timer(container)
        timer_frame.grid(row=0, column=0, sticky="NESW")

class Timer(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.current_time = tk.StringVar(value="00:10")
        self.timer_running = True

        timer_frame = ttk.Frame(self, height="100")
        timer_frame.grid(pady=(10, 0), sticky="NSEW")

        timer_counter = ttk.Label(
            timer_frame,
            textvariable=self.current_time
        )
        timer_counter.grid()

        self.decrement_time()

    def decrement_time(self):
        pass

app = PomodoroTimer()
app.mainloop()
