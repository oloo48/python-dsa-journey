student = {
    "name": "oloo48",
    "age": 20,
    "country": "Kenya",
    "language": "Python"
    "is_learning": True
}

print("Student dict:", student)
print()

print("---- Accessing values in the dictionary by key--")
print("Name:", student["name"])
print("Age:", student["age"])
print("Country:", student["country"])
print("Language:", student["language"])
print("Is Learning:", student["is_learning"])

print( "---- Accessing values in the dictionary using get() method--")
print("Name:", student.get("name"))
print("Age:", student.get("age"))
print("Country:", student.get("country"))
print("Language:", student.get("language"))
print("Is Learning:", student.get("is_learning"))
print("Grade:", student.get("grade", "Not Available"))  # Using get() with a default value
print("\n------ADD & UPDATE ----")
student["level"] = "Computer Science"
student["age"] = 21
print["After changes:", student]

print("\n-----Remove----")
removed_value = student.pop("is_learning")
print("Now:", student)

print("\n-----CHECK & LOOP----")
print("HAS 'name'?", "name" in student)
print("HAS 'score'?", "score" in student)
print("\nKeys only:", list(student.keys()))
print("Values only:", list(student.values()))
print("Items:", list(student.items()))
print("\n All Pairs:")
for key, value in student.items():
    print(f" {key}: {value}")
    print("\n-----FREQUENCY COUNT----")
    message = "dsa is awesome and powerful"
    counts = {}
    for char in message:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    print("Message:", message)
    print("\nCharacter  Count:", counts)
    for ch, num in counts.items():
        print(f" {ch}: {num} time(s)")

        print("\n-----NESTED DATA----")
        users = {
            "oloo48": {
                "name": "oloo48",
                "age": 20,
                "track": "DSA",
                "Skills": ["Python", "Git",]
            },
            "student2": {
                "name": "student2",
                "age": 22,
                "track": "Web Development",
                "Skills": ["HTML", "CSS", "JavaScript"]
            }
        }
        print("oloo48's Skills:", users["oloo48"] ["Skills"])
        print("student2's age:", users["student2"]["age"])
