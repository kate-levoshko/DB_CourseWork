from connect_database import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

PLOT_LABEL_FONT_SIZE = 8

def getColors(n):
    COLORS = []
    cm = plt.cm.get_cmap('hsv', n)
    for i in np.arange(n):
        COLORS.append(cm(i))
    return COLORS

def dict_sort(my_dict):
    keys = []
    values = []
    my_dict = sorted(my_dict.items(), key=lambda x:x[1], reverse=True)
    for k, v in my_dict:
        keys.append(k)
        values.append(v)
    return (keys,values)


def sales():
    conn = connect_db()
    df = pd.read_sql('SELECT SUM(na_sales) AS na_sales, SUM(eu_sales) AS eu_sales ,SUM(jp_sales) AS jp_sales, SUM(other_sales) AS other_sales FROM public.data_games', conn)
    dict = {}
    dict['NA_sales'] = df.values[0][0]
    dict['EU_sales'] = df.values[0][1]
    dict['JP_sales'] = df.values[0][2]
    dict['Other_sales'] = df.values[0][3]
    dict_keys,dict_values = dict_sort(dict)
    top_keys = len(dict_keys)
    plt.title('Продажі', fontsize=PLOT_LABEL_FONT_SIZE)
    plt.bar(np.arange(top_keys), dict_values, color=getColors(top_keys))
    plt.xticks(np.arange(top_keys), dict_keys, rotation=90, fontsize=8)
    plt.yticks(fontsize=PLOT_LABEL_FONT_SIZE)
    plt.ylabel('Кількість продаж', fontsize=PLOT_LABEL_FONT_SIZE)
    plt.show()

def games_by_years():
    conn = connect_db()
    df = pd.read_sql('SELECT year,COUNT(year) FROM public.data_games GROUP BY year',conn)
    dict = {}
    for i in range(len(df.values)):
        dict[df.values[i][0]] = df.values[i][1]

    dict_keys, dict_values = dict_sort(dict)
    top_keys = len(dict_keys)

    plt.title('Випуск ігор по рокам', fontsize=PLOT_LABEL_FONT_SIZE)
    plt.bar(np.arange(top_keys), dict_values, color=getColors(top_keys))
    plt.xticks(np.arange(top_keys), dict_keys, rotation=90, fontsize=8)
    plt.yticks(fontsize=PLOT_LABEL_FONT_SIZE)
    plt.ylabel('Кількість ігор', fontsize=PLOT_LABEL_FONT_SIZE)
    plt.show()


def games_by_publisher():
    conn = connect_db()
    df = pd.read_sql('SELECT publisher,COUNT(publisher) FROM public.data_games GROUP BY publisher',conn)
    dict = {}
    for i in range(len(df.values)):
        if df.values[i][1] > 50:
            dict[df.values[i][0]] = df.values[i][1]
        else :
            continue
    dict_keys, dict_values = dict_sort(dict)
    top_keys = len(dict_keys)

    plt.title('Випуск ігор по компаніям', fontsize=PLOT_LABEL_FONT_SIZE)
    plt.bar(np.arange(top_keys), dict_values, color=getColors(top_keys))
    plt.xticks(np.arange(top_keys), dict_keys, rotation=90, fontsize=8)
    plt.yticks(fontsize=PLOT_LABEL_FONT_SIZE)
    plt.ylabel('Кількість ігор', fontsize=PLOT_LABEL_FONT_SIZE)
    plt.show()

def games_by_platform():
    conn = connect_db()
    df = pd.read_sql('SELECT platform,COUNT(platform) FROM public.data_games GROUP BY platform',conn)
    dict = {}

    for i in range(len(df.values)):
        dict[df.values[i][0]] = df.values[i][1]

    dict_keys, dict_values = dict_sort(dict)
    top_keys = len(dict_keys)

    plt.title('Випуск ігор по платформам', fontsize=PLOT_LABEL_FONT_SIZE)
    plt.bar(np.arange(top_keys), dict_values, color=getColors(top_keys))
    plt.xticks(np.arange(top_keys), dict_keys, rotation=90, fontsize=8)
    plt.yticks(fontsize=PLOT_LABEL_FONT_SIZE)
    plt.ylabel('Кількість ігор', fontsize=PLOT_LABEL_FONT_SIZE)
    plt.show()

def games_by_genre():
    conn = connect_db()
    df = pd.read_sql('SELECT genre,COUNT(genre) FROM public.data_games GROUP BY genre', conn)
    dict = {}

    for i in range(len(df.values)):
        dict[df.values[i][0]] = df.values[i][1]

    dict_keys, dict_values = dict_sort(dict)
    top_keys = len(dict_keys)

    plt.title('Випуск ігор по жанрам', fontsize=PLOT_LABEL_FONT_SIZE)
    plt.bar(np.arange(top_keys), dict_values, color=getColors(top_keys))
    plt.xticks(np.arange(top_keys), dict_keys, rotation=90, fontsize=8)
    plt.yticks(fontsize=PLOT_LABEL_FONT_SIZE)
    plt.ylabel('Кількість ігор', fontsize=PLOT_LABEL_FONT_SIZE)
    plt.show()