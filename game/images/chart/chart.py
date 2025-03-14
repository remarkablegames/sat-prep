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
