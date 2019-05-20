#infs 791 group 3 project Wenying Su, Dex Roman, Ievgeniia Chubata

import tkinter as tk
from tkinter import *
import pandas as pd 
import numpy as np 
from tkinter import messagebox, scrolledtext
import matplotlib.pyplot as plt
import datetime
import os 
import matplotlib.pyplot as plt
import seaborn as sns


#GUI
    
def create_variable_window():

    date_entered2 = date_var2.get()
    date_entered1 = date_var1.get()
    ROAD_DEFECT = var1.get() 
    TRAFFIC_CONTROL_DEVICE = var2.get() 
    POSTED_SPEED_LIMIT = var3.get() 
    ROADWAY_SURFACE_COND = var4.get()
    DAMAGE =var6.get()
    
    windowname= "Result window"
    window2= tk.Toplevel(main_window)
    window2.geometry("800x600+300+100")
  
    window2.title(windowname)
    

    df = pd.read_csv('Traffic_Crashes1.csv')
    df = df.replace('UNKNOWN', np.nan).dropna() 
    df.where(df.notnull(),None)
    df = df.dropna()
    df['CRASH_DATE'] = pd.to_datetime(df['CRASH_DATE'],infer_datetime_format=True)
    df = df.set_index('CRASH_DATE')
    df.drop_duplicates()

    date_entered2 = date_var2.get()
    date_entered1 = date_var1.get()
    ROAD_DEFECT = var1.get() 
    TRAFFIC_CONTROL_DEVICE = var2.get() 
    POSTED_SPEED_LIMIT = var3.get() 
    ROADWAY_SURFACE_COND = var4.get()
    DAMAGE =var6.get()


    #muti-select
    Trueval_list = [var1.get(), var2.get(), var3.get(), var4.get(), var6.get()]
    idx_list = ['ROAD_DEFECT','TRAFFIC_CONTROL_DEVICE','POSTED_SPEED_LIMIT', 'ROADWAY_SURFACE_COND', 'DAMAGE']
    idx_choice = [idx_list[i] for i in range(len(Trueval_list)) if Trueval_list[i]]
 
    mw_cancelbutton=Button(window2,text="Cancel",\
                command=window2.destroy,width=10,height=2)\
                .grid(row=0,column=0)
    mw_submitbutton=Button(window2,\
                text="Next",command=Evaluation_window,width=10,height=2)\
                .grid(row=0,column=3)
    
    #message box  
    def validate(date_text):
        try:
            datetime.datetime.strptime(date_text, '%Y-%m-%d')
        except ValueError:
            messagebox.showerror("INCORRECT DATE FORMAT!",\
                                 "SHOULD BE YYYY-MM-DD. PLEASE TRY AGAIN CAREFULLY!")
            window2.destroy()
            
    validate(date_entered1)
    validate(date_entered2)

     
    #scrolle
    window2.update()
    scr = scrolledtext.ScrolledText(window2, width = 100, height = 30, wrap = tk.WORD)
    scr.place(x = int(window2.winfo_width() * 0.05), y = int(window2.winfo_height() *0.15))
    scr.insert(END, str(df.loc[date_entered1,idx_choice]))
    scr.insert(END, str(df.loc[date_entered2,idx_choice]))


    
def Evaluation_window():
    windowname= "Evaluation"
    window3= tk.Toplevel(main_window)
    window3.geometry("800x600+300+100")
    for col_no in range(0,3):
        window3.columnconfigure(col_no,minsize = 80)
    for row_no in range(0,9):
        window3.rowconfigure(row_no,minsize=80)
        
    var7 = StringVar()
    var7.set(2)
    
    window3.title(windowname)   
    
        
        
    mw_namelabel4 = Label(window3, text = "Do you like our program?",\
                     font =("Helvetica",16),fg = "black").grid(row = 1, column = 2)
    l = Label(window3, width=20, text='', font =("Helvetica",20))
    l.grid(row = 4, column = 2)
    
    def Thank_you():
        l.config(text='Thank you!')
    def Do_better():
        l.config(text='We can do better next time!')
        
    R1 = Radiobutton(window3, text='Yes', value= "Yes",variable = var7,command =Thank_you, font =("Helvetica",16)).grid(row = 2, column = 2)

    R2 = Radiobutton(window3, text='No', value= "No",variable = var7,command=Do_better, font =("Helvetica",16)).grid(row = 3, column = 2)


    Exit_cancelbutton=Button(window3,text="Exit",\
                command=window3.destroy,width=10,height=2)\
                .grid(row=4,column=3)            
 
def Analysis_window():
    windowname= "Analysis"
    window4= tk.Toplevel(main_window)
    window4.geometry("800x600+300+100")
    window4.title(windowname)
#link the listbox     
    listindex=mw_listbox.curselection()
    listitem=mw_listbox.get(listindex)
    
#can change data in following text 
    if listitem == 'Analysis1':
        mw_label= Label(window4, text="The most common day of the week when the crash had happened was Sunday.\n"  +
"The most common hour of day when the crash had happened was 4 pm.\n" +
'There were total 130 fatal injuries in the dataset. \n'+
'There were total 213 hit and run accidents in the dataset.\n' +
'The 5 most common causes of traffic crashes were:\n' +
'UNABLE TO DETERMINE              33675 \n'+
'FAILING TO YIELD RIGHT-OF-WAY    16389 \n'+
'FOLLOWING TOO CLOSELY            14090 \n'+
'NOT APPLICABLE                    5661 \n'+
'IMPROPER BACKING                  5333 \n',
        font=("Helvetica",20),justify=LEFT).grid(row=1,columnspan=3)

    mw_cancelbutton=Button(window4,text="Cancel",\
                command=window4.destroy,width=10,height=2)\
                .grid(row=0,column=3)     
     
    if listitem == 'CHART1':
        mw_label= Label(window4, text="Chart1",
        font=("Helvetica",20),justify=LEFT).grid(row=0,columnspan=3)
        image_file1 = PhotoImage(file= cwd + r'/chart1.gif')
        label_img= Label(window4, image = image_file1)
        label_img.grid(row=1,rowspan=1,column=3)
        
    if listitem == 'CHART2':
        mw_label= Label(window4, text="Chart2",
        font=("Helvetica",20),justify=LEFT).grid(row=0,columnspan=3)
        image_file2 = PhotoImage(file= cwd + r'/chart2.gif')
        label_img= Label(window4, image = image_file2)
        label_img.grid(row=1,rowspan=1,column=3)
        
    if listitem == 'CHART3':
        mw_label= Label(window4, text="Chart3",
        font=("Helvetica",20),justify=LEFT).grid(row=0,columnspan=3)
        image_file3 = PhotoImage(file= cwd + r'/chart3.gif')
        label_img= Label(window4, image = image_file3)
        label_img.grid(row=1,rowspan=1,column=3)
        
    if listitem == 'CHART4':
        mw_label= Label(window4, text="Chart4",
        font=("Helvetica",20),justify=LEFT).grid(row=0,columnspan=3)
        image_file4 = PhotoImage(file= cwd + r'/chart4.gif')
        label_img= Label(window4, image = image_file4)
        label_img.grid(row=1,rowspan=1,column=3)
        
              
main_window=tk.Tk()
main_window.title("Main window")

    
for col_no in range(0,3):
    main_window.columnconfigure(col_no,minsize = 300)
for row_no in range(0,9):
    main_window.rowconfigure(row_no,minsize=60)


mw_title=Label(main_window, text="Welcome to the City of Chicago Traffic Crashes Analysis",\
    font=("Helvetica",20),justify=CENTER).grid(row=0,columnspan=3)

mw_instruction=Label(main_window, text="Nearly 1.25 million people die in road crashes each year, \n "+
                   " on average 3,287 deaths a day. An additional 20-50 million are injured or disabled.\n" +
                   "More than half of all road traffic deaths occur among young adults.\n "+
                    "This program is here to bring awareness to this severe problem and educate its users into \n" + 
                   "becoming safer more well-informed drivers.", font=("Helvetica",16),fg = "gray").grid(row=1,columnspan=3)

global date_var
date_var1 = tk.StringVar() 
date_var2 = tk.StringVar()

mw_namelabel = Label(main_window, text = "Please enter the date from\n "+ "(eg:2017-09-01):",\
                     font =("Helvetica",16),fg = "black").grid(row=3,column = 0, columnspan=1)

mw_dateentry1 = Entry(main_window,textvariable = date_var1)
mw_dateentry1.grid(row = 4, column = 0)

mw_1to2 = Label(main_window, text = "to",\
                     font =("Helvetica",16),justify=CENTER, fg = "black").grid(row=5,column=0)


mw_dateentry2 = Entry(main_window,textvariable = date_var2)
mw_dateentry2.grid(row = 6, column = 0)


mw_cancelbutton=Button(main_window,text="Cancel",\
                command=main_window.destroy,width=10,height=2)\
                .grid(row=10,column=1)
mw_submitbutton=Button(main_window,\
                text="Submit",command=create_variable_window,width=10,height=2)\
                .grid(row=10,column=0)
                
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var6=IntVar()


mw_namelabel2 = Label(main_window, text = "Please select the variables \n"+"you want to explore:",\
                     font =("Helvetica",16),fg = "black").grid(row=3,column = 1, columnspan=1) 
mw_cbchoice1=Checkbutton(main_window, text="Road Defect",variable=var1,\
                font=("Helvetica",14)).grid(row=4,column=1,sticky = W)
mw_cbchoice2=Checkbutton(main_window, text="Traffic control device",variable=var2,\
                font=("Helvetica",14)).grid(row=5,column=1,sticky = W)        
mw_cbchoice3=Checkbutton(main_window, text="Speed Limit",variable=var3,\
                font=("Helvetica",14)).grid(row=6,column=1,sticky = W)
mw_cbchoice4=Checkbutton(main_window, text="Roadway surface condition",variable=var4,\
                font=("Helvetica",14)).grid(row=7,column=1,sticky = W)
mw_cbchoice6=Checkbutton(main_window, text="Damage",variable=var6,\
                font=("Helvetica",14)).grid(row=8,column=1,sticky = W)
mw_namelabel3 = Label(main_window, text = "Please choose the analysis we had:",
                font =("Helvetica",16),fg = "black").grid(row=3,column = 2, columnspan=1) 



mw_listbox = Listbox(main_window)
for item in ["Analysis", "CHART1", "CHART2", "CHART3","CHART4"]:   
    mw_listbox.insert(END, item)     
mw_listbox.grid(row=4, column = 2, rowspan = 4, columnspan = 1)


mw_submitbutton=Button(main_window,\
                text="Go to Analysis",command=Analysis_window,width=12,height=2)\
                .grid(row=10,column=2)
          
cwd = os.getcwd() 

image_file = PhotoImage(file= cwd + '/image3.gif')
label_img= Label(main_window, image = image_file)
label_img.grid(row=0,rowspan=1,column=3)


main_window.mainloop()


#Analysis dataset 
sns.set_style('whitegrid')

df = pd.read_csv('Traffic_Crashes2.csv', low_memory=False)
df1=df[df.isnull().any(axis=1)]
print(df1.head())

# Our data needs to be cleaned up because 6 of the columns have blank fields : LANE COUNT, REPORT TYPE, INTERSECTION RELATED, NOT RIGHT OF WAY, HIT AND RUN,
# AND MOST SEVERE INJURY.

df1=df1.fillna({"LANE_CNT": 2})

# Applying lambda function - if data type is in 'biufc' (boolean, integer, unicode, float, and complex), N/A values will be replaced with "NO".

df_clean = df1.apply(lambda x: x.fillna("NO") if x.dtype.kind in 'biufc' else x.fillna('.'))


# The most common day of the week when the crash had happened
def common_day(df):

    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    index = int(df_clean['CRASH_DAY_OF_WEEK'].mode())
    most_com_day = days_of_week[index]
    print('The most common day of the week when the crash had happened was {}.'.format(most_com_day))
common_day(df_clean)

# The most common hour the crash had happened
def common_hour(df):
    most_com_hour = int(df_clean["CRASH_HOUR"].mode())
    if most_com_hour == 0:
        am_pm = 'am'
        pop_hour_readable = 12
    elif 1 <= most_com_hour < 13:
        am_pm = 'am'
        pop_hour_readable = most_com_hour
    elif 13 <= most_com_hour < 24:
        am_pm = 'pm'
        pop_hour_readable = most_com_hour - 12
    print('The most common hour of day when the crash had happened was {} {}.'.format(pop_hour_readable, am_pm))
common_hour(df_clean)

# The number of fatal injuries in the dataset
def fatal_injury(df):
    fatal_injury=df_clean[df_clean["MOST_SEVERE_INJURY"].apply(lambda injury: injury=='FATAL')]['MOST_SEVERE_INJURY'].count()
    print('There were total {} fatal injuries in the dataset.'.format(fatal_injury))
fatal_injury(df_clean)

# The number of hit and run accidents
def hit_and_run(df):
    hit_run=df_clean[df_clean["HIT_AND_RUN_I"].apply(lambda hitrun: hitrun=='Y')]['HIT_AND_RUN_I'].count()
    print('There were total {} hit and run accidents in the dataset.'.format(hit_run))
hit_and_run(df_clean)

# The 5 most common crash types
#def common_type(df):
    
# The 5 most common crash causes
def common_cause(df):
    com_cause=df_clean["PRIM_CONTRIBUTORY_CAUSE"].value_counts().head()
    print('The 5 most common causes of traffic crashes were: \n{}.'.format(com_cause))
common_cause(df_clean)

# Creating a heatmap of most common crash hour, day of week and cause
def heat_map(df):
    dayHour = df_clean.groupby(by=['CRASH_HOUR','CRASH_DAY_OF_WEEK']).count()['PRIM_CONTRIBUTORY_CAUSE'].unstack()
    plt.figure(figsize=(12,6))
    sns.heatmap(dayHour, cmap='plasma')
    plt.show()
heat_map(df_clean)

# The countplot that shows the dollar amount of demage created by traffic crashes
def damage_plot(df):
    plot1=sns.countplot(x="DAMAGE",data=df_clean,palette='viridis')
    plt.show()
damage_plot(df_clean)

# The countplot that shows the crash month and damage related to it
def damage_plot_by_month(df):
    plot2=sns.countplot(x='CRASH_MONTH',data=df_clean,hue='DAMAGE')
    plt.show()
damage_plot_by_month(df_clean)

# The plot that shows most common crash hour
def crash_hour_plot(df):
    plot3=sns.countplot(x='CRASH_HOUR', data=df_clean)
    plt.show()
crash_hour_plot(df_clean)
