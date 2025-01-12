import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset from the Excel file
df = pd.read_excel('C:/Users/harsh.HARSHIKALA/Downloads/dhruvil/crop_data.xlsx')

# Calculate the adjusted water absorption capacity per unit area
df['AdjustedWaterAbsorption'] = df['RootDepth'] * df['SoilWaterRetention'] * (1 - df['SoilMoistureLevel'] / 100) * 10

# Setting up the color palette using seaborn
cmap = sns.light_palette("navy", as_cmap=True)

# Plotting the bar graph with enhanced aesthetics
plt.figure(figsize=(14, 10))
bars = plt.bar(df['Crop'], df['AdjustedWaterAbsorption'], color=sns.color_palette("Blues_d", len(df)))

# Adding annotations on top of the bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), 
             ha='center', va='bottom', fontsize=12, color='black')

# Adding labels, title, and grid
plt.xlabel('Crop', fontsize=14)
plt.ylabel('Adjusted Water Absorption (cubic meters)', fontsize=14)
plt.title('Adjusted Water Absorption by Crop Considering Soil Moisture & Root Depth', fontsize=16, fontweight='bold')
plt.xticks(rotation=45, fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adding a secondary y-axis for soil moisture levels and root depth
ax2 = plt.gca().twinx()
ax2.plot(df['Crop'], df['SoilMoistureLevel'], color='green', marker='o', linestyle='--', label='Soil Moisture Level (%)')
ax2.plot(df['Crop'], df['RootDepth'], color='red', marker='o', linestyle='-', label='Root Depth (meters)')
ax2.set_ylabel('Soil Moisture Level (%) & Root Depth (meters)', fontsize=14)
ax2.tick_params(axis='y', colors='black')
ax2.legend(loc='upper left')

# Adding annotations to the secondary y-axis line plots
for i, txt in enumerate(df['SoilMoistureLevel']):
    ax2.annotate(f'{txt}%', (df['Crop'][i], df['SoilMoistureLevel'][i]), textcoords="offset points", xytext=(0,10),
                 ha='center', fontsize=10, color='green')

for i, txt in enumerate(df['RootDepth']):
    ax2.annotate(f'{txt}m', (df['Crop'][i], df['RootDepth'][i]), textcoords="offset points", xytext=(0,-15),
                 ha='center', fontsize=10, color='red')

plt.show()