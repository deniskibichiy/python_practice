def steps(number):
    try:
        if number > 0:
            num_steps = 0
            while (number > 1):
                if number % 2 == 0:
                    num_steps +=1
                    number = number/ 2
                else:
                    num_steps += 1
                    number = (number * 3) + 1
        return num_steps
    except:
        raise ValueError("Only positive integers are allowed")
print(steps(12))
