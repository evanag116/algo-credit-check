def credit_check(str):
    num = [int(i) for i in str]
    doubles_of_every_other = [(( ((num[i]*2) // 10) + ((num[i]*2) % 10) ) if (num[i]*2 > 9) else num[i]*2) if i%2 == 0 else num[i] for i in range(len(num))]
    
    # return doubles_of_every_other
    return "The number is valid!" if sum(doubles_of_every_other) % 10 == 0 else "The number is invalid!"


# Your Luhn Algorithm Here
# Expected Output:
# If it is valid, print "The number is valid!"
# If it is invalid, print "The number is invalid!"

print(credit_check("5541808923795240"))