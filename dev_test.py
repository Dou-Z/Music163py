import pandas as pd

df = pd.read_csv('music_data/album_list.csv', header=None, names=['id', 'tag', 'url', 'z','a'])
print(df)