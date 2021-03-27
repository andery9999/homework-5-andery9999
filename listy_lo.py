if __name__ == "__main__":

    food = ["rice", "beans"]

    food.append("broccoli")

    food.extend(("bread", "pizza"))

    print(food[:2])

    print(food[-1])

    breakfast = "eggs,fruit,orange juice".split(",")

    print(f"The length of breakfast list is {len(breakfast)}.")

    user_list = []
    user_input = "start"
    while user_input != "stop":
        user_input = input("Please enter a floating-point value (enter stop to stop):\n")
        if user_input == "stop":
            breakpoint
        else:
            try:
                user_input = float(user_input)
            except:
                print("Invalid input. Please enter a number or stop.")
            else:
                user_list.append(user_input)
    print(f"You have entered {len(user_list)} numbers.")
    print(f"The average value you entered is: {sum(user_list)/float(len(user_list))}")
    print(f"The minimum value you entered is: {min(user_list)}")
    print(f"The maximum value you entered is : {max(user_list)}")