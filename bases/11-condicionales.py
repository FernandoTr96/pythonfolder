isOld = True
hasFlu = False
isStudent = False

# First condition: age
if isOld:
    print("The person is old")
else:
    print("The person is young")

# Second condition: health
if hasFlu:
    print("The person is sick")
elif not hasFlu:
    print("The person is healthy")
else:
    print("Health status unknown")

# ternary if
health_status = "The person is sick" if hasFlu else "The person is healthy"
print(health_status)