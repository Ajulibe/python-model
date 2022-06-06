from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

# database configuration
db_host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')
db_pass = os.getenv('DB_PASS')
db_user = os.getenv('DB_USER')

engine = create_engine(f"postgresql://{db_user}:{db_pass}@{db_host}/{db_name}")
Base = declarative_base()


SessionLocal = sessionmaker(bind=engine)