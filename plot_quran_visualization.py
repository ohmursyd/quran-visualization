import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from quran_data import QURAN_DATA

def set_size(w, h, ax=None):
    """Adjust the figure size"""
    if not ax:
        ax = plt.gca()
    l = ax.figure.subplotpars.left
    r = ax.figure.subplotpars.right
    t = ax.figure.subplotpars.top
    b = ax.figure.subplotpars.bottom
    figw = float(w)/(r-l)
    figh = float(h)/(t-b)
    ax.figure.set_size_inches(figw, figh)

# Create DataFrame from the imported data
df = pd.DataFrame(QURAN_DATA)

# Reverse the DataFrame so first surah starts on the right
df = df.iloc[::-1]

# Create the plot
fig, ax = plt.subplots()
ax.scatter(df['No'], df['No_of_ayat'])
plt.xticks(df['No'], df['No'], rotation=90)  # Temporarily using numbers instead of names
plt.xlabel('Surah')
plt.ylabel('Number of Ayat')
plt.grid(True)
plt.subplots_adjust(bottom=0.3)
set_size(20, 12)

# Flip the x-axis direction
ax.set_xlim(ax.get_xlim()[::-1])

# Draw Lam-Lam-Ha with fill first
array_lam1 = [105, 106, 101, 82, 73, 65, 54, 52, 48, 41, 17, 11, 6, 4, 0, 
              18, 58, 59, 71, 77, 86, 87, 91, 94, 88]
array_lam2 = [106, 107, 102, 83, 74, 66, 55, 53, 49, 42, 18, 12, 7, 5, 3, 
              19, 59, 60, 72, 78, 87, 88, 92, 95, 89]

# Create a polygon for the Lam-Lam-Ha shape
polygon_x = []
polygon_y = []

# Forward path (first half)
for p in range(len(array_lam1) // 2):
    lam_X = df.iloc[array_lam1[p]:array_lam2[p]]['No'].tolist()
    lam_Y = df.iloc[array_lam1[p]:array_lam2[p]]['No_of_ayat'].tolist()
    polygon_x.extend(lam_X)
    polygon_y.extend(lam_Y)

# Return path (second half)
for p in range(len(array_lam1) // 2, len(array_lam1)):
    lam_X = df.iloc[array_lam1[p]:array_lam2[p]]['No'].tolist()
    lam_Y = df.iloc[array_lam1[p]:array_lam2[p]]['No_of_ayat'].tolist()
    polygon_x.extend(lam_X)
    polygon_y.extend(lam_Y)

# Close the polygon by connecting back to the start
polygon_x.append(polygon_x[0])
polygon_y.append(polygon_y[0])

# Fill the Lam-Lam-Ha shape first
plt.fill(polygon_x, polygon_y, color='orange', alpha=0.8)

# Draw the outline after the fill
outline_x = []
outline_y = []

# Forward path (first half)
for p in range(len(array_lam1) // 2):
    lam_X = df.iloc[array_lam1[p]:array_lam2[p]]['No'].tolist()
    lam_Y = df.iloc[array_lam1[p]:array_lam2[p]]['No_of_ayat'].tolist()
    outline_x.extend(lam_X)
    outline_y.extend(lam_Y)
    
    # Connect to next segment if not last
    if p < len(array_lam1) // 2 - 1:
        connect_X = [lam_X[-1], df.iloc[array_lam1[p+1]]['No']]
        connect_Y = [lam_Y[-1], df.iloc[array_lam1[p+1]]['No_of_ayat']]
        outline_x.extend(connect_X)
        outline_y.extend(connect_Y)

# Return path (second half)
for p in range(len(array_lam1) // 2, len(array_lam1)):
    lam_X = df.iloc[array_lam1[p]:array_lam2[p]]['No'].tolist()
    lam_Y = df.iloc[array_lam1[p]:array_lam2[p]]['No_of_ayat'].tolist()
    outline_x.extend(lam_X)
    outline_y.extend(lam_Y)
    
    # Connect to next segment if not last
    if p < len(array_lam1) - 1:
        connect_X = [lam_X[-1], df.iloc[array_lam1[p+1]]['No']]
        connect_Y = [lam_Y[-1], df.iloc[array_lam1[p+1]]['No_of_ayat']]
        outline_x.extend(connect_X)
        outline_y.extend(connect_Y)

# Close the outline by connecting back to start
outline_x.append(outline_x[0])
outline_y.append(outline_y[0])

# Draw the complete outline
plt.plot(outline_x, outline_y, linewidth=2.0, color='purple')

# Draw Alif separately with purple color
array_alif1 = [112, 107, 108, 109, 113]
array_alif2 = [113, 108, 109, 110, 114]
temp1 = df.iloc[113:114]['No']
temp2 = df.iloc[113:114]['No_of_ayat']

for z in range(len(array_alif1)):
    alif_X = df.iloc[array_alif1[z]:array_alif2[z]]['No']
    alif_Y = df.iloc[array_alif1[z]:array_alif2[z]]['No_of_ayat']
    temp1 = pd.concat([temp1, alif_X])
    temp2 = pd.concat([temp2, alif_Y])
    plt.plot(temp1, temp2, linewidth=2.0, color='purple')

# Draw Alif separately with fill
array_alif1 = [112, 107, 108, 109, 113]
array_alif2 = [113, 108, 109, 110, 114]

# Create polygon points for Alif - only for the internal area
alif_x = []
alif_y = []

# Get the first point
first_x = df.iloc[array_alif1[0]]['No']
first_y = df.iloc[array_alif1[0]]['No_of_ayat']
alif_x.append(first_x)
alif_y.append(first_y)

# Forward path
for z in range(len(array_alif1)):
    segment_X = df.iloc[array_alif1[z]:array_alif2[z]]['No'].tolist()
    segment_Y = df.iloc[array_alif1[z]:array_alif2[z]]['No_of_ayat'].tolist()
    alif_x.extend(segment_X)
    alif_y.extend(segment_Y)
    plt.plot(segment_X, segment_Y, linewidth=2.0, color='purple')
    
    # Connect to next segment if not last
    if z < len(array_alif1) - 1:
        connect_X = [segment_X[-1], df.iloc[array_alif1[z+1]]['No']]
        connect_Y = [segment_Y[-1], df.iloc[array_alif1[z+1]]['No_of_ayat']]
        alif_x.extend(connect_X)
        alif_y.extend(connect_Y)
        plt.plot(connect_X, connect_Y, linewidth=2.0, color='purple')

# Close the shape by connecting back to the first point
alif_x.append(first_x)
alif_y.append(first_y)

# Fill Alif area
plt.fill(alif_x, alif_y, color='orange', alpha=0.8)

plt.show() 