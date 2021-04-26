import tkinter
import tkinter as tk
import random

# initialize window
window = tk.Tk()
window.title('D&D Roller')
window.config(bg='lightgray')

# create dice class
class Dice:
    def __init__(self, sides):
        """Initializes each Dice class with sides, name, number to roll & drop, a frame, a label, buttons, etc."""
        self.sides = sides
        self.name = 'D' + str(sides)
        self.num_roll = 0
        self.num_drop = 0
        self.frame = tk.Frame(master=window, relief=tk.RIDGE, borderwidth=5)
        self.label = tk.Label(master=self.frame, text=f'{self.name}', font=('default', font_size, 'bold'), width=lbl_width, height=int(lbl_height/4))
        self.ent_roll = tk.Entry(master=self.frame, width=lbl_width, font=('default', font_size), justify='center')
        self.btn_roll_up = tk.Button(master=self.frame, text='+', font=('default', font_size), width=lbl_width, height=int(lbl_height/2),
                                     command=lambda: self.increase('roll', self.ent_roll))
        self.btn_roll_down = tk.Button(master=self.frame, text='-', font=('default', font_size), width=lbl_width, height=int(lbl_height/2),
                                       command=lambda: self.decrease(self.num_roll, self.ent_roll))
        self.drop_state = tkinter.BooleanVar(False)
        self.chk_drop = tk.Checkbutton(master=self.frame, text='Drop', variable=self.drop_state)
        self.ent_drop = tk.Entry(master=self.frame, width=lbl_width, font=('default', font_size), justify='center')
        self.btn_drop_up = tk.Button(master=self.frame, text='+', font=('default', 10), command=lambda: self.increase(self.num_drop, self.ent_drop))
        self.btn_drop_down = tk.Button(master=self.frame, text='-', font=('default', 10), command=lambda: self.decrease(self.num_drop, self.ent_drop))

    def zero(self, setting, entry):
        """Zeroes the given Dice number (to roll or drop) and the given tkinter entry object"""
        entry.delete(0, tk.END)
        entry.insert(0, 0)
        if setting == 'roll':
            self.num_roll = 0
        if setting == 'drop':
            self.num_drop = 0
    def increase(self, setting, entry):
        """Increases the given number to roll (or drop) and the related entry by one"""
        entry_text = entry.get()
        if entry_text == '':
            entry_text = 0
        try:
            entry_text = int(entry_text)
            if entry_text >= 0:
                entry_text += 1
                num = entry_text
                entry.delete(0, tk.END)
                entry.insert(0, entry_text)
                if setting == 'roll':
                    self.num_roll = num
                elif setting == 'drop':
                    self.num_drop = num
            else:
                self.zero(setting, entry)
        except:
            self.zero(setting, entry)
    def decrease(self, setting, entry):
        """Decreases the given number to roll (or drop) and the related entry by one"""
        entry_text = entry.get()
        try:
            entry_text = int(entry_text)
            if entry_text > 0:
                entry_text -= 1
                num = entry_text
                entry.delete(0, tk.END)
                entry.insert(0, entry_text)
                if setting == 'roll':
                    self.num_roll = num
                elif setting == 'drop':
                    self.num_drop = num
            else:
                self.zero(setting, entry)
        except:
            self.zero(setting, entry)

# set up label widths and heights, font size, and row and column indexes
lbl_width = 10
lbl_height = 4
row_index = 0
column_index = 0
font_size = 10

# create all Dice objects
all_dice = [D2, D4, D6, D8, D10, D12, D20] = Dice(2), Dice(4), Dice(6), Dice(8), Dice(10), Dice(12), Dice(20)

# frm_d2 = tk.Frame(master=window, relief=tk.RIDGE, borderwidth=5)
# frm_d2.grid(row=0, column=0)
#
# lbl_d2 = tk.Label(master=frm_d2, text='D2', font=('default', 20, 'bold'), width=lbl_width, height=int(lbl_height/4))
# lbl_d2.pack(side=tk.TOP)
#
# ent_d2 = tk.Entry(master=frm_d2, width=lbl_width, font=('default', 20), justify='center')
# ent_d2.pack(side=tk.LEFT)
#
# btn_d2_up = tk.Button(master=frm_d2, text='+', font=('default', 20), width=lbl_width, height=int(lbl_height/2), command=lambda: D2.increase(ent_d2))
# btn_d2_up.pack(side=tk.TOP)
# btn_d2_down = tk.Button(master=frm_d2, text='-', font=('default', 20), width=lbl_width, height=int(lbl_height/2), command=lambda: D2.decrease(ent_d2))
# btn_d2_down.pack(side=tk.TOP)

def zero_all():
    """Zeroes all dice (to roll and to drop)"""
    for dice in all_dice:
        dice.zero('roll', dice.ent_roll)
        dice.zero('drop', dice.ent_drop)

# Pack all dice and buttons
for dice in all_dice:
    dice.frame.grid(row=row_index, column=column_index)

    dice.label.pack(side=tk.TOP)

    dice.ent_roll.pack(side=tk.LEFT)

    dice.btn_roll_up.pack(side=tk.TOP)

    dice.btn_roll_down.pack(side=tk.TOP)

    dice.chk_drop.pack(side=tk.LEFT)

    dice.btn_drop_down.pack(side=tk.RIGHT)
    dice.btn_drop_up.pack(side=tk.RIGHT)
    dice.ent_drop.pack(side=tk.RIGHT)

    row_index += 1

# set up a display window for results
frm_results = tk.Frame(master=window, relief=tk.RIDGE, borderwidth=5)
frm_results.grid(row=0, column=1, rowspan=7)

lbl_results = tk.Label(master=frm_results, text='', height=68, width=40)
lbl_results.pack(expand=True, fill='both')

def roll_all():
    """Rolls all dice, dropping the appropriate amount for each, and sends the total to the results label"""
    grand_total = 0
    for dice in all_dice:
        num_roll = dice.ent_roll.get()
        num_drop = dice.ent_drop.get()
        try:
            num_roll = int(num_roll)
            if num_roll < 0:
                num_roll = 0
        except:
            num_roll = 0
        dice.num_roll = num_roll
        try:
            num_drop = int(num_drop)
            if num_drop < 0:
                num_drop = 0
            elif num_drop > num_roll:
                num_drop = num_roll
        except:
            num_drop = 0
        dice.num_drop = num_drop
        # print(num_roll, num_drop)

        if dice.num_roll > 0:
            rolls = []
            total = 0
            for i in range(dice.num_roll):
                roll = random.randrange(1, dice.sides + 1)
                rolls.append(roll)
            rolls = sorted(rolls, reverse=True)
            # print(rolls)
            if dice.drop_state.get() == True:
                for roll in rolls[0: len(rolls)-dice.num_drop]:
                    total += roll
                # print(total)
            else:
                for roll in rolls:
                    total += roll
            grand_total += total
    lbl_results['text'] = grand_total

# Sets up the frame holding the calc and zero all buttons
frm_zerocalc = tk.Button(master=window)
frm_zerocalc.grid(row=row_index, column=0, columnspan=2)

# Sets up and packs the calc button
btn_calc = tk.Button(master=frm_zerocalc, text='Calculate', font=('default', 10, 'bold'), command=roll_all)
btn_calc.pack(side=tk.LEFT)

# Sets up and packs the zero all button
btn_zero = tk.Button(master=frm_zerocalc, text='0 all', font=('default', 10), command=zero_all)
btn_zero.pack(side=tk.LEFT)


window.mainloop()
