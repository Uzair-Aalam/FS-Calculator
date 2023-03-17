import tkinter as tk
from math import tan
from numpy import deg2rad
import tkinter.messagebox as MB
import tkinter.filedialog as FD
from snip1 import *
import snip5
import shutil #for move operation on file
import sys, os #imported for the resource_path()

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)





bgcolor2='grey'
bgcolor1='gray'
bgcolor3='Indianred'
Font1="Arial 80 bold"
Font2="Aerial 20 normal" 
Font3="Times 20 bold"


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.MainWindow()
    
    def MainWindow(self):
        self.geometry("1280x768+20+20")
        self.maxsize(1280,768)
        self.minsize(1280,768)
        self.title("FS Calculator")
        
        #-----------Upper Frame-----------------------------------
        upperFrame=tk.Frame(self,width=1280,height=150,bg=bgcolor2)
        upperFrame.pack()
        
        L1=tk.Label(upperFrame,text="FS Calculator",\
        font=Font1,fg="Black",bg=None)
        L1.pack()
        #-----------Upper Frame-----------------------------------
        
        #-----------Menu Bar--------------------------------------
        menubar=tk.Menu(self)        
        filemenu=tk.Menu(menubar)
        filemenu.add_command(label='Factor of Safety',command=self.Window1)
        filemenu.add_command(label='Sensitivity Analysis',command=self.Window2)
        filemenu.add_command(label='Exit',command=self.destroy)
        menubar.add_cascade(label='File',menu=filemenu)
        
        helpmenu=tk.Menu(menubar)
        helpmenu.add_command(label='About',command=self.About)
        helpmenu.add_command(label='Licence Info',command=self.Licence)
        menubar.add_cascade(label='Help',menu=helpmenu)
        self.config(menu=menubar)
        #-----------Menu Bar--------------------------------------
        
        #----------Lower Frame-----------------------------------
        lowerFrame=tk.Frame(self,width=1280,height=618,bg=bgcolor1)
        lowerFrame.pack()
        
        SF_Determin_Button=tk.Button(lowerFrame,text='Factor of Safety',font=Font2,bg=bgcolor1,command=self.Window1)
        SF_Determin_Button.place(x=570,y=200)
        
        SF_Determin_Button=tk.Button(lowerFrame,text='Sensitivity Analysis',font=Font2,bg=bgcolor1,command=self.Window2)
        SF_Determin_Button.place(x=550,y=300)
        
        ExitButton=tk.Button(lowerFrame,text="Exit",font=Font2,bg=bgcolor1,command=self.destroy)
        ExitButton.place(x=640,y=400)
        
        
        #self.im=tk.PhotoImage(file="./Pictures/M2.gif")
        #imgLabel=tk.Label(lowerFrame,image=self.im,bd=0)
        #imgLabel.place(x=600,y=0)
        #-----------Lower Frame-----------------------------------
        
        self.setIcon(self)
        
    def Window1(self):
        print('Window 1')
        window1=tk.Toplevel()
        window1.geometry("1280x768+20+20")
        #window1.maxsize(1280,768)
        #window1.minsize(1280,768)
        window1.title("FS Calculator")
        self.setIcon(window1)
        
        #----Upper Frame----------------------
        upperFrame=tk.Frame(window1,width=1280,height=150,bg=bgcolor2)
        upperFrame.pack()
        
        L1=tk.Label(upperFrame,text="Enter numerical values of various parameters ",\
        font=Font3,fg="Indianred",bg=None)
        L1.grid(row=0,column=0)
        #----Upper Frame----------------------
        
        #----Lower Frame----------------------
        lowerFrame=tk.Frame(window1,width=1280,height=618,bg=bgcolor1)
        lowerFrame.pack(side='bottom')
        
        NextButton=tk.Button(lowerFrame,text='Next ',font=Font2,bg=bgcolor1,command=self.Window11)
        NextButton.place(x=1100,y=300)
        
        Close=tk.Button(lowerFrame,text='Back',font=Font2,bg=bgcolor1,command=window1.destroy)
        Close.place(x=1100,y=370)
        
        label1=tk.Label(lowerFrame,text="Geomechanical Parameters:",font=Font2, fg="blue",bg=bgcolor1)
        label1.place(x=10,y=10)

        label10=tk.Label(lowerFrame,text="Cohesion (in kPa):",font=Font2,bg=bgcolor1)
        label10.place(x=30,y=70)

        self.cohesion=tk.Entry(lowerFrame,font=Font2)
        self.cohesion.place(x=280,y=70)
        
        label11=tk.Label(lowerFrame,text="Friction Angle :\n(in degrees)",font=Font2,bg=bgcolor1)
        label11.place(x=70,y=140)

        self.angle=tk.Entry(lowerFrame,font=Font2)
        self.angle.place(x=280,y=140)
        
        label12=tk.Label(lowerFrame,text="Density :\n(in kN per meter cube)",font=Font2,bg=bgcolor1)
        label12.place(x=10,y=240)
        
        self.density=tk.Entry(lowerFrame,font=Font2)
        self.density.place(x=280,y=240)
        
        label2=tk.Label(lowerFrame,text="Geomemetrical Parameters:",font=Font2, fg="blue",bg=bgcolor1)
        label2.place(x=10,y=350)
        
        label20=tk.Label(lowerFrame,text="Height (in m):",font=Font2,bg=bgcolor1)
        label20.place(x=60,y=400)

        self.height=tk.Entry(lowerFrame,font=Font2)
        self.height.place(x=280,y=400)
        
        label21=tk.Label(lowerFrame,text="Slope Angle:\n(in degrees)",font=Font2,bg=bgcolor1)
        label21.place(x=60,y=470)

        self.slopeAngle=tk.Entry(lowerFrame,font=Font2)
        self.slopeAngle.place(x=280,y=470)
        #----Lower Frame----------------------
    
    def Window11(self):
        print('window11')
        window11=tk.Toplevel(bg=bgcolor1)
        window11.geometry("1280x768+20+20")
        #window11.maxsize(1280,768)
        #window11.minsize(1280,768)
        window11.title("Slope Drain Condition")
        self.setIcon(window11)
        
        calculateButton=tk.Button(window11,text='Calculate',font=Font2,command=self.Window12,bg=bgcolor1)
        calculateButton.place(x=1100,y=400)
            
        calculateButton=tk.Button(window11,text='Back',font=Font2,command=window11.destroy,bg=bgcolor1)
        calculateButton.place(x=1120,y=470)
            
        self.radioValue=tk.IntVar()
        self.radioValue.set(None)
        self.photo1Path=resource_path("./Pictures/slopeCondition1.gif")
        self.photo1 = tk.PhotoImage(file=self.photo1Path)
        radio1=tk.Radiobutton(window11,text='1',image=self.photo1,variable=self.radioValue,value=1)
        radio1.place(x=10,y=0) 
        radio1label=tk.Label(window11,text='Fully drained slope',font=Font2)
        radio1label.place(x=400,y=75)
            
        self.photo2Path=resource_path("./Pictures/slopeCondition2.gif")
        self.photo2 = tk.PhotoImage(file=self.photo2Path)
        radio2=tk.Radiobutton(window11,text='2',image=self.photo2,variable=self.radioValue,value=2)
        radio2.place(x=10,y=150)
        radio1labe2=tk.Label(window11,text='Surface water 8x slope height behind toe of slope',font=Font2)
        radio1labe2.place(x=400,y=225)
        
        self.photo3Path=resource_path("./Pictures/slopeCondition3.gif")
        self.photo3 = tk.PhotoImage(file=self.photo3Path)
        radio3=tk.Radiobutton(window11,text='3',image=self.photo3,variable=self.radioValue,value=3)
        radio3.place(x=10,y=300)        
        radio1labe3=tk.Label(window11,text='Surface water 4x slope height behind toe of slope',font=Font2)
        radio1labe3.place(x=400,y=375)
          
        self.photo4Path=resource_path("./Pictures/slopeCondition4.gif")
        self.photo4 = tk.PhotoImage(file=self.photo4Path)
        radio4=tk.Radiobutton(window11,text='4',image=self.photo4,variable=self.radioValue,value=4)
        radio4.place(x=10,y=450)
        radio1labe3=tk.Label(window11,text='Surface water 2x slope height behind toe of slope',font=Font2)
        radio1labe3.place(x=400,y=525)
            
        self.photo5Path=resource_path("./Pictures/slopeCondition5.gif")
        self.photo5 = tk.PhotoImage(file=self.photo5Path)
        radio5=tk.Radiobutton(window11,text='5',image=self.photo5,variable=self.radioValue,value=5)
        radio5.place(x=10,y=600)
        radio1labe3=tk.Label(window11,text='Saturated slope subjected to heavy surface recharge',font=Font2)
        radio1labe3.place(x=400,y=675)
            
        instructionLabel=tk.Label(window11,text='Select appropriate slope condition by clicking the relevent diagram',font="Aerial 20 bold",fg='Indianred1')
        instructionLabel.place(x=395,y=0)
    
    def Window12(self):
            print('Window12')
            window12=tk.Toplevel(bg=bgcolor1)
            window12.geometry("1280x768+20+20")
            #window12.maxsize(1280,768)
            #window12.minsize(1280,768)
            window12.title("Result")
            self.setIcon(window12)
            closeButton=tk.Button(window12,text='Close',font=Font2,command=window12.destroy)
            closeButton.place(x=1120,y=400)
            try:
                #------------Calculation of X------------------------------            
                self.c=float(self.cohesion.get())
                self.gamma=float(self.density.get())
                self.H=float(self.height.get())
                self.phi=deg2rad(float(self.angle.get()))
                self.DlessRatio=self.c/(self.gamma*self.H*tan(self.phi))
                print((self.DlessRatio))
                self.DlessRatio=round(self.DlessRatio,3)
                print((self.radioValue.get()))
                self.chartNo=int(self.radioValue.get())
                slopeangle=float(self.slopeAngle.get())
                
                self.ResultTuple=Point_Between_theta1_and_2(self.DlessRatio,slopeangle,self.chartNo)
                self.x_value=round(self.ResultTuple[0],3)
                self.y_value=round(self.ResultTuple[1],3)
                FSx=self.c/(self.gamma*self.H*self.x_value)
                print(FSx)
                FSy=tan(self.phi)/self.y_value
                print(FSy)
                
                FS=str(round((FSx+FSy)/2.0,3))
                
                FSx=str(round(FSx,3))  
                #------------Calculation of X-------------------------------
                
                #=-----------Result Display---------------------------------            
                self.resultLabel3=tk.Label(window12,text='Factor of Safety from x-axis : '+FSx,font=Font3,fg='blue')
                self.resultLabel3.place(x=0,y=0)
                
                FSy=str(round(FSy,3))
                self.resultLabel3=tk.Label(window12,text='Factor of Safety from y-axis : '+FSy,font=Font3,fg='blue')
                self.resultLabel3.place(x=0,y=150)
                
                self.resultLabel3=tk.Label(window12,text='Factor of Safety (Average): '+FS,font=Font3,fg='blue')
                self.resultLabel3.place(x=0,y=300)
                #=-----------Result Display---------------------------------
            except:
                MB.showerror('Error','Please check the input parameters and select Slope condition properly!')
                print('except caught')
                window12.destroy
    
    def Window2(self):
        print('Window 2')
        window2=tk.Toplevel()
        window2.geometry("1280x768+20+20")
        #window2.maxsize(1280,768)
        #window2.minsize(1280,768)
        window2.title("Sensitivity Analysis")
        self.setIcon(window2)
                
        #----Upper Frame----------------------
        upperFrame=tk.Frame(window2,width=1280,height=150,bg=bgcolor2)
        upperFrame.pack()
        
        L1=tk.Label(upperFrame,text="Enter numerical values of various parameters.\n\
        Choose the parameters to be analysed by clicking the adjacent button.",
        font=Font3,fg="Indianred",bg=None)
        L1.grid(row=0,column=0)
        #----Upper Frame----------------------
        
        #----Lower Frame----------------------
        self.lowerFrame=tk.Frame(window2,width=1280,height=618,bg=bgcolor1)
        self.lowerFrame.pack(side='bottom')
        
        self.NextButton=tk.Button(self.lowerFrame,text='Next ',font=Font2,bg=bgcolor1,command=self.Window21)
        self.NextButton.place(x=1100,y=300)
        
        Close=tk.Button(self.lowerFrame,text='Back',font=Font2,bg=bgcolor1,command=window2.destroy)
        Close.place(x=1100,y=370)
        
        label1=tk.Label(self.lowerFrame,text="Geomechanical Parameters:",font=Font2, fg="blue",bg=bgcolor1)
        label1.place(x=10,y=10)
        
        self.Parameters2bAnalysed={'Cohesion':0,'FAngle':0,'Density':0,'Height':0,'SAngle':0,'SCondition':0}
        self.Dict1={'Cohesion':0,'FAngle':0,'Density':0,'Height':0,'SAngle':0,'SCondition':0}
        self.Dict2={'Cohesion':0,'FAngle':0,'Density':0,'Height':0,'SAngle':0,'SCondition':0}
        
        self.IntCohesion=tk.IntVar()        
        toggleRadCohesion=tk.Checkbutton(self.lowerFrame,text='   ',indicatoron=0,bg=bgcolor3,variable=self.IntCohesion,command=self.checkCohesion)
        toggleRadCohesion.place(x=10,y=70)
        label10=tk.Label(self.lowerFrame,text="Cohesion (in kPa):",font=Font2,bg=bgcolor1)
        label10.place(x=30,y=70)

        self.cohesion=tk.Entry(self.lowerFrame,font=Font2)
        self.cohesion.place(x=280,y=70)
        
        self.IntFAngle=tk.IntVar()
        toggleRadFAngle=tk.Checkbutton(self.lowerFrame,text='   ',indicatoron=0,bg=bgcolor3,variable=self.IntFAngle,command=self.checkFAngle)
        toggleRadFAngle.place(x=10,y=140)
        label11=tk.Label(self.lowerFrame,text="Friction Angle :\n(in degrees)",font=Font2,bg=bgcolor1)
        label11.place(x=70,y=140)

        self.angle=tk.Entry(self.lowerFrame,font=Font2)
        self.angle.place(x=280,y=140)
        
        self.IntDensity=tk.IntVar()
        toggleRadDensity=tk.Checkbutton(self.lowerFrame,text='   ',indicatoron=0,bg=bgcolor3,variable=self.IntDensity,command=self.checkDensity)
        toggleRadDensity.place(x=10,y=240)
        label12=tk.Label(self.lowerFrame,text="Density :\n(in kN per meter cube)",font=Font2,bg=bgcolor1)
        label12.place(x=30,y=240)
        
        self.density=tk.Entry(self.lowerFrame,font=Font2)
        self.density.place(x=280,y=240)
        
        label2=tk.Label(self.lowerFrame,text="Geomemetrical Parameters:",font=Font2, fg="blue",bg=bgcolor1)
        label2.place(x=10,y=350)
        
        self.IntHeight=tk.IntVar()
        toggleRadHeight=tk.Checkbutton(self.lowerFrame,text='   ',indicatoron=0,bg=bgcolor3,variable=self.IntHeight,command=self.checkHeight)
        toggleRadHeight.place(x=10,y=400)
        label20=tk.Label(self.lowerFrame,text="Height (in m):",font=Font2,bg=bgcolor1)
        label20.place(x=60,y=400)

        self.height=tk.Entry(self.lowerFrame,font=Font2)
        self.height.place(x=280,y=400)
        
        self.IntSAngle=tk.IntVar()
        toggleRadSAngle=tk.Checkbutton(self.lowerFrame,text='   ',indicatoron=0,bg=bgcolor3,variable=self.IntSAngle,command=self.checkSAngle)
        toggleRadSAngle.place(x=10,y=470)
        label21=tk.Label(self.lowerFrame,text="Slope Angle:\n(in degrees)",font=Font2,bg=bgcolor1)
        label21.place(x=60,y=470)

        self.slopeAngle=tk.Entry(self.lowerFrame,font=Font2)
        self.slopeAngle.place(x=280,y=470)
        
        self.IntSCondition=tk.IntVar()
        toggleRadSCondition=tk.Checkbutton(self.lowerFrame,text='   ',indicatoron=0,bg=bgcolor3,variable=self.IntSCondition,command=self.checkSCondition)
        toggleRadSCondition.place(x=10,y=560)
        label22=tk.Label(self.lowerFrame,text='Analyse over all of the slope conditions',font=Font2,bg=bgcolor1)
        label22.place(x=60,y=550)
        
        #----Lower Frame----------------------
    
    def checkCohesion(self):
        labelTo=tk.Label(self.lowerFrame,text='to',font=Font2,bg=bgcolor1)
        labelTo.place(x=600,y=70)
        
        if(self.IntCohesion.get()==1):
            self.cohesion2=tk.Entry(self.lowerFrame,font=Font2,state=tk.NORMAL)
            self.cohesion2.place(x=650,y=70)
            
        else:            
            self.cohesion2=tk.Entry(self.lowerFrame,font=Font2,state=tk.DISABLED)
            self.cohesion2.place(x=650,y=70)
        self.Parameters2bAnalysed['Cohesion']=self.IntCohesion.get()
        print(self.Parameters2bAnalysed['Cohesion'])
   
    def checkFAngle(self):
        labelTo=tk.Label(self.lowerFrame,text='to',font=Font2,bg=bgcolor1)
        labelTo.place(x=600,y=140)
        
        if(self.IntFAngle.get()==1):
            self.angle2=tk.Entry(self.lowerFrame,font=Font2,state=tk.NORMAL)
            self.angle2.place(x=650,y=140)
            
        else:            
            self.angle2=tk.Entry(self.lowerFrame,font=Font2,state=tk.DISABLED)
            self.angle2.place(x=650,y=140)
        self.Parameters2bAnalysed['FAngle']=self.IntFAngle.get()
        print(self.Parameters2bAnalysed['FAngle'])
    
    def checkDensity(self):
        labelTo=tk.Label(self.lowerFrame,text='to',font=Font2,bg=bgcolor1)
        labelTo.place(x=600,y=240)
        
        if(self.IntDensity.get()==1):
            self.density2=tk.Entry(self.lowerFrame,font=Font2,state=tk.NORMAL)
            self.density2.place(x=650,y=240)
        else:
            self.density2=tk.Entry(self.lowerFrame,font=Font2,state=tk.DISABLED)
            self.density2.place(x=650,y=240)
        self.Parameters2bAnalysed['Density']=self.IntDensity.get()
        print(self.Parameters2bAnalysed['Density'])
    
    def checkHeight(self):
        labelTo=tk.Label(self.lowerFrame,text='to',font=Font2,bg=bgcolor1)
        labelTo.place(x=600,y=400)
        
        if(self.IntHeight.get()==1):
            self.height2=tk.Entry(self.lowerFrame,font=Font2,state=tk.NORMAL)
            self.height2.place(x=650,y=400)
        else:
            self.height2=tk.Entry(self.lowerFrame,font=Font2,state=tk.DISABLED)
            self.height2.place(x=650,y=400)
        self.Parameters2bAnalysed['Height']=self.IntHeight.get()
        print(self.Parameters2bAnalysed['Height'])
    
    def checkSAngle(self):
        labelTo=tk.Label(self.lowerFrame,text='to',font=Font2,bg=bgcolor1)
        labelTo.place(x=600,y=470)
        
        if(self.IntSAngle.get()==1):
            self.slopeAngle2=tk.Entry(self.lowerFrame,font=Font2,state=tk.NORMAL)
            self.slopeAngle2.place(x=650,y=470)
        else:
            self.slopeAngle2=tk.Entry(self.lowerFrame,font=Font2,state=tk.DISABLED)
            self.slopeAngle2.place(x=650,y=470)
        self.Parameters2bAnalysed['SAngle']=self.IntSAngle.get()
        print(self.Parameters2bAnalysed['SAngle'])
    def checkSCondition(self):
        self.Parameters2bAnalysed['SCondition']=self.IntSCondition.get()
        if(self.IntSCondition.get()==1):
            self.NextButton.config(text='Run Analysis',command=self.runAnalysis)
            self.NextButton.place(x=1080,y=300)
        else:
            self.NextButton.config(text='Next',command=self.Window21)
            self.NextButton.place(x=1100,y=300)
        print(self.Parameters2bAnalysed['SCondition'])
        
    def Window21(self):
        print('Window21')
        
        if(self.IntSCondition.get()==0):        
            self.window21=tk.Toplevel(bg=bgcolor1)
            self.window21.geometry("1280x768+20+20")
            #self.window21.maxsize(1280,768)
            #self.window21.minsize(1280,768)
            self.window21.title("Slope Drain Condition")
            self.setIcon(self.window21)
                
            self.calculateButton=tk.Button(self.window21,text='Run Analysis',font=Font2,command=self.runAnalysis,bg=bgcolor1)
            self.calculateButton.place(x=1080,y=400)
                
            self.backButton=tk.Button(self.window21,text='Back',font=Font2,command=self.window21.destroy,bg=bgcolor1)
            self.backButton.place(x=1120,y=470)
                
            self.radioValue=tk.IntVar()
            self.radioValue.set(0)
                
            self.photo1Path=resource_path("./Pictures/slopeCondition1.gif")    
            self.photo1 = tk.PhotoImage(file=self.photo1Path)
            self.radio1=tk.Radiobutton(self.window21,text='1',image=self.photo1,variable=self.radioValue,value=1)
            self.radio1.place(x=10,y=0) 
            self.radio1label=tk.Label(self.window21,text='Fully drained slope',font=Font3)
            self.radio1label.place(x=400,y=75)
            
            self.photo2Path=resource_path("./Pictures/slopeCondition2.gif") 
            self.photo2 = tk.PhotoImage(file=self.photo2Path)
            self.radio2=tk.Radiobutton(self.window21,text='2',image=self.photo2,variable=self.radioValue,value=2)
            self.radio2.place(x=10,y=150)
            self.radio1labe2=tk.Label(self.window21,text='Surface water 8x slope height behind toe of slope',font=Font3)
            self.radio1labe2.place(x=400,y=225)
              
            self.photo3Path=resource_path("./Pictures/slopeCondition3.gif") 
            self.photo3 = tk.PhotoImage(file=self.photo3Path)
            self.radio3=tk.Radiobutton(self.window21,text='3',image=self.photo3,variable=self.radioValue,value=3)
            self.radio3.place(x=10,y=300)        
            self.radio1labe3=tk.Label(self.window21,text='Surface water 4x slope height behind toe of slope',font=Font3)
            self.radio1labe3.place(x=400,y=375)
            
            self.photo4Path=resource_path("./Pictures/slopeCondition4.gif") 
            self.photo4 = tk.PhotoImage(file=self.photo4Path)
            self.radio4=tk.Radiobutton(self.window21,text='4',image=self.photo4,variable=self.radioValue,value=4)
            self.radio4.place(x=10,y=450)
            self.radio1labe3=tk.Label(self.window21,text='Surface water 2x slope height behind toe of slope',font=Font3)
            self.radio1labe3.place(x=400,y=525)
            
            self.photo5Path=resource_path("./Pictures/slopeCondition5.gif") 
            self.photo5 = tk.PhotoImage(file=self.photo5Path)
            self.radio5=tk.Radiobutton(self.window21,text='5',image=self.photo5,variable=self.radioValue,value=5)
            self.radio5.place(x=10,y=600)
            self.radio1labe3=tk.Label(self.window21,text='Saturated slope subjected to heavy surface recharge',font=Font3)
            self.radio1labe3.place(x=400,y=675)
               
            self.instructionLabel=tk.Label(self.window21,text='Select appropriate slope condition by clicking the relevent diagram',font=Font3,fg='Indianred1')
            self.instructionLabel.place(x=450,y=0)
        else:
            pass
    def runAnalysis(self):
        
        for item in self.Parameters2bAnalysed:
            self.Dict1[item]=0
            self.Dict2[item]=0
            
        
        print('run analysis called')
        self.Dict1['Cohesion']=self.cohesion.get()
        self.Dict1['FAngle']=self.angle.get()
        self.Dict1['Density']=self.density.get()
        self.Dict1['Height']=self.height.get()
        self.Dict1['SAngle']=self.slopeAngle.get()
        if(self.IntSCondition.get()==1):
            self.Dict1['SCondition']=0
            self.Dict2['SCondition']=1
        else:
            self.Dict1['SCondition']=self.radioValue.get()
            self.Dict2['SCondition']=0
        print(self.Parameters2bAnalysed)
        print(self.Dict1)
        
        if(self.Parameters2bAnalysed['Cohesion']==1):
            self.Dict2['Cohesion']=self.cohesion2.get()
        if(self.Parameters2bAnalysed['FAngle']==1):
            self.Dict2['FAngle']=self.angle2.get()
        if(self.Parameters2bAnalysed['Density']==1):
            self.Dict2['Density']=self.density2.get()
        if(self.Parameters2bAnalysed['Height']==1):
            self.Dict2['Height']=self.height2.get()
        if(self.Parameters2bAnalysed['SAngle']==1):
            self.Dict2['SAngle']=self.slopeAngle2.get()
        print(self.Dict2)   
        try:
            
            self.filelist=snip5.analyse(self.Dict1,self.Dict2)
            OutputFileName=FD.asksaveasfilename(defaultextension='.xlsx',filetypes=[('Excelworkbook','.xlsx')])
            shutil.move('AnalysisData.xlsx',OutputFileName)
            print(self.filelist)
        except:
            self.window21.destroy()
            MB.showerror('Error','Please check the values and re-run the analysis')
            
         
        
    def About(self):
        MB.showinfo(title='About',message='''
                    Developer : Uzair Aalam
                    Contact : uaalam[at]myamu[dot]ac[dot]in, 
                                uzairaalam2[at]gmail[dot]com''')
    def Licence(self):
            MB.showinfo(title="License",message='''Licenced under BSD 3-Clause License''')
    def setIcon(self,windowObject):
        try:
            iconPath=resource_path(r'./Pictures/icon1.ico')
            windowObject.iconbitmap(iconPath)
        except:
            print("'icon1.ico' not found!")
           
        
if __name__=='__main__':
    a=App()
    a.mainloop()
