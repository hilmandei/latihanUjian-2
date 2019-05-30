import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

'--------------------------------------------------Data Awal-------------------------------------------------------'

d1 = pd.read_csv('Data Latihan Ujian\Balita Terimunisasi BCG 1995-2017.csv' )
d2 = pd.read_csv('Data Latihan Ujian\Balita Terimunisasi Campak 1995-2017.csv')
d3 = pd.read_csv('Data Latihan Ujian\Balita Terimunisasi DPT 1995-2017.csv')
d4 = pd.read_csv('Data Latihan Ujian\Balita Terimunisasi Polio 1995-2017.csv')

list1 = []
list2 = []
list3 = []
list4 = []
x1 = d1[d1.columns[1]]
x2 = d2[d2.columns[1]]
x3 = d3[d3.columns[1]]
x4 = d4[d4.columns[1]]

'---------------------------------------- check non-angka pada kolom %balita--------------------------------------'

for x in x1:
    try:
        if isinstance(float(x), float):
            pass
    except:
        list1.append(x)

for x in x2:
    try:
        if isinstance(float(x), float):
            pass
    except:
        list2.append(x)

for x in x3:
    try:
        if isinstance(float(x), float):
            pass
    except:
        list3.append(x)

for x in x4:
    try:
        if isinstance(float(x), float):
            pass
    except:
        list4.append(x)


naD1 = list(dict.fromkeys(list1))
naD2 = list(dict.fromkeys(list2))
naD3 = list(dict.fromkeys(list3))
naD4 = list(dict.fromkeys(list4))

'--------------------------------------Value non-angka diubah menjadi NaN value-------------------------------------'

df1 = d1.replace(naD1, np.NaN)
df2 = d2.replace(naD2, np.NaN)
df3 = d3.replace(naD3, np.NaN)
df4 = d2.replace(naD4, np.NaN)

df1[df1.columns[1]] = pd.to_numeric(df1[df1.columns[1]]).interpolate()
df2[df2.columns[1]] = pd.to_numeric(df2[df2.columns[1]]).interpolate()
df3[df3.columns[1]] = pd.to_numeric(df3[df3.columns[1]]).interpolate()
df4[df4.columns[1]] = pd.to_numeric(df4[df4.columns[1]]).interpolate()


'--------------------------------------Plot figure 1-------------------------------------'

plt.figure('Tervaksinasi', figsize=(10, 8))          #lebar 10, tinggi 8

#plot1
plt.subplot(2, 2, 1)                            #1 baris , 2 kolom , posisi 1(pertama)
plt.bar(df1[df1.columns[0]], df1[df1.columns[1]], color='red')
plt.title('BCG')
plt.xticks(df1[df1.columns[0]], rotation=90)


# #plot2
plt.subplot(2, 2, 2)                            #1 baris , 2 kolom , posisi 1(pertama)
plt.bar(df2[df2.columns[0]], df2[df2.columns[1]], color='green')
plt.title('Campak')
plt.xticks(np.array(df2[df2.columns[0]]), rotation=90)

# #plot3
plt.subplot(2, 2, 3)                            #1 baris , 2 kolom , posisi 1(pertama)
plt.bar(df3[df3.columns[0]], df3[df3.columns[1]], color='yellow')
plt.title('DPT')
plt.xticks(np.array(df3[df3.columns[0]]), rotation=90)

# #plot4
plt.subplot(2, 2, 4)                            #1 baris , 2 kolom , posisi 1(pertama)
plt.bar(df4[df4.columns[0]], df4[df4.columns[1]], color='blue')
plt.title('Polio')
plt.xticks(np.array(df4[df4.columns[0]]), rotation=90)



'--------------------------------------Plot figure 2-------------------------------------'

np100 = np.full(23, 100)
xz1 = np100 - (df1[df1.columns[1]])
xz2 = np100 - (df2[df2.columns[1]])
xz3 = np100 - (df3[df3.columns[1]])
xz4 = np100 - (df4[df4.columns[1]])

plt.figure('Belum Tervaksin', figsize=(10, 8))          #lebar 10, tinggi 8

#plot1
plt.subplot(2, 2, 1)
plt.bar(df1[df1.columns[0]], xz1, color='red')
plt.title('BCG')
plt.xticks(df1[df1.columns[0]], rotation=90)

# #plot2
plt.subplot(2, 2, 2)
plt.bar(df2[df2.columns[0]], xz2, color='green')
plt.title('Campak')
plt.xticks(np.array(df2[df2.columns[0]]), rotation=90)

# #plot3
plt.subplot(2, 2, 3)
plt.bar(df3[df3.columns[0]], xz3, color='yellow')
plt.title('DPT')
plt.xticks(np.array(df3[df3.columns[0]]), rotation=90)

# #plot4
plt.subplot(2, 2, 4)
plt.bar(df4[df4.columns[0]], xz4, color='blue')
plt.title('Polio')
plt.xticks(np.array(df4[df4.columns[0]]), rotation=90)











plt.tight_layout()
plt.show()