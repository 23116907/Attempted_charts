import tkinter as tk

import tksheet

top = tk.Tk()
top_left_fg = tk.Tk()
top_right_bg = tk.Tk()
sheet1 = tksheet.Sheet(top)
sheet2 = tksheet.Sheet(top_left_fg)
sheet3 = tksheet.Sheet(top_left_fg)
sheet4 = tksheet.Sheet(top_right_bg)

sheet1.grid()
sheet2.grid()
sheet3.grid()
sheet4.grid()


sheet1.set_sheet_data([[f"{ri+cj}" for cj in range(3)] for ri in range(5)])
sheet2.set_sheet_data([[f"{ri+cj}" for cj in range(1)] for ri in range(4)])
sheet3.set_sheet_data([[f"{ri+cj}" for cj in range(1)] for ri in range(4)])
sheet4.set_sheet_data([[f"{ri+cj}" for cj in range(1)] for ri in range(1)])

# table enable choices listed below:

top.mainloop()





