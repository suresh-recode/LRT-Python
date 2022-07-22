import traceback
try:
    print("Line-2")
    print(1/0)
    print("Line-4")

except Exception as e:
    print(traceback.format_exc())