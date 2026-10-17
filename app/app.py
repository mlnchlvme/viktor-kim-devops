import os
import time
 
name = os.getenv("STUDENT_NAME", "Viktor")
surname = os.getenv("STUDENT_SURNAME", "Kim")
group = os.getenv("STUDENT_GROUP", "IT2-2313")
student_id = os.getenv("STUDENT_ID", "37145")
 
print("=" * 32, flush=True)
print("DevOps Student Application", flush=True)
print("=" * 32, flush=True)
print("", flush=True)
print(f"Name: {name}", flush=True)
print(f"Surname: {surname}", flush=True)
print(f"Group: {group}", flush=True)
print(f"Student ID: {student_id}", flush=True)
print("", flush=True)
print("Application is running successfully!", flush=True)
while True:
   time.sleep(30)
