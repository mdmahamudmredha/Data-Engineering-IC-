"""
==============================================
Session 2 Homework: Lists, Dictionaries, 
Functions & File Handling
==============================================
"""

# ============================================
# TASK 1: Lists
# ============================================

print("""
# ============================================
# TASK 1: Lists
# ============================================
""")

# 1a
cities = ["Dhaka", "Chattogram", "Khulna", "Sylhet", "Barisal"]
print(f"Initial cities: {cities}")

# 1b
cities.append("Rajshahi")
print(f"After adding Rajshahi: {cities}")

# 1c
removed_city = cities.pop(1)
print(f"Removed second city ({removed_city}): {cities}")

# 1d
sorted_cities = sorted(cities)
print(f"Sorted cities: {sorted_cities}")


# ============================================
# TASK 2: List Comprehension
# ============================================

print("""
# ============================================
# TASK 2: List Comprehension
# ============================================
""")

prices_bdt = [1200, 450, 3200, 890, 5600, 150]

# 2a
expensive = [price for price in prices_bdt if price > 1000]
print(f"Expensive items: {expensive}")

# 2b
with_vat = [price * 1.15 for price in prices_bdt]
print(f"With VAT: {with_vat}")


# ============================================
# TASK 3: Tuples & Sets
# ============================================

print("""
# ============================================
# TASK 3: Tuples & Sets
# ============================================
""")

# 3a
info = ("Mredha", 25, "Dhaka")
name, age, city = info
print(f"{name}, {age}, from {city}")

# 3b
raw_ids = [101, 203, 101, 305, 203, 407, 305, 101]
unique_ids = list(set(raw_ids))
print(f"Unique IDs: {unique_ids}")


# ============================================
# TASK 4: Dictionaries
# ============================================

print("""
# ============================================
# TASK 4: Dictionaries
# ============================================
""")

# 4a
student = {
    "name": "Md. Mahamud Mredha",
    "department": "CSE",
    "cgpa": 3.49,
    "semester": 12
}
print(f"Student dict: {student}")

# 4b
student["university"] = "Daffodil International University"
print(f"After adding university: {student}")

# 4c
print("All key-value pairs:")
for key, value in student.items():
    print(f"{key}: {value}")

# 4d
email = student.get("email", "not provided")
print(f"Email: {email}")


# ============================================
# TASK 5: Functions
# ============================================

print("""
# ============================================
# TASK 5: Functions
# ============================================
""")

# 5a
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

print(f"Average: {calculate_average([80, 92, 75, 88, 95])}")

# 5b
def get_grade(score=0):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print(f"92 -> {get_grade(92)}")
print(f"75 -> {get_grade(75)}")
print(f"45 -> {get_grade(45)}")

# 5c
def summarize(scores):
    count = len(scores)
    avg = sum(scores) / count
    return count, avg

count, avg = summarize([85, 90, 78, 92])
print(f"Count: {count}, Average: {avg}")


# ============================================
# TASK 6: File Handling
# ============================================

print("""
# ============================================
# TASK 6: File Handling
# ============================================
""")

import csv
import json

students = [
    {"name": "Rahim", "dept": "CSE", "cgpa": 3.65},
    {"name": "Fatima", "dept": "EEE", "cgpa": 3.82},
    {"name": "Karim", "dept": "CSE", "cgpa": 3.21},
    {"name": "Nadia", "dept": "BBA", "cgpa": 3.90},
    {"name": "Arif", "dept": "EEE", "cgpa": 2.95},
]

# 6a: Write CSV
with open("students.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "dept", "cgpa"])
    writer.writeheader()
    writer.writerows(students)

print("students.csv written successfully")

# 6b: Read CSV
print("Reading students.csv:")
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

# 6c: JSON summary
cgpas = [s["cgpa"] for s in students]

summary = {
    "total_students": len(students),
    "average_cgpa": round(calculate_average(cgpas), 2),
    "highest_cgpa": max(cgpas),
    "lowest_cgpa": min(cgpas)
}

with open("summary.json", "w") as f:
    json.dump(summary, f, indent=4)

print("summary.json written successfully")

# verify
with open("summary.json") as f:
    result = json.load(f)
    print("Summary JSON:", result)


print("\nHomework complete!")