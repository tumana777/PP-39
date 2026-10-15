from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:otar1991@localhost:5432/PP-39"

engine = create_engine(DATABASE_URL)