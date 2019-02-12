import tkinter

import tkinter.messagebox

import tkinter.simpledialog


btnList = []


# 动态创建组件，并计算组件在窗体上的位置

def place(n):

    for i in range(n):

        exec('btn'+str(i)+'=tkinter.Button(root,text='+str(i)+')')

        eval('btn'+str(i)).place(x=80, y=10+i*30, width=60, height=20)

        btnList.append(eval('btn'+str(i)))

    root.geometry('200x'+str((n)*30+70)+'+400+300')

    return n*30 + 10


# 创建tkinter应用程序

root = tkinter.Tk()

# 窗口标题

root.title('动态创建组件')

# 窗口初始大小和位置

root.geometry('200x180+400+300')

# 不允许改变窗口大小

root.resizable(False, False)


# 增加按钮的按钮

def btnSetClick():

    n = tkinter.simpledialog.askinteger(title='输入一个整数',

                                        prompt='想动态增加几个按钮：',

                                        initialvalue=3)

    if n and n>0:

        startY = place(n)

        modify(startY)

        # 根据需要禁用和启用“增加按钮”和“清空按钮”

        btnSet['state'] = 'disabled'

        btnClear['state'] = 'normal'

btnSet = tkinter.Button(root, text='增加按钮',command=btnSetClick)


def btnClearClick():

    global btnList

    # 删除动态创建的按钮

    for btn in btnList:

        btn.destroy()

    btnList = []

    modify(20)

    btnClear['state'] = 'disabled'

    btnSet['state'] = 'normal'

btnClear = tkinter.Button(root,text='清空按钮',command=btnClearClick)

# 默认处于禁用状态

btnClear['state'] = 'disabled'


# 动态调整“增加按钮”和“清空按钮”的位置

def modify(startY):

    btnSet.place(x=10, y=startY, width=80, height=20)

    btnClear.place(x=100, y=startY, width=80, height=20)

modify(20)


root.mainloop()