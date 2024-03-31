from sqlalchemy.orm import Session
from ..models import Sandwich
from ..schemas import SandwichCreate, SandwichUpdate

def create_sandwich(db: Session, sandwich: SandwichCreate):
    db_sandwich = Sandwich(**sandwich.dict())
    db.add(db_sandwich)
    db.commit()
    db.refresh(db_sandwich)
    return db_sandwich

def update_sandwich(db: Session, sandwich_id: int, sandwich: SandwichUpdate):
    db_sandwich = db.query(Sandwich).filter(Sandwich.id == sandwich_id).first()
    if db_sandwich:
        for var, value in vars(sandwich).items():
            setattr(db_sandwich, var, value) if value is not None else None
        db.commit()
        db.refresh(db_sandwich)
    return db_sandwich

def delete_sandwich(db: Session, sandwich_id: int):
    db_sandwich = db.query(Sandwich).filter(Sandwich.id == sandwich_id).first()
    if db_sandwich:
        db.delete(db_sandwich)
        db.commit()
    return None

def get_all_sandwiches(db: Session):
    return db.query(Sandwich).all()

def get_sandwich_by_id(db: Session, sandwich_id: int):
    return db.query(Sandwich).filter(Sandwich.id == sandwich_id).first()
