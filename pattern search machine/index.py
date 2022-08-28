from tkinter import *

win = Tk()
win.title("Pattern Search Machine")
win.maxsize(width=400,height=400)
win.geometry('400x400')
bg = StringVar()
def changeBgColor():
    win.configure(background=bg.get())
bnc = StringVar()
def changeBannerColor():
    heading = Label(win,text="Welcome to Pattern Search Machine!",bg=bnc.get(),padx=30,pady=15,fg="white",bd=12)
    heading.place(x=50,y=10)
    btn = Button(win,text='Search', bg=bnc.get() , fg='white',width=30,command=searchFunc)
    btn.place(x=90,y=180)

    

themeMenu = Menu(win)
win.config(menu=themeMenu)
bgMenu = Menu(themeMenu)

themeMenu.add_cascade(label='background',menu=bgMenu)
bgMenu.add_radiobutton(label='cyan',command=changeBgColor, variable=bg ,value='cyan')
bgMenu.add_radiobutton(label='black',command=changeBgColor ,variable= bg ,value='black')
bgMenu.add_radiobutton(label='gray',command=changeBgColor ,variable= bg ,value='gray')
bgMenu.add_radiobutton(label='dark cyan',command=changeBgColor ,variable= bg ,value='#004958')
bgMenu.add_radiobutton(label='blue v2',command=changeBgColor ,variable= bg ,value='#302b63')


bannerMenu = Menu(themeMenu)
themeMenu.add_cascade(label='banner color',menu=bannerMenu)
bannerMenu.add_radiobutton(label='blue',command=changeBannerColor , variable=bnc , value='blue')
bannerMenu.add_radiobutton(label='green',command=changeBannerColor , variable=bnc , value='green')
bannerMenu.add_radiobutton(label='green v2',command=changeBannerColor , variable=bnc , value='light green')
bannerMenu.add_radiobutton(label='black',command=changeBannerColor , variable=bnc , value='black')
bannerMenu.add_radiobutton(label='gray',command=changeBannerColor , variable=bnc , value='gray')
bannerMenu.add_radiobutton(label='black v2',command=changeBannerColor , variable=bnc , value='#203A43')


#logical function


NO_OF_CHARS = 256

def getNextState(pat, M, state, x):
	'''
	calculate the next state
	'''

	# If the character c is same as next character
	# in pattern, then simply increment state

	if state < M and x == ord(pat[state]):
		return state+1

	i=0
	# ns stores the result which is next state

	# ns finally contains the longest prefix
	# which is also suffix in "pat[0..state-1]c"

	# Start from the largest possible value and
	# stop when you find a prefix which is also suffix
	for ns in range(state,0,-1):
		if ord(pat[ns-1]) == x:
			while(i<ns-1):
				if pat[i] != pat[state-ns+1+i]:
					break
				i+=1
			if i == ns-1:
				return ns
	return 0

def computeTF(pat, M):
	'''
	This function builds the TF table which
	represents Finite Automata for a given pattern
	'''
	global NO_OF_CHARS

	TF = [[0 for i in range(NO_OF_CHARS)]\
		for _ in range(M+1)]

	for state in range(M+1):
		for x in range(NO_OF_CHARS):
			z = getNextState(pat, M, state, x)
			TF[state][x] = z

	return TF

def search(pat, txt,res =''):    
	'''
	Prints all occurrences of pat in txt
	'''
	global NO_OF_CHARS
	M = len(pat)
	N = len(txt)
	TF = computeTF(pat, M)


	# Process txt over FA.
	state=0
	for i in range(N):
		state = TF[state][ord(txt[i])]
		if state == M:
			res+=("Pattern found at index: {} \n".\
				format(i-M+1))
	return res;





#function

def searchFunc():
    pat = patternInp.get()
    strInp = stringInp.get()
    lbl3.config(text=search(pat,strInp))
    print(search(pat,strInp))
    
    

if  bnc.get():
    pass
else:
    heading = Label(win,text="Welcome to Pattern Search Machine!",bg='#203A43',padx=30,pady=15,fg="white",bd=12)
    heading.place(x=50,y=10)

lbl1 = Label(win,text='Enter String : ')
lbl1.place(x=30,y=90);

stringInp = StringVar()
string1Text = Entry(win,width=34,bd=4,textvariable=stringInp)
string1Text.place(x=110,y=90)

lbl2 = Label(win,text='Enter pattern : ')
lbl2.place(x=30,y=140);

patternInp = StringVar()
string2Text = Entry(win,width=34,bd=4,textvariable=patternInp)
string2Text.place(x=110,y=140)

if bnc.get():
    pass
else:
    btn = Button(win,text='Search', bg='#203A43' , fg='white',width=30,command=searchFunc)
    btn.place(x=90,y=180)


lbl3 = Label(win,text='')
lbl3.place(x=90,y=220)



win.mainloop()