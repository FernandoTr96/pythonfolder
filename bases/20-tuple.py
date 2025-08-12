# Tuples are ordered
# Tuples are immutable
# Admit duplicates
# Tuples has indexes
# Tuples has only two methods
myTuple = (1, 2, 3, 4, 5, 5, "Hello",True)
print(myTuple)

# count value in a tuple
print(myTuple.count(5))

# Get index of values, but the first index
print(myTuple.index(5))

# hashable tuple
locations = {
    (19.4326, -99.1332): "Mexico City",
    (25.6866, -100.3161): "Monterrey"
}
