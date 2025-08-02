from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.player import Player
from pydantic import BaseModel
from typing import List

router = APIRouter()

class PlayerCreate(BaseModel):
    name: str
    chips: int
class PlayerOut(BaseModel):
    id: int
    name: str
    chips: int

    class Config:
        orm_mode = True
@router.post("/players", response_model=PlayerOut)
def create_player(player: PlayerCreate, db: Session = Depends(get_db)):
    db_player = Player(name=player.name, chips=player.chips)
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player

# Get all players
@router.get("/players", response_model=List[PlayerOut])
def get_players(db: Session = Depends(get_db)):
    return db.query(Player).all()