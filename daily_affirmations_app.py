import requests
import schedule
import time
from datetime import datetime

# Predefined list of affirmations
affirmations = [
    "You are doing great.",
    "Keep pushing forward.",
    "Today is a day full of opportunities.",
    "Believe in yourself.",
    "Your potential is limitless."
]

def post_affirmation():
    try:
        # Select a random affirmation
        affirmation = random.choice(affirmations)
        print(f"{datetime.now()}: {affirmation}")
        # Here you would add code to post the affirmation to a social media platform or another outlet
        # For example: requests.post("https://api.socialmedia.com/post", data={"message": affirmation})
    except Exception as e:
        print(f"An error occurred: {e}")

# Schedule the post_affirmation function to run every day at 8:00 AM
schedule.every().day.at("08:00").do(post_affirmation)

print("Daily Affirmation App is running. Affirmations will be posted daily at 8:00 AM.")

while True:
    schedule.run_pending()
    time.sleep(60)  # Wait for one minute before checking again
