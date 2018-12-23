from matplotlib import pyplot as plt

labels = ['WS.Reputation.1', 'SONAR.Heur.RGCg336', 'Sonar.Heur.RGC!g336',
          'Heur.AdvML.B', 'Trojan.Gen.2', 'Heur.AdvML.C', 'Others']
sizes = [1001, 180, 124, 79, 40, 33, 129]
explode = [0.1, 0, 0, 0, 0, 0, 0]

ax = plt.subplot()
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, counterclock=False, startangle=90)
ax.axis('equal')
ax.set_xlabel('File detections set by humans')
plt.show()
