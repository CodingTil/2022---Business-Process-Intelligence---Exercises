import matplotlib.pyplot as plt
import os
ywerte = [2366, 552, 228, 213, 164, 109, 69, 62, 48, 40]
xwerte = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
plt.bar(xwerte, ywerte)
plt.ylabel("Absolute Häufigkeit")
plt.savefig(os.path.dirname(os.path.abspath(__file__)) + "/../img/RapidMiner_c_Chart.png")