#imports
import sys,os,shutil,ctypes
from zipfile import ZipFile
from tkinter import EXCEPTION, Tk,messagebox,ttk,PhotoImage,filedialog

#Define
def Menu(args): #This runs when you select a number
    global img1
    global img2
    global zval
    global nam
    global pre
    if os.path.exists(f'{args}.zip'):
        zval=args
        try:
            with ZipFile(f'{args}.zip') as z:
                z.extract('preview.png',path=None,pwd=None)
            img2=PhotoImage(file=opath+'/Files/preview.png')
            pre.config(image=img2)
            os.remove(opath+'/Files/preview.png')
        except:
            pre.config(image=img1)
        try:
            with ZipFile(f'{args}.zip') as z:
                z.extract('name.txt',path=None,pwd=None)
            na=open(f"{opath}/Files/name.txt","r")
            name=na.readline()
            na.close()
        except Exception:
            name=None
        finally:
            nam.config(text=name)
            os.remove(opath+'/Files/name.txt')
    else:
        nam.config(text='No File')
        pre.config(image=img1)

def Swap(args):
    archive = ZipFile(f'{args}.zip')
    for archive_item in archive.namelist():
        if archive_item.startswith('Tex/'):
            archive.extract(archive_item,'temp/')
    try:
        shutil.rmtree(f'{fn}/Plugin/GFX/GLideN64/hires_texture/SUPER MARIO 64/')
    except:
        print('RMTREE failed... Continuing')
    shutil.copytree('./temp/Tex/',f'{fn}/Plugin/GFX/GLideN64/hires_texture/SUPER MARIO 64/')
    shutil.rmtree('./temp')

def PgUp():
    global page
    page=page+1 #Go forwards a page
    pt.config(text=f'Page {page+1}')

def PgDn():
    global page
    if page != 0: #Go backwards a page unless it makes page a negative number
        page=page-1
    pt.config(text=f'Page {page+1}')

def Sel():
    global fn
    fn=filedialog.askdirectory(title="Select PJ64 Path",initialdir="..")
    if fn=='':
        messagebox.showerror("Error", "Please select a file")
        sys.exit()
    p.destroy()

opath=os.getcwd() #Store current working directory to var
page=0 #Set page to 0

#read PJ64 Location
try:
    pj64=open("pj64.txt", "r")
    fn=pj64.readline()
except: #If unable to read, then ask
    p=Tk()
    p.overrideredirect(1)
    p.eval('tk::PlaceWindow . center')
    p.tk.call('wm','iconphoto',p._w,PhotoImage(file=f'{opath}/icon.png'))
    p.title('Settings')
    ttk.Label(p,text="Please enter the path PJ64 is in to continue").pack()
    ttk.Button(p,text="Search",command=Sel).pack()
    p.mainloop()
    f=open("pj64.txt","x")
    f.write(fn)
    f.close()

#Go into ./Files/
try: #Detect if Files is a folder
    os.chdir('Files')
except FileNotFoundError: #Throw error if there is no Files folder
    messagebox.showerror(title="Error - No File",message='Please make a folder named "Files" in this directory')
    sys.exit()
except PermissionError: #Throw error if python does not have permissions to read Files folder
    messagebox.showerror(title="Error - No Permission",message='Cannot accsess Files folder!\nRun this program as administrator and see if it works then.')
    sys.exit()

#Initialize a window
T=Tk()
T.eval('tk::PlaceWindow . center')
T.tk.call('wm','iconphoto',T._w,PhotoImage(file=f'{opath}/icon.png'))
img1=PhotoImage(file=opath+'/nofile.png')
T.title('SMR')
tab=ttk.Notebook(T)
main=ttk.Frame(tab)
mah=ttk.Frame(main)
tab.add(main,text='SM Retexturing Program')
tab.grid(column=0,row=1)

#Left side of screen (Panel of buttons)
ttk.Label(main,text="Click any number!").grid(column=0,row=0)
ttk.Button(main,text='<',command=PgDn,width=3).grid(column=0,row=1,sticky='W')
pt=ttk.Label(main,text=f'Page {page+1}')
ttk.Button(main,text='>',command=PgUp,width=3).grid(column=0,row=1,sticky='E')
ttk.Button(main,text='1',command=lambda:Menu(1+(9*page)),width=3).grid(column=0,row=2,sticky='W')
ttk.Button(main,text='2',command=lambda:Menu(2+(9*page)),width=3).grid(column=0,row=2)
ttk.Button(main,text='3',command=lambda:Menu(3+(9*page)),width=3).grid(column=0,row=2,sticky='E')
ttk.Button(main,text='4',command=lambda:Menu(4+(9*page)),width=3).grid(column=0,row=3,sticky='W')
ttk.Button(main,text='5',command=lambda:Menu(5+(9*page)),width=3).grid(column=0,row=3)
ttk.Button(main,text='6',command=lambda:Menu(6+(9*page)),width=3).grid(column=0,row=3,sticky='E')
ttk.Button(main,text='7',command=lambda:Menu(7+(9*page)),width=3).grid(column=0,row=4,sticky='W')
ttk.Button(main,text='8',command=lambda:Menu(8+(9*page)),width=3).grid(column=0,row=4)
ttk.Button(main,text='9',command=lambda:Menu(9+(9*page)),width=3).grid(column=0,row=4,sticky='E')
ttk.Button(main,text='Reset',command=lambda:Menu(0)).grid(column=0,row=5)

#Right side of screen
pre=ttk.Button(mah,image=img1,command=lambda:Swap(zval))
nam=ttk.Label(mah,text='')

#Finish up
pre.pack()
nam.pack()
mah.grid(column=1,row=0,rowspan=5)
pt.grid(column=0,row=1)
T.mainloop()