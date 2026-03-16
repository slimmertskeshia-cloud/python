# ----------------------------------------
# Exercise 2-3: Personal Message
# ----------------------------------------

# Create a variable to store a person's name
name = "Eric"

# Print a personal message to that person
print("Exercise 2-3:")
print(f"Hello {name}, would you like to learn some Python today?")
print()


# ----------------------------------------
# Exercise 2-4: Name Cases
# ----------------------------------------

# Store a person's name in a variable
name = "eric"

# Print the name in different formats
print("Exercise 2-4:")
print("Lowercase:", name.lower())   # converts the name to lowercase
print("Uppercase:", name.upper())   # converts the name to uppercase
print("Title Case:", name.title())  # capitalizes the first letter
print()


# ----------------------------------------
# Exercise 2-5: Famous Quote
# ----------------------------------------

# Print a famous quote and the author's name
print("Exercise 2-5:")
print('Albert Einstein once said, "A person who never made a mistake never tried anything new."')
print()


# ----------------------------------------
# Exercise 2-6: Famous Quote 2
# ----------------------------------------

# Store the famous person's name in a variable
famous_person = "Albert Einstein"

# Create a variable that stores the full message
message = f'{famous_person} once said, "A person who never made a mistake never tried anything new."'

# Print the message
print("Exercise 2-6:")
print(message)
print()


# ----------------------------------------
# Exercise 2-7: Stripping Names
# ----------------------------------------

# Store a name with whitespace characters
# \t = tab space
# \n = new line
name = "\t\n  Eric Smith  \n\t"

print("Exercise 2-7:")

# Print the original name with whitespace
print("Original name:")
print(name)

# Remove whitespace from the left side
print("Left strip:")
print(name.lstrip())

# Remove whitespace from the right side
print("Right strip:")
print(name.rstrip())

# Remove whitespace from both sides
print("Full strip:")
print(name.strip())
print()


# ----------------------------------------
# Exercise 2-8: File Extensions
# ----------------------------------------

# Store a filename with an extension
filename = "python_notes.txt"

# Remove the .txt suffix
clean_filename = filename.removesuffix(".txt")

print("Exercise 2-8:")
print(clean_filename)