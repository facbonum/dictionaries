# Dictionaries
band = {
    "vocals" : "Plant",
    "guitar" : "Page"
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)

print(type(band))
print(len(band))


# Access items
print(band["vocals"])
print(band.get("guitar"))

# List all keys
print(band.keys())

# List all values
print(band.values())

# List of key/value pairs as tuples
print(band.items())

# Verify a key exists
print("guitar" in band)
print("rectangle" in band)

# Change values
band["vocals"] = "Coverdale"
band.update({"bass" : "JPJ"})
print(band)

# remove items
print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem()) #tuple
print(band)

# Delete and clear
band["drums"] = "Bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2

# Copy dictionaries

# band2 = band # create a reference, same place in memory, not a copy
# print("Bad copy!")
# print(band2)
# print(band)

# band2["drums"] = "Dave"
# print(band)

band2 = band.copy()
band2["drums"] = "Dave"
print("Good copy!")
print(band)
print(band2)

# or use the dict() constructor fucntion
band3 = dict(band)
print("Good copy!")
print(band3)

# Nested dictionaries
member1 = {
    "name": "Plant",
    "instrument": "vocals"
}
member2 = {
    "name": "Page",
    "instrument": "guitar"
}
band = {
    "member1": member1, # careful not to quote the value of the key, it is a reference
    "member2": member2
}
print(band)

print(band["member1"]["name"])

# Sets

nums = {1, 2, 3, 4}

nums2 = set((1, 2, 3, 4))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))