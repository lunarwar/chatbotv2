
# Chat Bot

This is a chat bot project that interacts with users and retrieves information from a MySQL database. It uses Python and relies on the provided database configuration.

## Requirements

- Python (version 3.9.1)
- MySQL database

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/JonOlummy/chat-bot.git
   ```

2. Navigate to the project directory:

   ```shell
   cd chat-bot
   ```

3. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

## Configuration

1. Ensure that you have a MySQL database set up with the necessary tables and data. (columns are tag, patterns, responses)
2. Update the database configuration in the `chatbot.py` file with your MySQL database credentials.

## Usage

1. Run the chat bot:
   ```shell
   python chatbot.py
   ```
2. The chat bot will prompt for user input and interact with the database to retrieve information.
