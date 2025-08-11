isOld = True
hasFlu = False

# AND: both must be True
if isOld and hasFlu:
    print("Old and sick")
else:
    print("Condition for 'and' not met")

# OR: at least one must be True
if isOld or hasFlu:
    print("Either old or sick (or both)")
else:
    print("Neither old nor sick")

# NOT: negates the value
if not hasFlu:
    print("Not sick")
else:
    print("Sick")
