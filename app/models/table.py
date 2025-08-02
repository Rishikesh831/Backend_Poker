from sqlalchemy import Column, Integer, String, ForeignKey,Boolean
from sqlalchemy.orm import relationship
from app.db.database import Base

class Table(Base):
    __tablename__ = 'tables'
    id = Column(Integer, primary_key=True, index=True)
    game_type = Column(String, index=True)
    
    max_players = Column(Integer, default=8)
    status = Column(String, default='waiting')
    
    players = relationship("Player", back_populates="table")