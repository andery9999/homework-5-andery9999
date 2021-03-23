if __name__ == "__main__":

    food = ["rice", "beans"]

    food.append("broccoli")

    food.extend(("bread", "pizza"))

    print(food[:2])

    print(food[-1])

    breakfast = "eggs,fruit,orange juice".split(",")

    print(len(breakfast) is 3)

    user_list = ["start"]
    while user_list[-1] != "stop" :
        user_input = input("Please enter a floating-point value (enter stop to stop):\n")
        user_list.append(user_input)
    user_list.remove("stop")
    user_list.remove("start")
    math_list = [float(i) for i in user_list]
    print(f"The average value you entered is: {sum(math_list)/float(len(math_list))}")
    print(f"The minimum value you entered is: {min(math_list)}")
    print(f"The maximum value you entered is : {max(math_list)}")