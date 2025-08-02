from fastapi import FastAPI
from app.routers import player, table

app = FastAPI()

app.include_router(player.router)
app.include_router(table.router)
