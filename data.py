from connect_database import *
import random
import pandas as pd


PLATFORM_CHOICES = [
    ("Wii","Wii"),
    ("X360","X360"),
    ("XOne","XOne"),
    ("PC","PC"),
    ("PS","PS"),
    ("Wii","Wii")
]

GENRES_CHOICES = [
    ("Sports","Sports"),
    ("Strategy","Strategy"),
    ("Action","Action"),
    ("Puzzle","Puzzle"),
    ("Role-Playing","Role-Playing"),
    ("Platform","Platform"),
    ("Fighting","Fighting"),
    ("Simulation","Simulation"),
    ("Misc","Misc"),
    ("Adventure","Adventure"),
    ("Shooter","Shooter"),
    ("Racing","Racing")
]

PUBLISHER_CHOICES = [
    ("Nintendo","Nintendo"),
    ("Activision","Activision"),
    ("Ubisoft","Ubisoft"),
    ("Electronic Arts","Electronic Arts"),
    ("Bethesda Softworks","Bethesda Softworks")
]

def generate_data(count):
    conn = connect_db()
    cursor = conn.cursor()
    for i in range(count):
        genre = random.choice(GENRES_CHOICES)[0]
        publisher = random.choice(PUBLISHER_CHOICES)[0]
        year = random.randrange(1990,2016)
        platform = random.choice(PLATFORM_CHOICES)[0]
        NA_sales = random.randrange(0,100)
        EU_sales = random.randrange(0,100)
        JP_sales = random.randrange(0,100)
        Other_sales = random.randrange(0,100)
        Global_sales = NA_sales + EU_sales + JP_sales + Other_sales
        name = 'name'
        cursor.execute('INSERT INTO public.data_games(name, platform, year, genre, publisher, na_sales, eu_sales,'
                       'jp_sales, other_sales, global_sales)'
                       'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                       (name, platform, year, genre, publisher, NA_sales, EU_sales, JP_sales, Other_sales, Global_sales))
        conn.commit()

def read_data():
    df = pd.read_csv('vgsales.csv', escapechar='`', low_memory=True)
    conn = connect_db()
    cursor = conn.cursor()
    for i in range(len(df)-1):
        try:
            name = df.loc[i, 'Name']
            platform = df.loc[i, 'Platform']
            year = int(df.loc[i, 'Year'])
            genre = df.loc[i, 'Genre']
            publisher = df.loc[i, 'Publisher']
            NA_sales = df.loc[i, 'NA_Sales']
            EU_sales = df.loc[i, 'EU_Sales']
            JP_sales = df.loc[i, 'JP_Sales']
            Other_sales = df.loc[i, 'Other_Sales']
            Global_sales = df.loc[i, 'Global_Sales']
            cursor.execute('INSERT INTO public.data_games(name, platfrom, year, genre, publisher, na_sales, eu_sales,'
            'jp_sales, other_sales, global_sales)'
            'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                           (name,platform,year,genre,publisher,NA_sales,EU_sales,JP_sales,Other_sales,Global_sales))
            conn.commit()
        except ValueError:
             continue
    print("Success")