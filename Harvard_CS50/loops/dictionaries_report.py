# def main():
#     spacecraft = {"name": "Voyager 1", "distance": 163}
#     print(create_report(spacecraft))


# def create_report(spacecraft):
#     return f"""
#     ======== REPORT ========

#     Name: {spacecraft["name"]}
#     Distance: {spacecraft["distance"]} AU

#     ========================
#     """

# main()

# AU --> astronomical units

# Running the file wihtout the "distance" key causes a KeyError -> because we are trying to access a key that doesn't exist in the dictionary.
# An additional key can be added subsequently, as shown on line 25.

# def main():
#     spacecraft = {"name": "James Webb Space Telescope"}
#     spacecraft["distance"] = 0.01
#     print(create_report(spacecraft))

# def create_report(spacecraft):
#     return f"""
#     ======== REPORT ========

#     Name: {spacecraft["name"]}
#     Distance: {spacecraft["distance"]} AU

#     ========================
#     """

# main()

# GET METHOD -> can be used to try to access a key; if that key doesn't exist, it will output another value we specify instead.
# You can use it to try to get a key if you are unsure whether it exist and return a different value in case it doesn't.

# def main():
#     spacecraft = {"name": "James Webb Space Telescope"}
#     print(create_report(spacecraft))

# def create_report(spacecraft):
#     return f"""
#     ======== REPORT ========

#     Name: {spacecraft.get("name", "Unknown")}
#     Distance: {spacecraft.get("distance", "Unknown")} AU

#     ========================
#     """

# main()

# UPDATE METHOD -> use to add multiple keys to an existing dictionary
# The method takes as an argument another dictionary and adds the keys and values from it to the existing dictionary

def main():
    spacecraft = {"name": "James Webb Space Telescope"}
    spacecraft.update({"distance": 0.01, "orbit": "Sun"})
    print(create_report(spacecraft))

def create_report(spacecraft):
    return f"""
    ======== REPORT ========

    Name: {spacecraft.get("name", "Unknown")}
    Distance: {spacecraft.get("distance", "Unknown")} AU
    Orbit: {spacecraft.get("orbit", "Unknown")}

    ========================
    """

main()
