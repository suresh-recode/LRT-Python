import pandas

df = pandas.read_excel('Test_File.xlsx', sheet_name="Sheet1")
# df = df.loc[df['Gender'] != 'Male']
df['Phone'] = "99999991111"
new_data = {'Name': "Sakthi", "Age": 30, "Gender": "Male", "Phone": 988761222}
df = df.append(new_data, ignore_index=True)
df.to_excel('Test_File.xlsx', index=False)

