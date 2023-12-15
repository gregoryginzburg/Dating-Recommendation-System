import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import pickle
import mplcursors
import sqlite3
import warnings

warnings.filterwarnings('ignore')
# read the serialized data from the file
with open("embeddings/embeddings_all.pickle", "rb") as f:
    serialized_data = f.read()


def tuple_to_str(t):
    sex = {0: 'Мужской', 1: 'Женский'}
    return f"Обо мне: {t[4]},\n"\
           f"Возраст: {t[1]},\n"\
           f"Пол: {sex[t[2]]},\n"\
           f"Город: {t[3]}\n"\



conn = sqlite3.connect('main.db')

cur = conn.cursor()
cur.execute("SELECT id, age, sex, city, description FROM users WHERE age IS NOT NULL AND sex IS NOT NULL AND city IS NOT NULL AND description != '' AND description IS NOT NULL")
rows = cur.fetchall()
print('rows: ', len(rows))


# deserialize the data using pickle
embeddings = pickle.loads(serialized_data)
print('embeddings: ', len(embeddings))
embeddings = [x for x in embeddings if x is not None]
print('embeddings: ', len(embeddings))

indices = []
for i, x in enumerate(embeddings):
    if x is not None:
        indices.append(i)
rows = [rows[i] for i in indices]


ages = []
print(rows[0])

for row in rows:
    if row[1] <= 11:
        ages.append(0)
    elif row[1] <= 13:
        ages.append(1)
    elif row[1] <= 15:
        ages.append(2)
    elif row[1] <= 18:
        ages.append(3)
    else:
        ages.append(4)
print('rows: ', len(rows))


# Create a t-SNE model and transform the data
tsne = TSNE(n_components=2, perplexity=15, random_state=42,
            init='random', learning_rate=200)
array = np.array(embeddings)
vis_dims = tsne.fit_transform(array)


x = [x for x, y in vis_dims]
y = [y for x, y in vis_dims]


color_map = ['red', 'green', 'blue', 'orange', 'purple']
fig, ax = plt.subplots()
sc = ax.scatter(x, y, c=ages, cmap='bwr_r', alpha=0.3)

# add annotations to the scatter plot
annotations = [tuple_to_str(row) for row in rows]
tooltip = mplcursors.cursor(sc, hover=True)
tooltip.connect("add", lambda sel: sel.annotation.set_text(
    annotations[sel.target.index]))

# display the plot
plt.show()
