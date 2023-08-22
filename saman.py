import pandas as pd
import csv

file1 = open("D:\Onedrive - antivirus\OneDrive\Desktop\Lottery_Mega_Millions_Winning_Numbers__Beginning_2002.csv","r")

with open("D:\Onedrive - antivirus\OneDrive\Desktop\Lottery_Mega_Millions_Winning_Numbers__Beginning_2002.csv","r") as file1:
    file_stuff = file1.read()
    print(file_stuff)