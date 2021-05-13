dict = {"key_1": 12,
        "key_2": True, 3: [1, 2, 3],
        ("key_3", 7): [1.2],
        -8: 3}

print(dict.values())
# print(dict.items())
# print(dict["key_2"])  # True
# print(dict["key_3"])  # error
# print(dict["key_3", 7]

# print(dict.get("key_3"))  -> None

# set = set()
# print(type(set)) -> type tuple

# print("key_3" in dict)  -> False


# dict["key_3"] = False
# dict.clear()

dict.update({"key_4": 3, "key_5": 4})

# dict.pop("key_2")
# dict.popitem()
print(dict)