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
data = [
    ['Element', 'SPC', 'AST', 'HTC', 'OCC'],
    ['iron', '20%', '28%', '90%', '98%'],
    ['potassium', '44%', '74%', '97%', '100%'],
    ['sodium', '45%', '75%', '99%', '100%']
]
fig, ax = plt.subplots(figsize=(8, 6))
ax.axis('off')
ax.set_title('Ablation Rates for Three Elements in Cosmic Dust, by\nDust Source', y=0.62)
table = ax.table(cellText=data[1:], loc='center', cellLoc='center', colLabels=data[0])
table.auto_set_font_size(False)
table.set_fontsize(16)
table.scale(1.5, 1.5)
plt.tight_layout()
plt.savefig(path('test4_module1_question15'))

# test4_module1_question17
plt.clf()
data = [
    ['Plant\nspecies', 'Mycorrhizal\nhost', 'Average mass of plants\ngrown in soil containing\nmycorrhizal fungi\n(in grams)', 'Average mass of plants\ngrown in soil treated\nto kill fungi (in grams)'],
    ['Corn', 'yes', '15.1', '3.8'],
    ['Marigold', 'yes', '10.2', '2.4'],
    ['Broccoli', 'no', '7.5', '7'],
]
fig, ax = plt.subplots(figsize=(8, 6))
ax.axis('off')
ax.set_title('Effects of Mycorrhizal Fungi on 3 Plant Species', y=0.72)
table = ax.table(cellText=data[1:], loc='center', cellLoc='center', colLabels=data[0], colWidths=[0.2, 0.2, 0.4, 0.4])
cell_dict = table.get_celld()
for i, col in enumerate(data[0]):
    cell_dict[(0, i)].set_height(0.1)
table.auto_set_font_size(False)
table.set_fontsize(16)
table.scale(1, 2)
plt.tight_layout()
plt.savefig(path('test4_module1_question17'))
