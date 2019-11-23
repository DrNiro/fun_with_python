from tkinter import *
import random


class ChaosGui:
    def __init__(self, main_window):
        self.main_window = main_window
        self.main_window.title("Chaos Game")
        self.main_window.geometry("425x350")

        title_label = Label(self.main_window, text="Chaos Game", font=("Impact", 35))
        title_label.pack(side=TOP, pady=10)

        # starting points location
        self.dot_size = 3
        self.number_of_fractions = 2
        self.a_x_location = 300
        self.a_y_location = 50
        self.b_x_location = 20
        self.b_y_location = 550
        self.c_x_location = 550
        self.c_y_location = 550

        self.body_frame = Frame(self.main_window)
        self.body_frame.pack()
        control_frame = Frame(self.body_frame)
        control_frame.pack(side=TOP, padx=15)

        open_game_button = Button(control_frame, text="open canvas", command=self.openCanvas, height=2, width=9)
        open_game_button.pack(pady=5)
        next_dot_button = Button(control_frame, text="Next Dot", command=self.nextDot, height=2, width=9)
        next_dot_button.pack(pady=5)
        many_dots_button = Button(control_frame, text="Many Dots", command=self.manyDots, height=2, width=9)
        many_dots_button.pack(pady=5)

        # settings frame
        footer_frame = Frame(self.body_frame)
        footer_frame.pack(side=BOTTOM)
        change_dots_location_button = Button(footer_frame, text="Change start locations", command=self.change_start_location)
        change_dots_location_button.pack(pady=15)

    def change_start_location(self):
        self.change_location_window = Tk()
        self.change_location_window.title("Change starting points location")
        self.change_location_window.geometry("350x275")
        title_label = Label(self.change_location_window, text="Change location", width=20, font=("Impact", 20), pady=10)
        title_label.pack()

        chg_loc_frame = Frame(self.change_location_window)
        chg_loc_frame.pack()

        x_label = Label(chg_loc_frame, text="X Value", font="Times 10 underline")
        x_label.grid(row=0, column=1, pady=5, padx=5)
        y_label = Label(chg_loc_frame, text="Y Value", font="Times 10 underline")
        y_label.grid(row=0, column=2, pady=5, padx=5)

        a_label = Label(chg_loc_frame, text="Point A:")
        a_label.grid(row=1, sticky=E, pady=5, padx=5)
        self.a_entry_x = Entry(chg_loc_frame)
        self.a_entry_x.grid(row=1, column=1, sticky=E, pady=5, padx=5)
        self.a_entry_y = Entry(chg_loc_frame)
        self.a_entry_y.grid(row=1, column=2, sticky=E, pady=5, padx=5)

        b_label = Label(chg_loc_frame, text="Point B:")
        b_label.grid(row=2, sticky=E, pady=5, padx=5)
        self.b_entry_x = Entry(chg_loc_frame)
        self.b_entry_x.grid(row=2, column=1, sticky=E, pady=5, padx=5)
        self.b_entry_y = Entry(chg_loc_frame)
        self.b_entry_y.grid(row=2, column=2, sticky=E, pady=5, padx=5)

        c_label = Label(chg_loc_frame, text="Point C:")
        c_label.grid(row=3, sticky=E, pady=5, padx=5)
        self.c_entry_x = Entry(chg_loc_frame)
        self.c_entry_x.grid(row=3, column=1, sticky=E, pady=5, padx=5)
        self.c_entry_y = Entry(chg_loc_frame)
        self.c_entry_y.grid(row=3, column=2, sticky=E, pady=5, padx=5)

        change_loc_button = Button(self.change_location_window, text="Change", command=self.change_loc, pady=10, padx=10)
        change_loc_button.pack(pady=15)

        self.change_location_window.mainloop()

    def change_loc(self):
        good_vals = True
        ax = int(self.a_entry_x.get())
        ay = int(self.a_entry_y.get())
        bx = int(self.b_entry_x.get())
        by = int(self.b_entry_y.get())
        cx = int(self.c_entry_x.get())
        cy = int(self.c_entry_y.get())

        lst = [ax, ay, bx, by, cx, cy]
        if not all(map(lambda x: type(x) == int, lst)):
            good_vals = False
            print("All values must be integers.")
        if ay > by or ay > cy:
            good_vals = False
            print("Point A's 'Y' value must be lower than point B's or C's 'Y' value")
        if good_vals:
            self.a_x_location = ax
            self.a_y_location = ay
            self.b_x_location = bx
            self.b_y_location = by
            self.c_x_location = cx
            self.c_y_location = cy
            print("Values changed successfully")

    def openCanvas(self):
        canvas_window = Tk()
        self.canvas_width = 600
        self.canvas_height = 600
        canvas_window.title("Chaos Game")

        self.canvas = Canvas(canvas_window, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack(expand=YES, fill=BOTH)

        # Points Location
        self.pin_point_A = [self.a_x_location, self.a_y_location]
        self.pin_point_B = [self.b_x_location, self.b_y_location]
        self.pin_point_C = [self.c_x_location, self.c_y_location]
        # Create fixed starting points
        self.canvas.create_oval(self.pin_point_A[0], self.pin_point_A[1], self.pin_point_A[0] + 7,
                                self.pin_point_A[1] + 7, fill='black')
        self.canvas.create_oval(self.pin_point_B[0], self.pin_point_B[1], self.pin_point_B[0] + 7,
                                self.pin_point_B[1] + 7, fill='black')
        self.canvas.create_oval(self.pin_point_C[0], self.pin_point_C[1], self.pin_point_C[0] + 7,
                                self.pin_point_C[1] + 7, fill='black')
        # Add text - A, B, C
        self.canvas.create_text(self.pin_point_A[0] + 5, self.pin_point_A[1] - 10, fill="black",
                                font="Times 15 bold", text="A")
        self.canvas.create_text(self.pin_point_B[0] + 3, self.pin_point_B[1] + 18, fill="black",
                                font="Times 15 bold", text="B")
        self.canvas.create_text(self.pin_point_C[0] + 5, self.pin_point_C[1] + 18, fill="black",
                                font="Times 15 bold", text="C")

        # Create a first random point within the shape
        self.current_x = 0
        self.current_y = 0
        self.current_x, self.current_y = self.drawRandomDotWithinParemiter()
        self.current_point = self.canvas.create_text(self.current_x + 5, self.current_y + 18, fill="black",
                                                     font="Times 10", text="Tracking point")
        canvas_window.mainloop()

    def rand_dot(self):
        x, y = self.drawRandomDotWithinParemiter()
        self.canvas.coords(self.current_point, x + 5, y + 18)

    def nextDot(self):
        choose_point = random.choice([1, 2, 3, 4, 5, 6])

        if choose_point == 1 or choose_point == 2:
            self.current_x = (self.current_x + self.pin_point_A[0]) / self.number_of_fractions
            self.current_y = (self.current_y + self.pin_point_A[1]) / self.number_of_fractions
        elif choose_point == 3 or choose_point == 4:
            self.current_x = (self.current_x + self.pin_point_B[0]) / self.number_of_fractions
            self.current_y = (self.current_y + self.pin_point_B[1]) / self.number_of_fractions
        elif choose_point == 5 or choose_point == 6:
            self.current_x = (self.current_x + self.pin_point_C[0]) / self.number_of_fractions
            self.current_y = (self.current_y + self.pin_point_C[1]) / self.number_of_fractions

        self.canvas.create_oval(self.current_x, self.current_y, self.current_x + self.dot_size, self.current_y + self.dot_size, fill='black')
        self.canvas.coords(self.current_point, self.current_x+5, self.current_y+18)

    def manyDots(self):
        for i in range(1000):
            self.nextDot()

    def fx(self, x, y1, m, x1):
        return y1 + m*(x-x1)

    def fy(self, y, x1, m, y1):
        return (y-y1 + m*x1)/m

    def drawRandomDotWithinParemiter(self):
        m_ab = (self.pin_point_A[1] - self.pin_point_B[1]) / (self.pin_point_A[0] - self.pin_point_B[0])
        m_ac = (self.pin_point_A[1] - self.pin_point_C[1]) / (self.pin_point_A[0] - self.pin_point_C[0])
        m_bc = (self.pin_point_B[1] - self.pin_point_C[1]) / (self.pin_point_B[0] - self.pin_point_C[0])

        x = random.choice(range(0, self.canvas_width))
        y = random.choice(range(0, self.canvas_height))

        while not (
                self.fy(y, self.pin_point_A[0], m_ab, self.pin_point_A[1]) <= x <= self.fy(y, self.pin_point_A[0],
                                                                                           m_ac,
                                                                                           self.pin_point_A[1])
                and y <= self.fx(x, self.pin_point_C[1], m_bc, self.pin_point_C[0])):
            x = random.choice(range(0, self.canvas_width))
            y = random.choice(range(0, self.canvas_height))

        self.canvas.create_oval(x, y, x + self.dot_size, y + self.dot_size, fill='black')
        return x, y


if __name__ == '__main__':
    chaos_root = Tk()
    words_gui = ChaosGui(chaos_root)
    chaos_root.mainloop()
