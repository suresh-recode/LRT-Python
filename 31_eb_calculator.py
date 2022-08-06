prev_month = int(input("Previous month Unit :")) # 90
curr_month = int(input("Current month Unit :"))  # 100
type_of_usage = input("D / C :")

total_amount = 0
if type_of_usage == 'D':
    total_amount = (curr_month - prev_month) * 6
else:
    total_amount = (curr_month - prev_month) * 10
print("The unit consumed = {0} and you have to pay = {1}".format(curr_month - prev_month,
                                                                 total_amount))