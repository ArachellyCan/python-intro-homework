# Page 1 (try/except + finally section):
try:
    with open("data.txt", "r") as f:
        content = f.read()
    print("File read successfully.")
except FileNotFoundError:
    print("File not found.")

# Page 3 (Crashing vs. Graceful Degradation):
# the same idea inside a function, with a friendly message