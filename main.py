import pandas as pd
import csv


pd.set_option('display.max_columns', None)

url = "http://www.espn.com/nfl/team/roster/_/name/cle/cleveland-browns"


tables = pd.read_html(url, extract_links = "body", index_col= "Name")

df = tables[0]

df = pd.DataFrame(df, columns = ["Name"])

df.to_csv("ignore.csv")

players = []
with open("ignore.csv", newline = '') as csvfile:
    read = csv.reader(csvfile, delimiter = ' ', quotechar= '|')
    for row in read:
        line = ''.join(row)
        line = line.removeprefix('"')
        line = line.removeprefix('(')
        line = line.removeprefix('"')
        line = line.removeprefix("'")

        line = line.removesuffix(',')
        line = line.removesuffix('"')
        line = line.removesuffix(')')
        line = line.removesuffix('"')
        line = line.removesuffix("'")

        index = line.find(" _/")
        if index != -1:
            line = line[:index] + "gamelog/" + line[index:]
        tmp = line.split(",")
        if (tmp[0].__contains__('zaire')):
            break
        players.append(tmp)

players.pop(0)

list = []

with pd.ExcelWriter("browns.xlsx") as writer:
    for p in players:
        link = p[1].removeprefix("'")
        name = p[0].removesuffix("'")
        stats = pd.read_html(link)
        if name == 'AustinWatkinsJr.80':
            break
        new_df = pd.DataFrame(stats[2])
        new_df.to_excel(writer, sheet_name=name, index=False)
    



