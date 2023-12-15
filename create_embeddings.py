import sqlite3
import openai
import pickle
import time
from yandex_api import *
import asyncio
openai.api_key = "***"
yandex = YandexAPI(token='***', folderid='***')


def get_embedding(text, model="text-embedding-ada-002"):
    text = text.replace("\n", " ")
    return openai.Embedding.create(input=[text], model=model)['data'][0]['embedding']


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

# s = tuple_to_str(rows[9])
# print(s)
# translated = asyncio.run(yandex.translate(s, 'en'))
# print(get_embedding(translated))


print(len(rows))
embeddings = []
for i in range(len(rows)):
    try:
        print(i)
        time.sleep(3.1)
        s = tuple_to_str(rows[i])
        translated = asyncio.run(yandex.translate(s, 'en'))
        embeddings.append(get_embedding(translated))
    except Exception:
        print(f'exception at {i}')
        time.sleep(30)
        embeddings.append(None)

serialized_data = pickle.dumps(embeddings)

with open("embeddings_all.pickle", "wb") as f:
    f.write(serialized_data)

print(len(embeddings))

cur.close()
conn.close()

print('done')
