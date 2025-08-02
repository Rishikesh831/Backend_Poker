from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models import table as table_model
from app.schemas import table_schemas as table_schemas

router = APIRouter()

@router.get("/tables/", response_model=list[table_schemas.Table])
def read_tables(db: Session = Depends(get_db)):
    tables = db.query(table_model.Table).all()
    return tables


@router.post("/tables/", response_model=table_schemas.Table)
def create_table(table: table_schemas.TableCreate, db: Session = Depends(get_db)):
    db_table = table_model.Table(**table.dict())
    db.add(db_table)
    db.commit()
    db.refresh(db_table)
    return db_table