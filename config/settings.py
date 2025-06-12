from dotenv import load_dotenv
import os

load_dotenv()

base_url = os.getenv("BASE_URL")
api_key = os.getenv("API_KEY")
list_id = os.getenv("LIST_ID")
task_id = os.getenv("TASK_ID")

if not all([base_url, api_key, list_id, task_id]):
    raise ValueError("One or more required environment variables are not set.")