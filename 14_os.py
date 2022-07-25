import os

path = r"C:\Users\Suresh Arunachalam\Desktop\Projects\Data_Extraction\Output"

# print(os.path.isfile(path))
# print(os.path.isdir(path))
# print(os.path.exists(path))
for file in os.listdir(path):
    if os.path.isfile(path + "/" + file):
        print(file)