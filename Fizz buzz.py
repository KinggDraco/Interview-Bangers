def FizzBuzz(range_of_numbers, m1, m2):
    listInts = []

    for integers in range(1, (range_of_numbers + 1)):

        if integers % m1 == 0 and integers % m2 == 0:
            listInts.append("FizzBuzz")
        elif integers % m1 == 0:
            listInts.append("Fizz")
        elif integers % m2 == 0:
            listInts.append("Buzz")
        elif integers % m1 != 0 and integers % m2 != 0:
            listInts.append(integers)
    #parse text
    print(str(listInts).translate(str.maketrans({'[': '', ']': '', '\'': ''})))
