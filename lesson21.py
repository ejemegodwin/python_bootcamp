# Calcualate is here
student = {
    "name": "Godwin",
    "age": 24,
    "country": "Nigeria"
}

# Loop through the keys
for key in student:
    print(key)

# Access the values
for key in student:
    print(student[key])

# Get both key and value
for key, value in student.items():
    print(key, value)

# Exercise
person = {
    "name": "Godwin",
    "age": 24,
    "profession": "Software Developer"
}

for key in person:
    print(key)

for key in person:
    print(person[key])

for key, value in person.items():
    print(key, value)


book = {
    "title": "Python Basics",
    "pages": 300
}

for key, value in book.items():
    print(f"{key}: {value}")

scores = [70, 85, 92, 60]
total = 0

for score in scores:
    total += score
    print(total)