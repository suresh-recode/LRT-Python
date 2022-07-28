import random

choice_list = ["stone", "paper", "scissor"]

for i in range(5):
    system_choice = random.choice(choice_list)

    user_input = input("Enter your choice :").lower()

    print("System chosen : {} and User chosen : {}".
          format(system_choice, user_input))

    system_count = user_count = 0
    # if system_choice == user_input:
    #     print("Tie")

    if system_choice == "stone" and user_input == "paper":
        # print("User wins")
        user_count += 1

    elif system_choice == "stone" and user_input == "scissor":
        # print("System wins")
        system_count += 1
    elif system_choice == "paper" and user_input == "stone":
        # print("System wins")
        system_count += 1

    elif system_choice == "paper" and user_input == "scissor":
        # print("User wins")
        user_count += 1

    elif system_choice == "scissor" and user_input == "stone":
        # print("User wins")
        user_count += 1

    elif system_choice == "scissor" and user_input == "paper":
        # print("System wins")
        system_count += 1

print("system : {} and user : {}".format(system_count, user_count))