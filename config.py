import dotenv
import os

dotenv.load_dotenv()

DATABASE_URL = os.environ.get('DATABASE_URL')
