import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#Reading the dataset
try:
    df1 = pd.read_csv("spotify stuff/spotify_data.csv")
except:
    print("Dataset has not been added correctly")
#Defining the variables
genres = ["metal","Hard-rock","metalcore","death-metal"]
year1 = [2000]
year2 = []
year3 = []
column1 = ["artist_name","track_name","popularity","year","genre","duration_ms"]
b = 2000
year4 = [2000]
year5 = []
#Creating a list from 2000 - 2024
for i in range(0,24):
    year3.append(b)
    b = b+1
#Creating a dataset of the most popular songs
try:
    df = df1.loc[df1['genre'].isin(genres)]
    for i in range(0,24): 
        df2 = df.loc[df['year'].isin(year4)]
        df2 = df2.sort_values(
        by="popularity",
        ascending=False)
        x = df2.iloc[0]["popularity"]
        year5.append(x)
        year4[0] = year4[0]+1
except:
    print("Dataset does not include a genre column")
#Creating a dataset of how many songs per year
try:
    for i in range(0,24):
        year2.append(len(df.loc[df['year'].isin(year1)]))
        year1[0] = year1[0]+1
    df = df.sort_values(
        by="popularity",
        ascending=False)
    df = df[column1]
except:
    print("Dataset does not include a year column")

#Creates the bar graph of how many songs per year
def bar():
    y = np.array(year2)
    x = np.array(year3)
    plt.bar(x,y)
    plt.show()
#Creates the bar graph of popularity over time
def plot():
    y = np.array(year5)
    x = np.array(year3)
    plt.bar(x,y)
    plt.show()

#The inputs from the user and visualisation 
def ui():
    print("""Please select an option:
                1 - Show the original dataset
                2 - Show the updated dataset
                3 - Visualise the amount of metal songs per year
                4 - Visualise the popularity of metal songs over time
                5 - Quit program""")
    try:
        inp = int(input("Enter Selection: "))

        if inp == 1:
            print("Input received")
            print(df1)
            ui()
        elif inp == 2:
            print("Input received")
            foo = int(input("""How would you like the dataset sorted?:
                        1 - Popularity high to low
                        2 - Year low to high
                        Enter selection: """))
            if foo == 1:
                print("Input received")
                print(df.head(50))
            elif foo == 2:
                print("Input received")
                df3 = df.sort_values(
                by="year",
                ascending=True)
                print(df3.head(50))
            else:
                print("Invalid input")
            ui()
        elif inp == 3:
            print("Input received")
            y = np.array(year2)
            x = np.array(year3)
            plt.bar(x,y)
            plt.show()
            ui()
        elif inp == 4:
            print("Input received")
            y = np.array(year5)
            x = np.array(year3)
            plt.bar(x,y)
            plt.show()
            ui()
        elif inp == 5:
            print("Input received")
            pass
        else:
            print("Number is not within specified range")
    except:
        print("Input is not an integer")
ui()