from sqlalchemy.orm import declarative_base
from sqlalchemy import Column,Integer,String,Float,DateTime
from datetime import datetime


Base=declarative_base()



class Trade(Base):

    __tablename__="trades"


    id=Column(
        Integer,
        primary_key=True
    )


    symbol=Column(
        String
    )


    action=Column(
        String
    )


    volume=Column(
        Float
    )


    price=Column(
        Float
    )


    profit=Column(
        Float
    )


    time=Column(
        DateTime,
        default=datetime.utcnow
    )
