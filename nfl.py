import pandas as pd
from bs4 import BeautifulSoup as bs

urls = ['https://www.nfl.com/stats/player-stats/category/passing/2023/reg/all/passingyards/desc',
        'https://www.nfl.com/stats/player-stats/category/rushing/2023/reg/all/rushingyards/desc',
        'https://www.nfl.com/stats/player-stats/category/receiving/2023/reg/all/receivingreceptions/desc']

dfs = []
for url in urls:
    table = pd.read_html(url)
    df = pd.DataFrame(table[0])
    dfs.append(df)

tags = ['pass', 'rush', 'rec']

for tag,df in zip(tags,dfs):
     df.to_csv('{}.csv'.format(tag), index=False)
