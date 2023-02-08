import matplotlib.pyplot as plt
import numpy as np

def pie_chart(var_dict, results_path):
    titles = list(var_dict.keys())
    for title in titles:
        label = []
        value = []
        for ky in list(var_dict[title].keys()):
            value.append(var_dict[title][ky])
            label.append(ky+f" {int(100*var_dict[title][ky]/sum(var_dict[title].values()))}%")
        value = np.array(value)
        plt.pie(value, labels = label)
        plt.title(title, y = -0.1)
        plt.savefig(f"{results_path}/pie_chart_{title}.jpeg")
        plt.close()