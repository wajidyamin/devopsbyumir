# Step 1: Store your info
name = "Abdul Wajid"
age = 30
country = "Pakistan"

# Step 2: Print a welcome message
print(f"Welcome, {name} from {country}! You are {age} years old.")

# Step 3: List of top 3 DevOps tools
devops_tools = ["Kubernetes", "Github", "Grfana"]

# Step 4: Loop through and print each tool
print("\nYour top DevOps tools:")
for tool in devops_tools:
    print(f"- {tool}")

# Step 5: Store profile info in a dictionary
profile = {
    "Name": name,
    "Age": age,
    "Country": country,
    "DevOps Tools": devops_tools
}

# Step 6: Print each key-value pair
print("\nProfile Information:")
for key, value in profile.items():
    print(f"{key}: {value}")

# Step 7: Define greet_user function
def greet_user(username):
    print(f"\nHello, {username}! Hope you're having a great day.")

# Step 8: Call the function
greet_user(name)

# Step 9: Define add_numbers function
def add_numbers(x, y):
    return x + y

# Call and print result
result = add_numbers(75, 25)
print(f"\nThe sum of 75 and 25 is: {result}")