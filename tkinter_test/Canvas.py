import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

canvas = tk.Canvas(window, bg='blue', height=100, width=200)
image_file = tk.PhotoImage(file=r'C:\Users\user\Desktop\test_files\ins.gif')
image = canvas.create_image(10, 10, anchor='nw', image=image_file)
#里面的参数10,10就是图片放入画布的坐标,anchor=nw则是把图片的左上角作为锚定点
x0, y0, x1, y1= 50, 50, 80, 80
line = canvas.create_line(x0, y0, x1, y1)
#实现的是画一条直线，后面()中给的参数就是线段两点的坐标
oval = canvas.create_oval(x0, y0, x1, y1, fill='red')
#创建一个圆，填充色为`red`红色
arc = canvas.create_arc(x0+30, y0+30, x1+30, y1+30, start=0, extent=180)
#创建一个扇形
rect = canvas.create_rectangle(100, 30, 100+20, 30+20)
#创建一个矩形
canvas.pack()

def moveit():
    canvas.move(rect, 0, 2)#0和2，也就是横坐标移动0个单位，纵坐标移动2个单位

b = tk.Button(window, text='move', command=moveit).pack()


window.mainloop()