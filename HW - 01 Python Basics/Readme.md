# Session 1 Homework: Python Basics

## Topics Covered

Variables, Data Types, Operators, Strings, Booleans, Type Conversion, Input/Output, Conditionals, Loops

---

## Full Code

```python
"""
==============================================
Session 1 Homework: Python Basics
Modern Data Engineering Course
==============================================
"""

# ============================================
# TASK 1: Variables & Data Types
# ============================================

pipeline_name = "user_sync_pipeline"
source_system = "crm_database"
total_records = 25000
error_count = 178
processing_time = 45.7
is_successful = True

print("""
# ============================================
# TASK 1: Variables & Data Types
# ============================================
""")

print(f"{pipeline_name} -> {type(pipeline_name)}")
print(f"{source_system} -> {type(source_system)}")
print(f"{total_records} -> {type(total_records)}")
print(f"{error_count} -> {type(error_count)}")
print(f"{processing_time} -> {type(processing_time)}")
print(f"{is_successful} -> {type(is_successful)}")


# ============================================
# TASK 2: Arithmetic Operations
# ============================================

success_count = total_records - error_count
success_rate = success_count / total_records * 100
error_rate = error_count / total_records * 100
records_per_second = total_records / processing_time

print("""
# ============================================
# TASK 2: Arithmetic Operations
# ============================================
""")

print(f"Success count: {success_count}")
print(f"Success rate: {success_rate:.2f}%")
print(f"Error rate: {error_rate:.2f}%")
print(f"Records/sec: {records_per_second:.1f}")


# ============================================
# TASK 3: String Operations
# ============================================

raw_name = "   rahim UDDIN   "
raw_email = "RAHIM@GMAIL.COM"
raw_city = "dhaka"

clean_name = raw_name.strip().title()
clean_email = raw_email.lower()
clean_city = raw_city.capitalize()

print("""
# ============================================
# TASK 3: String Operations
# ============================================
""")

print(f"Name: {clean_name}")
print(f"Email: {clean_email}")
print(f"City: {clean_city}")

summary = f"{clean_name} ({clean_email}) from {clean_city}"
print(summary)


# ============================================
# TASK 4: Type Conversion
# ============================================

str_price = "1250.75"
str_quantity = "8"
str_discount = "15"
str_in_stock = "True"

price = float(str_price)
quantity = int(str_quantity)
discount = int(str_discount)

subtotal = price * quantity
discount_amount = subtotal * discount / 100
final_total = subtotal - discount_amount

print("""
# ============================================
# TASK 4: Type Conversion
# ============================================
""")

print(f"Subtotal: {subtotal:.2f} BDT")
print(f"Discount ({discount}%): -{discount_amount:.2f} BDT")
print(f"Final Total: {final_total:.2f} BDT")


# ============================================
# TASK 5: Comparisons & Booleans
# ============================================

rows_loaded = 9500
rows_expected = 10000
null_percentage = 3.2
max_allowed_nulls = 5.0
run_time_minutes = 12
max_run_time = 15

data_complete = rows_loaded >= rows_expected
data_clean = null_percentage <= max_allowed_nulls
within_time = run_time_minutes <= max_run_time
all_checks_passed = data_complete and data_clean and within_time
any_issue = not all_checks_passed

print("""
# ============================================
# TASK 5: Comparisons & Booleans
# ============================================
""")

print(f"Data complete: {data_complete}")
print(f"Data clean: {data_clean}")
print(f"Within time: {within_time}")
print(f"All passed: {all_checks_passed}")
print(f"Any issue: {any_issue}")


# ============================================
# TASK 6: Conditionals
# ============================================

pipeline_score = 87

if pipeline_score >= 90:
    grade = "EXCELLENT"
    color = "green"
elif pipeline_score >= 70:
    grade = "GOOD"
    color = "yellow"
elif pipeline_score >= 50:
    grade = "WARNING"
    color = "orange"
else:
    grade = "CRITICAL"
    color = "red"

print("""
# ============================================
# TASK 6: Conditionals
# ============================================
""")

print(f"Pipeline Score: {pipeline_score} -> {grade} ({color})")


# ============================================
# TASK 7: For Loops
# ============================================

print("""
# ============================================
# TASK 7: For Loops
# ============================================
""")

tables = ["customers", "orders", "products", "reviews", "inventory"]
row_counts = [15000, 42000, 3500, 28000, 7200]

for table in tables:
    print(table.upper())

print("---")

for i in range(len(tables)):
    print(f"Table: {tables[i]} -> {row_counts[i]} rows")

print("---")

total = 0
for count in row_counts:
    total += count

print(f"Total rows across all tables: {total}")


# ============================================
# TASK 8: While Loop
# ============================================

print("""
# ============================================
# TASK 8: While Loop
# ============================================
""")

remaining = 7500
batch_size = 1000
batch_number = 0

while remaining > 0:
    batch_number += 1
    if remaining >= batch_size:
        processed = batch_size
    else:
        processed = remaining
    remaining -= processed
    print(f"Batch {batch_number}: processed {processed}, remaining: {remaining}")

print(f"Done! Processed in {batch_number} batches")


# ============================================
# TASK 9: Pipeline Report
# ============================================

pipeline = "ecommerce_daily_sync"
tables_processed = ["users", "orders", "products", "payments"]
total_rows = 95400
failed_rows = 1230
start_time_seconds = 0
end_time_seconds = 324

success_rows = total_rows - failed_rows
success_rate = success_rows / total_rows * 100
duration_minutes = (end_time_seconds - start_time_seconds) / 60
rows_per_second = total_rows / (end_time_seconds - start_time_seconds)

print("""
# ============================================
# TASK 9: Pipeline Report
# ============================================
""")

if success_rate >= 98:
    status = "HEALTHY"
elif success_rate >= 95:
    status = "WARNING"
else:
    status = "CRITICAL"

print("=" * 50)
print(f"  PIPELINE REPORT: {pipeline}")
print("=" * 50)
print(f"  Status: {status}")
print(f"  Duration: {duration_minutes:.1f} minutes")
print(f"  Tables processed:")
for table in tables_processed:
    print(f"    - {table}")
print(f"  Total rows: {total_rows:,}")
print(f"  Successful: {success_rows:,} ({success_rate:.1f}%)")
print(f"  Failed: {failed_rows:,}")
print(f"  Throughput: {rows_per_second:.0f} rows/sec")
print("=" * 50)


# ============================================
# BONUS: User Input Version
# ============================================

pipeline = input("Pipeline name: ")
total = int(input("Total rows: "))
failed = int(input("Failed rows: "))
time_sec = float(input("Run time (seconds): "))

success = total - failed
success_rate = success / total * 100
rows_per_sec = total / time_sec
duration_min = time_sec / 60

if success_rate >= 98:
    status = "HEALTHY"
elif success_rate >= 95:
    status = "WARNING"
else:
    status = "CRITICAL"

print("=" * 50)
print(f"  PIPELINE REPORT: {pipeline}")
print("=" * 50)
print(f"  Status        : {status}")
print(f"  Duration      : {duration_min:.1f} minutes")
print(f"  Total rows    : {total:,}")
print(f"  Successful    : {success:,} ({success_rate:.1f}%)")
print(f"  Failed        : {failed:,}")
print(f"  Throughput    : {rows_per_sec:.0f} rows/sec")
print("=" * 50)

print("\nHomework complete!")
```

---

## Output

```text
# ============================================
# TASK 1: Variables & Data Types
# ============================================
# Create variables for a data pipeline run

user_sync_pipeline -> <class 'str'>
crm_database -> <class 'str'>
25000 -> <class 'int'>
178 -> <class 'int'>
45.7 -> <class 'float'>
True -> <class 'bool'>

# ============================================
# TASK 2: Arithmetic Operations
# ============================================
# Using the variables from Task 1, calculate:

Success count: 24822
Success rate: 99.29%
Error rate: 0.71%
Records/sec: 547.0

# ============================================
# TASK 3: String Operations
# ============================================
# Given this messy data from a CSV file:

Name: Rahim Uddin
Email: rahim@gmail.com
City: Dhaka
Rahim Uddin (rahim@gmail.com) from Dhaka

# ============================================
# TASK 4: Type Conversion
# ============================================
# This data came from a CSV file — everything is a string!

Subtotal: 10006.00 BDT
Discount (15%): -1500.90 BDT
Final Total: 8505.10 BDT

# ============================================
# TASK 5: Comparisons & Booleans
# ============================================
# A data pipeline has these metrics:

Data complete: False
Data clean: True
Within time: True
All passed: False
Any issue: True

# ============================================
# TASK 6: Conditionals (if/elif/else)
# ============================================
# Write a grading system for pipeline health

Pipeline Score: 87 -> GOOD (yellow)

# ============================================
# TASK 7: For Loops
# ============================================
# Given a list of database tables and their row counts:

CUSTOMERS
ORDERS
PRODUCTS
REVIEWS
INVENTORY
---
Table: customers -> 15000 rows
Table: orders -> 42000 rows
Table: products -> 3500 rows
Table: reviews -> 28000 rows
Table: inventory -> 7200 rows
---
Total rows across all tables: 95700

# ============================================
# TASK 8: While Loop
# ============================================
# Simulate a data sync that processes 1000 records per batch

Batch 1: processed 1000, remaining: 6500
Batch 2: processed 1000, remaining: 5500
Batch 3: processed 1000, remaining: 4500
Batch 4: processed 1000, remaining: 3500
Batch 5: processed 1000, remaining: 2500
Batch 6: processed 1000, remaining: 1500
Batch 7: processed 1000, remaining: 500
Batch 8: processed 500, remaining: 0
Done! Processed in 8 batches

# ============================================
# TASK 9: Putting It All Together
# ============================================
# Build a complete pipeline status report

==================================================
  PIPELINE REPORT: ecommerce_daily_sync
==================================================
  Status: HEALTHY
  Duration: 5.4 minutes
  Tables processed:
    - users
    - orders
    - products
    - payments
  Total rows: 95,400
  Successful: 94,170 (98.7%)
  Failed: 1,230
  Throughput: 294 rows/sec
==================================================

# ============================================
# BONUS: User Input Version
# ============================================
# Uncomment and complete this section to make
# an interactive version that asks for input!

Pipeline name: Md. Mahamud Mredha's Marketing Data pipeline Report
Total rows: 10000000
Failed rows: 1000
Run time (seconds): 200
==================================================
  PIPELINE REPORT: Md. Mahamud Mredha's Marketing Data pipeline Report
==================================================
  Status        : HEALTHY
  Duration      : 3.3 minutes
  Total rows    : 10,000,000
  Successful    : 9,999,000 (100.0%)
  Failed        : 1,000
  Throughput    : 50000 rows/sec
==================================================

Homework complete!
```
