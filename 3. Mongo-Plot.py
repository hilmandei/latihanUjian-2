import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pymongo import MongoClient

server = MongoClient('mongodb://localhost:27017/')

db = server['kampus']  # memilih database yang akan digunakan
koleksi1 = db['Dosen']  # memilih collection(table) yang akan dipakai
koleksi2 = db['Mahasiswa']

df1 = []
df2 = []

for x in koleksi1.find():
    a = {'asal': x['asal'], 'nama': x['nama'], 'status': 'dosen', 'usia': x['usia']}
    df1.append(a)
print(pd.DataFrame(df1))
x1 = pd.array(pd.DataFrame(df1)['nama'])
y1 = pd.array(pd.DataFrame(df1)['usia'])

print()

for y in koleksi2.find():
    b = {'asal': y['asal'], 'nama': y['nama'], 'status': 'mahasiswa', 'usia': y['usia']}
    df2.append(b)
print(pd.DataFrame(df2))
x2 = pd.array(pd.DataFrame(df2)['nama'])
y2 = pd.array(pd.DataFrame(df2)['usia'])


plt.figure('Usia Dosen-Mahasiswa', figsize=(10, 5))          #lebar 10, tinggi 5

plt.bar(x1, y1)
plt.bar(x2, y2)
plt.grid(True)
plt.title('Usia Warga Kampus')

plt.legend(['Dosen', 'Mahasiswa'])



plt.show()
