from tkinter import*
from tkinter import messagebox

# checker functiom
i =TRUE
def checker(buttons):
    global i
    if buttons['text'] == '':
        if(i):
            i=FALSE
            buttons['text']='X'
            winner()
        else:
            i=TRUE
            buttons['text']='O'
            winner()


def Reset():
    btn1['text'] = ''
    btn2['text'] = ''
    btn3['text'] = ''
    btn4['text'] = ''
    btn5['text'] = ''
    btn6['text'] = ''
    btn7['text'] = ''
    btn8['text'] = ''
    btn9['text'] = ''

# after press the reset button change the color
    btn1.configure(bg='gainsboro')
    btn2.configure(bg='gainsboro')
    btn3.configure(bg='gainsboro')

    btn4.configure(bg='gainsboro')
    btn5.configure(bg='gainsboro')
    btn6.configure(bg='gainsboro')

    btn7.configure(bg='gainsboro')
    btn8.configure(bg='gainsboro')
    btn9.configure(bg='gainsboro')

# check winner
def winner():
    if( btn1['text']=='X' and  btn2['text']=='X' and  btn3['text']=='X'):
        btn1.configure(bg='powder blue')
        btn2.configure(bg='powder blue')
        btn3.configure(bg='powder blue')

        messagebox.showinfo("Congratuation!!!",'X is Winner' )

    elif( btn1['text']=='X' and  btn4['text']=='X' and  btn7['text']=='X' ):
        btn1.configure(bg='powder blue')
        btn4.configure(bg='powder blue')
        btn7.configure(bg='powder blue')

        messagebox.showinfo("Congratuation!!!",'X is Winner' )

    elif( btn1['text']=='X' and  btn5['text']=='X' and  btn9['text']=='X' ):
        btn1.configure(bg='powder blue')
        btn5.configure(bg='powder blue')
        btn9.configure(bg='powder blue')

        messagebox.showinfo("Congratuation!!!",'X is Winner' )

    elif( btn4['text']=='X' and  btn5['text']=='X' and  btn6['text']=='X' ):
        btn4.configure(bg='powder blue')
        btn5.configure(bg='powder blue')
        btn6.configure(bg='powder blue')

        messagebox.showinfo("Congratuation!!!",'X is Winner' )

    elif( btn7['text']=='X' and  btn8['text']=='X' and  btn9['text']=='X' ):
        btn7.configure(bg='powder blue')
        btn8.configure(bg='powder blue')
        btn9.configure(bg='powder blue')

        messagebox.showinfo("Congratuation!!!",'X is Winner' )

    elif( btn3['text']=='X' and  btn6['text']=='X' and  btn9['text']=='X' ):
        btn3.configure(bg='powder blue')
        btn6.configure(bg='powder blue')
        btn9.configure(bg='powder blue')

        messagebox.showinfo("Congratuation!!!",'X is Winner' )

    elif( btn3['text']=='X' and  btn5['text']=='X' and  btn7['text']=='X' ):
        btn3.configure(bg='powder blue')
        btn5.configure(bg='powder blue')
        btn7.configure(bg='powder blue')

        messagebox.showinfo("Congratuation!!!",'X is Winner' )

    elif( btn2['text']=='X' and  btn5['text']=='X' and  btn8['text']=='X' ):
        btn2.configure(bg='powder blue')
        btn5.configure(bg='powder blue')
        btn8.configure(bg='powder blue')

        messagebox.showinfo("Congratuation!!!",'X is Winner' )

# Logic for player O

    elif( btn1['text']=='O' and  btn2['text']=='O' and  btn3['text']=='O'):
        btn1.configure(bg='powder blue')
        btn2.configure(bg='powder blue')
        btn3.configure(bg='powder blue')

        messagebox.showinfo("Congratuation !!!",'O is Winner' )

    elif( btn1['text']=='O' and  btn4['text']=='O' and  btn7['text']=='O' ):
        btn1.configure(bg='powder blue')
        btn4.configure(bg='powder blue')
        btn7.configure(bg='powder blue')

        messagebox.showinfo("Congratuation !!!",'O is Winner' )

    elif( btn1['text']=='O' and  btn5['text']=='O' and  btn9['text']=='O' ):
        btn1.configure(bg='powder blue')
        btn5.configure(bg='powder blue')
        btn9.configure(bg='powder blue')

        messagebox.showinfo("Congratuation !!!",'O is Winner' )

    elif( btn4['text']=='O' and  btn5['text']=='O' and  btn6['text']=='O' ):
        btn4.configure(bg='powder blue')
        btn5.configure(bg='powder blue')
        btn6.configure(bg='powder blue')

        messagebox.showinfo("Congratuation !!!",'O is Winner' )

    elif( btn7['text']=='O' and  btn8['text']=='O' and  btn9['text']=='O' ):
        btn7.configure(bg='powder blue')
        btn8.configure(bg='powder blue')
        btn9.configure(bg='powder blue')

        messagebox.showinfo("Congratuation !!!",'O is Winner' )

    elif( btn3['text']=='O' and  btn6['text']=='O' and  btn9['text']=='O' ):
        btn3.configure(bg='powder blue')
        btn6.configure(bg='powder blue')
        btn9.configure(bg='powder blue')

        messagebox.showinfo("Congratuation !!!",'O is Winner' )

    elif( btn3['text']=='O' and  btn5['text']=='O' and  btn7['text']=='O' ):
        btn3.configure(bg='powder blue')
        btn5.configure(bg='powder blue')
        btn7.configure(bg='powder blue')

        messagebox.showinfo("Congratuation !!!",'O is Winner' )

    elif( btn2['text']=='O' and  btn5['text']=='O' and  btn8['text']=='O' ):
        btn2.configure(bg='powder blue')
        btn5.configure(bg='powder blue')
        btn8.configure(bg='powder blue')

        messagebox.showinfo("Congratuation !!!",'O is Winner' )


# Logic for if both player are not winner
    elif(btn1['text']!='' and btn2['text']!='' and btn3['text']!='' and btn4['text']!='' and btn5['text']!='' and btn6['text']!='' and btn7['text']!='' and btn8['text']!='' and btn9['text']!=''):

        messagebox.showinfo("Game says:" ,"No One Wins , please reset the game")
        Reset()




root = Tk()
root.title("Tic Tac Toe")
root.configure(bg='powder blue')
root.resizable(0,0)
root.geometry('535x600+200+100')

mainframe = Frame(root,height=450,width=600)
mainframe.place(x=0,y=0)

btn1= Button(mainframe,text='',font=('times',26,'bold'),height=3,width=8,bg='gainsboro',command=lambda:checker(btn1))
btn1.grid(row=0,column=0)

btn2= Button(mainframe,text='',font=('times',26,'bold'),height=3,width=8,bg='gainsboro',command=lambda:checker(btn2))
btn2.grid(row=0,column=1)

btn3= Button(mainframe,text='',font=('times',26,'bold'),height=3,width=8,bg='gainsboro',command=lambda:checker(btn3))
btn3.grid(row=0,column=2)

btn4= Button(mainframe,text='',font=('times',26,'bold'),height=3,width=8,bg='gainsboro',command=lambda:checker(btn4))
btn4.grid(row=1,column=0)

btn5= Button(mainframe,text='',font=('times',26,'bold'),height=3,width=8,bg='gainsboro',command=lambda:checker(btn5))
btn5.grid(row=1,column=1)

btn6= Button(mainframe,text='',font=('times',26,'bold'),height=3,width=8,bg='gainsboro',command=lambda:checker(btn6))
btn6.grid(row=1,column=2)

btn7= Button(mainframe,text='',font=('times',26,'bold'),height=3,width=8,bg='gainsboro',command=lambda:checker(btn7))
btn7.grid(row=2,column=0)

btn8= Button(mainframe,text='',font=('times',26,'bold'),height=3,width=8,bg='gainsboro',command=lambda:checker(btn8))
btn8.grid(row=2,column=1)

btn9= Button(mainframe,text='',font=('times',26,'bold'),height=3,width=8,bg='gainsboro',command=lambda:checker(btn9))
btn9.grid(row=2,column=2)


# Reset Button
reset_btn = Button(root,text='Reset', font=('Arial',15,'bold'),height=2,width=20,bg='gainsboro',command=Reset)

reset_btn.place(x=120,y=500)

root.mainloop()