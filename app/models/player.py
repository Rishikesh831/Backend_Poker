from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.db.database import Base
class Player(Base):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    
    table_id = Column(Integer, ForeignKey('tables.id'))
   
    email = Column(String, unique=True, index=True)
    chips = Column(Integer, default=10000)
    in_game = Column(Boolean, default=False)
    
    
    table = relationship("Table", back_populates="players")
    
    
    