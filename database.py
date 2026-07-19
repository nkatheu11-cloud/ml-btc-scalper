"""
Database storage
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE="sqlite:///trading.db"


engine=create_engine(
    DATABASE,
    connect_args={
        "check_same_thread":False
    }
)


Session=sessionmaker(
    bind=engine
)
