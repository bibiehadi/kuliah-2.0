import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

filepath = "contoh-data.csv"
sep = ","
hue = "Kategori"
delimiter = None

df = pd.read_csv(filepath, sep=sep, delimiter=delimiter)

sns.pairplot(df, hue=hue)
plt.show()
