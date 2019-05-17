import csv
import matplotlib.pyplot as plt
import numpy as np

players = []
with open('data.csv', 'r', encoding='utf8') as fifa:
    reader = csv.DictReader(fifa)
    # print(reader)
    for i in reader:
        players.append(dict(i))
Age = []
Overall = []
for i in range(len(players)):
    Age.append(int(players[i]['Age']))
    Overall.append(int(players[i]['Overall']))

umur = np.array(Age)
skill = np.array(Overall)
# print(len(umur))
umur1 = []
umur2 = []
umur3 = []
umur4 = []
skill1 = []
skill2 = []
skill3 = []
skill4 = []

for i in range(len(umur)):
    if umur[i] > 25 and skill[i] > 85:
        umur1.append(umur[i])
        skill1.append(skill[i])
    elif umur[i] > 25 and skill[i] <= 85:
        umur2.append(umur[i])
        skill2.append(skill[i])
    elif umur[i] <= 25 and skill[i] > 85:
        umur3.append(umur[i])
        skill3.append(skill[i])
    else:
        umur4.append(umur[i])
        skill4.append(skill[i])

plt.figure('BOLA')
plt.subplot(111)
plt.title('FIFA 2019')
plt.xlabel('Umur')
plt.ylabel('Overall')
plt.xticks(rotation = 90)               # atur rotasi dari value x dan y
plt.yticks(rotation = 60)
# plt.grid(True)

plt.scatter(umur1,skill1, color='r', marker='.')
plt.scatter(umur2,skill2, color='g', marker='.')
plt.scatter(umur3,skill3, color='b', marker='.')
plt.scatter(umur4,skill4, color='y', marker='.')

plt.legend(
    ['Aged Talented', 'Aged Non-Talented ', 'Young Talented', 'Young RAW'],
    scatterpoints=1,
    loc='lower left',
    ncol=3,
    fontsize=8
) 


plt.tight_layout()
plt.show()
