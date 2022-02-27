import datetime
from sqlalchemy import Column, Integer, String, Date, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///gardenHighscores.db')
Base = declarative_base()

class GardenHighscores(Base):
    __tablename__ = 'Highscores'
    id = Column(Integer, primary_key=True)
    name = Column("Player", String)
    score = Column("Score", Integer)
    created_date = Column("Date", Date, default=datetime.datetime.utcnow)

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return f"{self.id}. PLAYER: {self.name} >>> SCORE: << {self.score} >> ({self.created_date})"

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def get_highscores():
    highscores = session.query(GardenHighscores).all()
    for i in highscores:
        print(i)
