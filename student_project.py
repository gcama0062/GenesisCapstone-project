"""
Data Structures
Student Project
Project Title:
"""

#hospital database- look up patients for employes 

import requests
import random

print("Welcome to the Hospital Database Lookup!")
print("Enter a patient's first name, last name, and date of birth (YYYY-MM-DD).")
print("The system will display the patient's information based on your input.\n")

# Get user input
first_name = input("First name: ").strip()
last_name = input("Last name: ").strip()
dob_input = input("Date of Birth (YYYY-MM-DD): ").strip()

# Get users from the API
response = requests.get('https://randomuser.me/api/?results=50')

if response.status_code == 200:
    data = response.json()
    found = False
    matched_user = None

    for user in data['results']:
        api_first = user['name']['first'].lower()
        api_last = user['name']['last'].lower()
        api_dob = user['dob']['date'][:10]

        if first_name.lower() == api_first and last_name.lower() == api_last and dob_input == api_dob:
            matched_user = user
            found = True
            break

    print("\n--- Patient Information ---")

    if found:
        # Use actual data if found
        print("Full Name: {} {}".format(matched_user['name']['first'], matched_user['name']['last']))
        print("Date of Birth: {}".format(matched_user['dob']['date'][:10]))
        print("Gender: {}".format(matched_user['gender'].capitalize()))
        print("Email: {}".format(matched_user['email']))
        print("Country: {}".format(matched_user['location']['country']))
        print("Nationality: {}".format(matched_user['nat']))
    else:
        # Use input + random user for extra fields
        random_user = random.choice(data['results'])
        print("Full Name: {} {}".format(first_name, last_name))
        print("Date of Birth: {}".format(dob_input))
        print("Gender: {}".format(random_user['gender'].capitalize()))
        print("Email: {}".format(random_user['email']))
        print("Country: {}".format(random_user['location']['country']))
        print("Nationality: {}".format(random_user['nat']))
else:
    print("Error fetching data. Please try again later.")
