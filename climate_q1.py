import sqlite3

conn = sqlite3.connect('climate.db')
cursor = conn.cursor()

years = []
co2 = []
temp = []

cursor.execute('SELECT year, co2, temperature FROM climate_data')
data = cursor.fetchall()

for row in data:
    years.append(row[0])
    co2.append(row[1])
    temp.append(row[2])

conn.close()

plt.savefig("co2_temp_1.png")
plt.show()
