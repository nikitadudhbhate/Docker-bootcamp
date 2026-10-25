import datetime
import os

data_file = "/data/notes.txt"
os.makedirs(os.path.dirname(data_file), exist_ok=True)

now = str(datetime.datetime.now())
with open(data_file, "a") as f:
    f.write(f"Container entry saved at: {now}\n")

print("📝 Successfully wrote entry to volume!")
print("--- Reading Entire Persistent History ---")
with open(data_file, "r") as f:
    print(f.read())
