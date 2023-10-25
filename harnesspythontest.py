import random
import datetime
import json

# Generate a random number between 1 and 5
random_number = random.randint(1, 6)

# Get the current hour
current_hour = datetime.datetime.now().hour

# Calculate the sum
result = random_number + current_hour

# Create a list containing the random number, current hour, and their sum
data_list = [random_number, current_hour, result]

# Convert the list to a JSON object
json_data = json.dumps(data_list)

# Print the JSON object
print(json_data)
