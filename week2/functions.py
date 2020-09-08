def line_func(z):
    return 2*z + 1


result = line_func(99)

def greet_me(name, time_of_day):
    # Morning, Afternoon, Evening
    greeting = ""

    if time_of_day == "Morning":
        greeting = "Good morning"
    elif time_of_day == "Afternoon":
        greeting = "Good Afternoon"
    elif time_of_day == "Evening":
        greeting = "Good Evening"
    else:
        greeting = "Hello"

    return f"{greeting} {name}"


result = greet_me("SBK", "Morning")

print(result)

