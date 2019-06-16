from tkinter import *
operator=''
def btn(number):
    global operator
    operator=operator+str(number)
    txt_input.set(operator)

def equal():
    global operator
    sumup=float(eval(operator))
    txt_input.set(sumup)
def clear():
    global operator
    operator=''
    txt_input.set('')
    Display.insert(0,'Start Calculating .....')
root=Tk()
root.title('Calculator')
txt_input=StringVar(value='Start Calculating.....')
#=======================================SCREEN===========================================================
Display=Entry(root,font=('arial',30,'bold'),fg='black',bg='red',justify='right',bd=10,textvariable=txt_input)
# root is which screen ,aerial is font of text ,fg is font background ,bg is background,bd is border size justify is for text to be justified 
Display.grid(columnspan=4)
# grid is to display the screen in grid
#=======================================ROW1================================================================
bt7=Button(root,padx=30,pady=15,bd=5,fg='black',font=('arial',30,'italic'),text='7',command=lambda:btn(7),bg='green').grid(row=1,column=0)
bt8=Button(root,padx=30,pady=15,bd=5,fg='black',font=('arial',30,'italic'),text='8',command=lambda:btn(8),bg='green').grid(row=1,column=1)
bt9=Button(root,padx=30,pady=15,bd=5,fg='black',font=('arial',30,'italic'),text='9',command=lambda:btn(9),bg='green').grid(row=1,column=2)
btC=Button(root,padx=30,pady=15,bd=5,fg='black',font=('arial',30,'italic'),text='C',command=clear,bg='blue').grid(row=1,column=3)
#===========================================ROW2====================================================================
bt4=Button(root,padx=30,pady=15,bd=5,fg='black',font=('arial',30,'italic'),text='4',command=lambda:btn(4),bg='green').grid(row=2,column=0)
bt5=Button(root,padx=30,pady=15,bd=5,fg='black',font=('arial',30,'italic'),text='5',command=lambda:btn(5),bg='green').grid(row=2,column=1)
bt6=Button(root,padx=30,pady=15,bd=5,fg='black',font=('arial',30,'italic'),text='6',command=lambda:btn(6),bg='green').grid(row=2,column=2)
btplus=Button(root,padx=36,pady=15,bd=5,fg='black',font=('arial',30,'italic'),text='+',command=lambda:btn('+'),bg='orange').grid(row=2,column=3)
#===========================================ROW3====================================================================
bt1=Button(root,padx=30,pady=15,bd=5,fg='black',font=('arial',30,'italic'),text='1',command=lambda:btn(1),bg='green').grid(row=3,column=0)
bt2=Button(root,padx=30,pady=15,bd=5,fg='black',font=('arial',30,'italic'),text='2',command=lambda:btn(2),bg='green').grid(row=3,column=1)
bt3=Button(root,padx=30,pady=15,bd=5,fg='black',font=('arial',30,'italic'),text='3',command=lambda:btn(3),bg='green').grid(row=3,column=2)
btminus=Button(root,padx=40,pady=15,bd=5,fg='black',font=('arial',30,'italic'),text='-',command=lambda:btn('-'),bg='orange').grid(row=3,column=3)
#========================================ROW4===================================================================
bt0=Button(root,padx=35,pady=15,bd=5,fg='black',font=('arial',30,'italic'),text='0',command=lambda:btn(0),bg='green').grid(row=4,column=0)
btdot=Button(root,padx=35,pady=15,bd=5,fg='black',font=('arial',30,'italic'),text='.',command=lambda:btn('.'),bg='green').grid(row=4,column=1)
btdivision=Button(root,padx=42,pady=15,bd=5,fg='black',font=('arial',30,'italic'),text='/',command=lambda:btn('/'),bg='orange').grid(row=4,column=2)
btmultiply=Button(root,padx=40,pady=15,bd=5,fg='black',font=('arial',30,'italic'),text='*',command=lambda:btn('*'),bg='orange').grid(row=4,column=3)
#===========================================ROW5===================================================================
btequal=Button(root,padx=90,pady=15,bd=5,fg='black',font=('arial',30,'italic'),text='=',command=equal,bg='orange').grid(row=5,column=0,columnspan=2)
btopenbrac=Button(root,padx=40,pady=15,bd=5,fg='black',font=('arial',30,'italic'),text='(',command=lambda:btn('('),bg='orange').grid(row=5,column=2)
btclosebrac=Button(root,padx=40,pady=15,bd=5,fg='black',font=('arial',30,'italic'),text=')',command=lambda:btn(')'),bg='orange').grid(row=5,column=3)
root.mainloop()
'''
from tkinter import *
root=Tk()
def cal():
    var3=var1.get()
    var4=var2.get()
    var5=var3*var4
    e3.insert(0,var5)
def clear():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
var1=IntVar()
var2=IntVar()
root.title('Area Calculator')
Label(text='Area Calculation',padx=50,font=('aerial',30,'bold')).grid(row=0,sticky=W)
Label(text='Height',padx=30,font=('aerial',30,'bold')).grid(row=1,sticky=W)
e1=Entry(width=30,textvariable=var1)
e1.grid(row=1,column=1)
Label(text='Length',padx=30,font=('aerial',30,'bold')).grid(row=2,sticky=W)
e2=Entry(width=30,textvariable=var2)
e2.grid(row=2,column=1)
Label(text='Area',padx=30,font=('aerial',30,'bold')).grid(row=3,sticky=W)
e3=Entry(width=30)
e3.grid(row=3,column=1)
Button(text='Calculate',padx =60,pady=20,fg='black',bg='red',command=cal).grid(row=4,column=0,sticky=W)
Button(text='Clear',fg='black',padx =60,pady=20,bg='red',command=clear).grid(row=4,column=1,sticky=E)



root.mainloop()'''