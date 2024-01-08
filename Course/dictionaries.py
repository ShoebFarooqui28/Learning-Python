# Dictionaries = A changeable, unordered collection of unique key:value pairs fast because they use hashing, allow us to access a value quickly.

capitals = {"USA": "Washington DC",
            "India": "New Delhi",
            "Japan": "Tokyo"}

capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "New York"})
capitals.pop("India")
# capitals.clear()

print(capitals["USA"])
print(capitals["Japan"])
print(capitals.get("Germany")) # whether this key is there or not
print(capitals.keys()) # print keys
print(capitals.values()) # print values
print(capitals.items()) # print entire dictionary

for key,value in capitals.items():
    print(key,value)


