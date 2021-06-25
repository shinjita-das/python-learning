# Input: N, entered by the user
# Output: List of prime numbers before N
# Conditions: N>2


# 10, 2,3,4,5,6,7,8,9,
limit = int(input("Enter the limit:"))
if limit <= 2:
    print("Invalid input")
else:
    output_list = [1]
    for number in range(2, limit):
        print(number)
        prime_number = True
        for x in range(2, number):
            if number % x == 0:
                prime_number = False
                break
        if prime_number:
            output_list.append(number)
    print(output_list)


print(output_list)