def credit_check(str):
    # num = [int(i) for i in reversed(str)]
    # for i in range(0, len(list(reversed(str))), 2):
    #     print(list(reversed(str))[i])
    # return 0

    x = sum([i*2 for i in range(0, len(list(reversed(str))), 2)])
    return x

# Your Luhn Algorithm Here
# Expected Output:
# If it is valid, print "The number is valid!"
# If it is invalid, print "The number is invalid!"

print(credit_check("5541808923795240"))