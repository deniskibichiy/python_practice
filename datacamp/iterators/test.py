import sys

fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# 1. List Comprehension (Square Brackets)
fellow1 = [member for member in fellowship if len(member) >= 7]

# 2. Generator Expression (Parentheses)
fellow2 = (member for member in fellowship if len(member) >= 7)

# Inspect

print("=== TYPES ===")
print("fellow1 type:", type(fellow1))
print("fellow2 type:", type(fellow2))

print("\n=== PRINTING VALUES DIRECTLY ===")
print("fellow1 content:", fellow1)
print("fellow2 content:", fellow2)

print("\n=== MEMORY USAGE (bytes) ===")
print("fellow1 size:", sys.getsizeof(fellow1))
print("fellow2 size:", sys.getsizeof(fellow2))