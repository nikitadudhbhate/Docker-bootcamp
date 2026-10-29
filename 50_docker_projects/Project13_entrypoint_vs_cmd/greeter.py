import sys

# sys.argv contains all arguments passed to the script
if len(sys.argv) > 1:
    name = " ".join(sys.argv[1:])
else:
    name = "World"

print(f"👋 Hello, {name}! Welcome to the automated DevOps pipeline.")
