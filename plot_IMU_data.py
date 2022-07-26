import pandas
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()

path = filedialog.askopenfilename(
    title = "open csv file",
    filetypes = [("csv file", ".csv")],
    initialdir = "./"
)

df = pandas.read_csv(path)

root.withdraw()

fig, axs = plt.subplots(2, 3, tight_layout=True)
axs = axs.reshape([6,1])
ax_names = ['acc x', 'acc y', 'acc z', 'gyro x', 'gyro y', 'gyro z']
# ax_limits = [10, 10, 10, 100, 100, 100]

for i in range(6):
  axs[i,0].set_title(ax_names[i])
  # axs[i,0].set_ylim([-ax_limits[i],ax_limits[i]])
  axs[i,0].plot(df.time, df[df.columns[i+1]])
