value = None

if value is None:
    print("The value is None")
else:
    print("The value is not None")



value = None

if value:
    print("This will not run, because None is falsy")
else:
    print("None is treated as False in conditions")
