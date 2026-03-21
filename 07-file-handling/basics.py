"""
Module: basics.py
Topic: File Handling Basics
Level: Intermediate

This file teaches you about:
- Opening and closing files
- Reading files
- Writing files
- File modes
- Context managers (with statement)
"""

# =============================================================================
# SECTION 1: FILE MODES
# =============================================================================

print("=" * 60)
print("FILE MODES")
print("=" * 60)

"""
File Modes:
'r'  - Read (default) - File must exist
'w'  - Write - Creates new or truncates existing
'a'  - Append - Creates new or appends to existing
'x'  - Exclusive creation - Fails if file exists
'b'  - Binary mode
't'  - Text mode (default)
'+'  - Update (read and write)

Common combinations: 'r', 'w', 'a', 'rb', 'wb', 'r+', 'w+'
"""

# =============================================================================
# SECTION 2: READING FILES
# =============================================================================

print("\n" + "=" * 60)
print("READING FILES")
print("=" * 60)

import os

# Create a sample file for demonstration
sample_content = """Line 1: Hello, World!
Line 2: Python is awesome
Line 3: File handling in Python
Line 4: Easy and powerful
Line 5: End of file"""

# Write sample file
with open('demo_file.txt', 'w') as f:
    f.write(sample_content)

# Method 1: read() - reads entire file
print("Method 1: read()")
with open('demo_file.txt', 'r') as f:
    content = f.read()
    print(f"Content:\n{content}")

# Method 2: readline() - reads one line at a time
print("\nMethod 2: readline()")
with open('demo_file.txt', 'r') as f:
    line1 = f.readline()
    line2 = f.readline()
    print(f"Line 1: {line1.strip()}")
    print(f"Line 2: {line2.strip()}")

# Method 3: readlines() - returns list of all lines
print("\nMethod 3: readlines()")
with open('demo_file.txt', 'r') as f:
    lines = f.readlines()
    print(f"Number of lines: {len(lines)}")

# Method 4: Iterating over file object (memory efficient)
print("\nMethod 4: Iterating over file")
with open('demo_file.txt', 'r') as f:
    for i, line in enumerate(f, 1):
        print(f"  {i}: {line.strip()}")

# =============================================================================
# SECTION 3: WRITING FILES
# =============================================================================

print("\n" + "=" * 60)
print("WRITING FILES")
print("=" * 60)

# write() - writes string to file
print("write():")
with open('write_demo.txt', 'w') as f:
    f.write("First line\n")
    f.write("Second line\n")
    f.write("Third line\n")

with open('write_demo.txt', 'r') as f:
    print(f.read())

# writelines() - writes list of strings
print("writelines():")
lines = ['Line A\n', 'Line B\n', 'Line C\n']
with open('writelines_demo.txt', 'w') as f:
    f.writelines(lines)

# Appending to files
print("Appending:")
with open('write_demo.txt', 'a') as f:
    f.write("Appended line\n")

with open('write_demo.txt', 'r') as f:
    print(f.read())

# =============================================================================
# SECTION 4: FILE POSITION
# =============================================================================

print("\n" + "=" * 60)
print("FILE POSITION (seek and tell)")
print("=" * 60)

with open('demo_file.txt', 'r') as f:
    print(f"Initial position: {f.tell()}")
    
    content = f.read(10)
    print(f"After reading 10 chars: {f.tell()}")
    print(f"Content read: '{content}'")
    
    # Seek to beginning
    f.seek(0)
    print(f"After seek(0): {f.tell()}")

# =============================================================================
# SECTION 5: BINARY FILES
# =============================================================================

print("\n" + "=" * 60)
print("BINARY FILES")
print("=" * 60)

# Writing binary data
binary_data = bytes([65, 66, 67, 68, 69])  # A, B, C, D, E
with open('binary_demo.bin', 'wb') as f:
    f.write(binary_data)

# Reading binary data
with open('binary_demo.bin', 'rb') as f:
    data = f.read()
    print(f"Binary data: {data}")
    print(f"As hex: {data.hex()}")

# =============================================================================
# SECTION 6: CONTEXT MANAGERS
# =============================================================================

print("\n" + "=" * 60)
print("CONTEXT MANAGERS (with statement)")
print("=" * 60)

print("""
The 'with' statement automatically:
1. Opens the file
2. Ensures file is closed even if exception occurs
3. Handles cleanup

Example:
    with open('file.txt', 'r') as f:
        content = f.read()
    # File is automatically closed here
""")

# Multiple files at once
print("Opening multiple files:")
with open('demo_file.txt', 'r') as f1, open('write_demo.txt', 'r') as f2:
    content1 = f1.read(20)
    content2 = f2.read(20)
    print(f"  File 1: {content1}")
    print(f"  File 2: {content2}")

# =============================================================================
# SECTION 7: PRACTICAL UTILITIES
# =============================================================================

print("\n" + "=" * 60)
print("PRACTICAL FILE UTILITIES")
print("=" * 60)


def count_lines(filename):
    """Count lines in a file efficiently."""
    with open(filename, 'r') as f:
        return sum(1 for _ in f)


def tail_file(filename, n=3):
    """Get last n lines of a file."""
    with open(filename, 'r') as f:
        lines = f.readlines()
        return lines[-n:]


def copy_file(source, destination):
    """Copy a file efficiently."""
    with open(source, 'rb') as src, open(destination, 'wb') as dst:
        for chunk in iter(lambda: src.read(8192), b''):
            dst.write(chunk)


print(f"Line count: {count_lines('demo_file.txt')}")
print(f"Last 2 lines: {tail_file('demo_file.txt', 2)}")

# =============================================================================
# CLEANUP
# =============================================================================

# Clean up demo files
for filename in ['demo_file.txt', 'write_demo.txt', 'writelines_demo.txt', 'binary_demo.bin']:
    if os.path.exists(filename):
        os.remove(filename)

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("✅ You've learned file handling basics!")
    print("=" * 60)
