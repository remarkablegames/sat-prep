import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import numpy as np
import os

CWD = os.path.dirname(__file__)

def path(filename: str) -> str:
    """
    Gets the absolute path of the file.

    Args:
        filename: The filename.

    Returns:
        The absolute path of the file.
    """
    return os.path.join(CWD, filename + '.png')

plt.figure(figsize=(10, 6))
plt.rcParams['font.family'] = fm.FontProperties(fname=os.path.join(CWD, '../../fonts/PTSerif.ttf')).get_name()
plt.rcParams['font.size'] = 14

# test4_module1_question13
plt.clf()
categories = ['California', 'Wisconsin', 'New York', 'Pennsylvania', 'Iowa', 'Washington']
values = [2700, 1300, 1100, 800, 750, 700]
plt.bar(categories, values, color='lightslategray', width=0.5)
plt.yticks(np.arange(0, 2800, step=200))
plt.xlabel('State')
plt.ylabel('Number of organic farms')
plt.title('US States with the Greatest Number of Organic Farms in 2016')
plt.grid(axis='y', linestyle='solid')
plt.savefig(path('test4_module1_question13'))

# test4_module1_question15
plt.clf()
col_labels = ['Element', 'SPC', 'AST', 'HTC', 'OCC']
data = [
    ['iron', '20%', '28%', '90%', '98%'],
    ['potassium', '44%', '74%', '97%', '100%'],
    ['sodium', '45%', '75%', '99%', '100%']
]
fig, ax = plt.subplots()
ax.axis('off')
ax.set_title('Ablation Rates for Three Elements in Cosmic Dust, by\nDust Source', y=0.7)
table = ax.table(cellText=data, loc='center', cellLoc='center', colLabels=col_labels)
table.scale(1.2, 2)
plt.savefig(path('test4_module1_question15'))
