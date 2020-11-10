#covid-tracker.py
import requests
from tkinter import *
import json
from datetime import datetime

root = Tk()

root.title('Covid-19 Tracker - California')
root.geometry('500x500')

lbl = Label(root, text='Total positive cases...')
lbl1 = Label(root, text='Positive test case increase from the previous day...')

lbl.grid(column=1, row=0)
lbl1.grid(column=1, row=1)
lbl2 = Label(root,text='')
lbl2.grid(column=1, row=3)

def clicked():
    print('Retrieving California covid statistics...')
    url = 'https://api.covidtracking.com/v1/states/CA/current.json?state=CA'
    data = requests.get(url)
    current_date_str = str(data.json()['date'])
    new_date = datetime.strptime(current_date_str, "%Y%m%d")
    updated_date = datetime.strftime(new_date, "%B %d, %Y")

    total_cases = str(data.json()['positive'])




    lbl.configure(text= 'Total positive cases as of ' + updated_date + ': ' + total_cases)
    lbl1.configure(text='Increase in positive cases from previous day: ' + str(data.json()['positiveIncrease']), fg='red',bg='white')

    lbl2.configure(text='Data Refreshed!', fg='white', bg='blue')

btn = Button(root,text='Refresh', command = clicked)
btn.grid(column=2,row=0)

root.mainloop()
