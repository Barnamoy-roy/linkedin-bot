## LinkedIn-Bot 
Want to build more connections? Can't find people of your niche on LinkedIn? Want to automate the process of sending connection request with personalized invitation request? I have got you covered. 

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [How it works](#howitworks)

## Features
- **Automated Login:** Automatically log in to LinkedIn with your credentials.
- **Custom Connection Requests:** Send connection requests with custom invitation notes.
- **Fallback to Normal Requests:** If your daily limit for sending custom notes is reached, the bot will send connection requests without notes.
- **Pagination Handling:** Seamlessly navigate through multiple pages of search results.
- **Command Line Interface:** Control the bot and receive real-time updates directly from the command line.
- **Search Capabilities:** Search for users based on specific companies and roles.
- **Captcha Handling:** If a captcha appears, the bot pauses for 1 minute to allow manual solving.

## Technologies 
- **Python** 
- **Selenium**

## Installation 
Clone the repository:
```bash
git clone https://github.com/yourusername/linkedin-bot.git
cd linkedin-bot
```
Install the required dependencies: 
```bash
pip install -r requirements.txt
```
Run the bot using the command line interface. Below is an example of how to use the bot:
```bash
python linkedin_bot.py --n "number of connection requests" --username "your_email@example.com" --password "yourpassword" --company "Company Name" --role "Job Title"
```
Command Line Arguments
--username: Your LinkedIn email address.
--password: Your LinkedIn password.
--company: The company you want to search for.
--role: The role you want to search for.

## How It Works
- **Login**: The bot logs into your LinkedIn account using the provided credentials.
- **Search**: It searches for users based on the specified company and role.
- **Send Requests**: The bot sends connection requests with a custom note, if available. If the daily limit for custom notes is reached, it sends a standard connection request.
- **Handle Captchas**: If a captcha appears, the bot pauses for 1 minute to allow manual solving.
- **Pagination**: The bot handles pagination to ensure all relevant profiles are processed.
