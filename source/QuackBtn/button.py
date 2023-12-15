from sound import quack
import tkinter as tk

class DraggableButtonObj:
    def __init__(self, master, **kwargs):
        self.master = master
        self.button = tk.Button(master, **kwargs, )
        self.start_x, self.start_y = 0, 0
        self.moved = False

        self.button.bind("<B1-Motion>", self.on_drag)
        self.button.bind("<ButtonPress-1>", self.on_press)
        self.button.bind("<ButtonRelease-1>", self.on_release)

    def on_drag(self, event):
        x = event.x_root - self.start_x
        y = event.y_root - self.start_y

        self.master.geometry(f"+{x}+{y}")
        self.moved = True

    def on_press(self, event):
        self.start_x = event.x_root - self.master.winfo_x()
        self.start_y = event.y_root - self.master.winfo_y()

    def on_release(self, event):
        if not self.moved:
            quack()

        self.moved = False

if __name__ == "__main__":

    window = tk.Tk()
    window.overrideredirect(True)
    window.attributes('-topmost', True)

    DragButtobj = DraggableButtonObj(window, text="Quack!", )
    DragButtobj.button.pack()

    
    window.mainloop()
