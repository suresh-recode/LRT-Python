import pandas as pd

df = pd.DataFrame(
    columns=["Name", "Age", "Gender"])

for i in range(1):
    name = input("Enter the name: ")
    age = input("Enter the age: ")
    gender = input("Enter the gender: ")
    data = {"Name": name, "Age": age, "Gender": gender}

    df = df.append(data, ignore_index=True)

df.to_excel('test.xlsx', index=False, sheet_name="Sheet2")
