import pandas as pd

# create a list of users and their test scores
data = [
    {"Name": "Ash", "Test Score": 85},
    {"Name": "Misty", "Test Score": 90},
    {"Name": "Brock", "Test Score": 78},
    {"Name": "James", "Test Score": 92},
    {"Name": "Jessie", "Test Score": 88},
    {"Name": "Oak", "Test Score": 76},
    {"Name": "Steven", "Test Score": 95},
    {"Name": "May", "Test Score": 81},
    {"Name": "Mallow", "Test Score": 89},
    {"Name": "Giovanni", "Test Score": 73},
]

# converts the list to a DataFrame
df = pd.DataFrame(data)

# print out just the names from the DataFrame
print(df["Name"])