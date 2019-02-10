# rows = [
#     {'fname': 'Brian', 'lname': 'Jones', 'uid': 1},
#     {'fname': 'Dacid', 'lname': 'Bee', 'uid': 7},
#     {'fname': 'Jone', 'lname': 'Cleece', 'uid': 5},
#     {'fname': 'Big', 'lname': 'Jones', 'uid': 3}
# ]
# from operator import itemgetter
 
# rows_by_fname = sorted(rows, key=itemgetter('fname'))
 
# print(rows_by_fname)

from tkinter import *
root=Tk()
frame=Frame(root,width=300,height=300)
frame.grid(row=0,column=0)
canvas=Canvas(frame,bg='#FFFFFF',width=300,height=300,scrollregion=(0,0,500,500))
hbar=Scrollbar(canvas,orient=HORIZONTAL)
hbar.pack(side=BOTTOM,fill=X)
hbar.config(command=canvas.xview)
vbar=Scrollbar(canvas,orient=VERTICAL)
vbar.pack(side=RIGHT,fill=Y)
vbar.config(command=canvas.yview)
canvas.config(width=300,height=300)
canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
canvas.pack(side=LEFT,expand=True,fill=BOTH)

root.mainloop()