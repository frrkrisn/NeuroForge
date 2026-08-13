weight = 5

learning_rate = 0.1

for step in range(10):

    gradient = 2 * weight

    weight = weight - learning_rate * gradient

    print(
        f"Step {step+1}:",
        round(weight, 4)
    )