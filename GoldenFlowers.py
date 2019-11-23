from tkinter import *
import math
# from random import random


class FlowersGui:

    def __init__(self, main_window):
        self.main_window = main_window
        self.main_window.title("Golden Flowers")
        self.main_window.geometry("500x450")

        self.dots_window = None
        self.isOpen = False
        title_label = Label(self.main_window, text="Golden Flowers", font=("Impact", 35))
        title_label.pack(side=TOP, pady=10)

        self.body_frame = Frame(self.main_window)
        self.body_frame.pack()

        self.settings_pane = Frame(self.body_frame)
        self.settings_pane.pack()
        factor_label = Label(self.settings_pane, text="Factor: ", font="Times 10")
        factor_label.grid(row=0, column=0, pady=5, padx=5, sticky=E)
        num_of_dots_label = Label(self.settings_pane, text="Number of dots: ", font="Times 10")
        num_of_dots_label.grid(row=1, column=0, pady=5, padx=5, sticky=E)
        layers_label = Label(self.settings_pane, text="Layers: ", font="Times 10")
        layers_label.grid(row=2, column=0, pady=5, padx=5, sticky=E)
        layers_factor_label = Label(self.settings_pane, text="Factor between layers: ", font="Times 10")
        layers_factor_label.grid(row=3, column=0, pady=5, padx=5, sticky=E)
        zoom_label = Label(self.settings_pane, text="Zoom: ", font="Times 10")
        zoom_label.grid(row=4, column=0, pady=5, padx=5, sticky=E)
        self.factor_entry = Entry(self.settings_pane)
        self.factor_entry.grid(row=0, column=1, sticky=E, pady=5, padx=5)
        self.num_of_dots_entry = Entry(self.settings_pane)
        self.num_of_dots_entry.grid(row=1, column=1, sticky=E, pady=5, padx=5)
        self.layers_entry = Entry(self.settings_pane)
        self.layers_entry.grid(row=2, column=1, sticky=E, pady=5, padx=5)
        self.layers_factor_entry = Entry(self.settings_pane)
        self.layers_factor_entry.grid(row=3, column=1, sticky=E, pady=5, padx=5)
        self.zoom_entry = Entry(self.settings_pane)
        self.zoom_entry.grid(row=4, column=1, sticky=E, pady=5, padx=5)

        start_dots_button = Button(self.body_frame, text="Start Dots", command=self.startDots, height=2, width=9)
        start_dots_button.pack()
        if self.isOpen:
            self.dots_window.protocol("WM_DELETE_WINDOW", self.onClosing)

    def onClosing(self):
        print("Closed")
        self.isOpen = False
        self.dots_window.destroy()

    def startDots(self):
        self.dots_window = Tk()
        self.dots_window.title("Layout")
        self.dots_window.geometry("900x750")
        self.isOpen = True

        self.dots_window.update()
        self.dot_size = 10
        self.zoom = 0.5
        self.dif_factor_between_layers = 0
        self.starting_dot_x = self.dots_window.winfo_width()/2
        self.starting_dot_y = self.dots_window.winfo_height()/2

        #  Draw first center dot, init canvas.
        self.canvas = Canvas(self.dots_window, width=self.dots_window.winfo_width(),
                             height=self.dots_window.winfo_height()-75, scrollregion=(-500, -650, 1500, 1350))
        hbar = Scrollbar(self.canvas, orient=HORIZONTAL)
        hbar.pack(side=BOTTOM, fill=X)
        hbar.config(command=self.canvas.xview)
        vbar = Scrollbar(self.canvas, orient=VERTICAL)
        vbar.pack(side=RIGHT, fill=Y)
        vbar.config(command=self.canvas.yview)
        self.canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        self.canvas.pack(expand=YES, fill=BOTH)
        self.canvas.create_oval(self.starting_dot_x, self.starting_dot_y, self.starting_dot_x + self.dot_size,
                                self.starting_dot_y + self.dot_size, fill='black')

        # control panel (buttons)
        self.score_panel_frame = Frame(self.dots_window)
        self.score_panel_frame.pack()
        self.control_panel_frame = Frame(self.dots_window)
        self.control_panel_frame.pack()
        factor_label = Label(self.score_panel_frame, text="Factor: ", font="Times 10")
        factor_label.grid(row=0, column=4, pady=3, padx=3)
        self.factor_string_val = StringVar(self.score_panel_frame)    # for textvariable
        factor_value_label = Label(self.score_panel_frame, textvariable=self.factor_string_val, font="Times 10")
        factor_value_label.grid(row=0, column=5, pady=3, padx=3)
        reduce1Button = Button(self.control_panel_frame, text="-1", command=lambda: self.changeFactor(-1), height=2, width=5)
        reduce1Button.grid(row=1, column=0, sticky=E, pady=3, padx=3)
        reduce2Button = Button(self.control_panel_frame, text="-0.1", command=lambda: self.changeFactor(-0.1), height=2, width=5)
        reduce2Button.grid(row=1, column=1, sticky=E, pady=3, padx=3)
        reduce3Button = Button(self.control_panel_frame, text="-0.01", command=lambda: self.changeFactor(-0.01), height=2, width=5)
        reduce3Button.grid(row=1, column=2, sticky=E, pady=3, padx=3)
        reduce4Button = Button(self.control_panel_frame, text="-0.001", command=lambda: self.changeFactor(-0.001), height=2, width=5)
        reduce4Button.grid(row=1, column=3, sticky=E, pady=3, padx=3)
        reduce5Button = Button(self.control_panel_frame, text="-0.0001", command=lambda: self.changeFactor(-0.0001), height=2, width=5)
        reduce5Button.grid(row=1, column=4, sticky=E, pady=3, padx=3)

        raise1Button = Button(self.control_panel_frame, text="+0.0001", command=lambda: self.changeFactor(0.0001), height=2, width=5)
        raise1Button.grid(row=1, column=5, sticky=E, pady=3, padx=3)
        raise2Button = Button(self.control_panel_frame, text="+0.001", command=lambda: self.changeFactor(0.001), height=2, width=5)
        raise2Button.grid(row=1, column=6, sticky=E, pady=3, padx=3)
        raise3Button = Button(self.control_panel_frame, text="+0.01", command=lambda: self.changeFactor(0.01), height=2, width=5)
        raise3Button.grid(row=1, column=7, sticky=E, pady=3, padx=3)
        raise4Button = Button(self.control_panel_frame, text="+0.1", command=lambda: self.changeFactor(0.1), height=2, width=5)
        raise4Button.grid(row=1, column=8, sticky=E, pady=3, padx=3)
        raise5Button = Button(self.control_panel_frame, text="+1", command=lambda: self.changeFactor(1), height=2, width=5)
        raise5Button.grid(row=1, column=9, sticky=E, pady=3, padx=3)

        # Draw all other dots.
        if not self.zoom_entry.get():
            self.zoom = 0.5
        else:
            self.zoom = float(self.zoom_entry.get())
        if not self.num_of_dots_entry.get():
            self.num_of_dots = 200
        else:
            self.num_of_dots = int(self.num_of_dots_entry.get())
        self.radius = self.dot_size
        self.alpha = 0
        if not self.factor_entry.get():
            self.factor = 1
            self.factor_string_val.set(str(self.factor))    # update factor label
        else:
            self.factor = float(self.factor_entry.get())
            self.factor_string_val.set(str(self.factor))    # update factor label
        if not self.layers_entry.get():
            self.repeat = 1
        else:
            self.repeat = int(self.layers_entry.get())
        if not self.layers_factor_entry.get():
            self.dif_factor_between_layers = 0
        else:
            self.dif_factor_between_layers = float(self.layers_factor_entry.get())

        # get dots position and draw them "repeat" times (first run).
        self.dots_locations = []
        self.dots_locations = self.repeatedDotsLocationVector(self.repeat)
        self.dots_list = self.draw_dots(self.dots_locations)

        self.dots_window.mainloop()

    def repeatedDotsLocationVector(self, repeat):
        dots_list = []
        for i in range(repeat):
            dots_list.extend(self.dots_location_vector(self.num_of_dots))
            self.factor += self.dif_factor_between_layers
        self.factor -= repeat*self.dif_factor_between_layers
        return dots_list

    def changeFactor(self, num):
        deleteDots(self.canvas, self.dots_list)
        self.factor += num
        self.factor_string_val.set(str(self.factor))  # update factor label
        # RESTART SELF STATS
        self.alpha = 0
        self.radius = self.dot_size

        self.dots_locations = []
        self.dots_locations = self.repeatedDotsLocationVector(self.repeat)
        self.dots_list = self.draw_dots(self.dots_locations)


    def dots_location_vector(self, num_of_dots):
        dots_vector = []
        for x in range(num_of_dots):
            self.radius += self.zoom
            self.alpha += 2*math.pi*self.factor
            self.new_dot_x = self.starting_dot_x + self.radius*math.cos(self.alpha)
            self.new_dot_y = self.starting_dot_y + self.radius*(math.sin(self.alpha))
            dots_vector.append((self.new_dot_x, self.new_dot_y))
        return dots_vector

    def draw_dots(self, dots_vector):
        dots_list = []
        for dot in range(len(dots_vector)):
            x = dots_vector[dot][0]
            y = dots_vector[dot][1]
            # colors = ["pink","blue","purple","yellow","green","red"]
            # randNum = int(random()*6)-1
            # color = colors[randNum]
            # dot = self.canvas.create_oval(x, y, x + self.dot_size, y + self.dot_size, fill=color)
            dot = self.canvas.create_oval(x, y, x + self.dot_size, y + self.dot_size, fill="yellow")
            dots_list.append(dot)
        return dots_list


def deleteDots(canvas, dots_list):
    for i in range(len(dots_list)):
        canvas.delete(dots_list[i])


if __name__ == '__main__':
    flowers_root = Tk()
    words_gui = FlowersGui(flowers_root)
    flowers_root.mainloop()
