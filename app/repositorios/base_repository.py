# repositories/base_repository.py
from sqlalchemy.orm import Session

class BaseRepository:
    def __init__(self, db: Session):
        self.db = db
