import pandas
import warnings
warnings.filterwarnings('ignore')

f = open(r'C:\Users\Suresh Arunachalam\Downloads\Sample.txt', "r")
data = f.readlines()
f.close()

header = data[0][:-1]

header_list = header.split(',')

df = pandas.DataFrame(
    columns=header_list)

row = data[1:]
for val in row:
    val = val[:-1].split(',')
    df = df.append({header_list[0]: val[0],
                    header_list[1]: val[1],
                    header_list[2]: val[2],
                    header_list[3]: val[3],
                    header_list[4]: val[4],
                    header_list[5]: val[5],
                    header_list[6]: val[6],
                    }, ignore_index=True)
df['Combine'] = df['Date'].astype(str) + df['Time'].astype(str)
df['Combine'] = df['Combine'].replace(":", "")
df.to_excel("txt_to_excel.xlsx", index=False)