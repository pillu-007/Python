import os

# Import the dotenv library
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

# Access the environment variables
api_key = os.getenv("API_KEY")
database_url = os.getenv("DATABASE_URL")
debug_mode = os.getenv("DEBUG")

# Now you can use these variables in your code
print(f"API Key: {api_key}")
print(f"Database URL: {database_url}")
print(f"Debug Mode: {debug_mode}")
