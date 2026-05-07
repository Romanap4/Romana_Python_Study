results = ["Mario", "Luigi"]

results.append("Princess")
results.append("Yoshi")
results.append("Koopa Troopa")
results.append("Toad")

# Adding multiple elements at a time:
results.append(["Bowser", "Donkey Kong Jr."])
results.remove(["Bowser", "Donkey Kong Jr."])
# EXTEND METHOD - use to add elements from a different list instead of appending that list itself:
results.extend(["Bowser", "Donkey Kong Jr."])

print(results)

results_2 = ["Mario", "Luigi", "Princess", "Yoshi", "Koopa Troopa", "Toad", "Bowser", "Donkey Kong Jr."]

results_2.remove("Bowser")
results_2.insert(0, "Bowser")
results_2.reverse()

print(results_2)
