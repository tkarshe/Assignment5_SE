from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends

from ..models import models
from ..schemas import schemas


def create(db: Session, order_detail: schemas.OrderDetailCreate):
    db_order_detail = models.OrderDetail(**order_detail.dict())
    db.add(db_order_detail)
    db.commit()
    db.refresh(db_order_detail)
    return db_order_detail


def read_all(db: Session):
    return db.query(models.OrderDetail).all()


def read_one(db: Session, order_detail_id: int):
    return db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id).first()


def update(db: Session, order_detail: schemas.OrderDetailUpdate, order_detail_id: int):
    db_order_detail = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id).first()
    if db_order_detail is None:
        raise HTTPException(status_code=404, detail="Order Detail not found")
    update_data = order_detail.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_order_detail, key, value)
    db.commit()
    return db_order_detail


def delete(db: Session, order_detail_id: int):
    db_order_detail = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id).first()
    if db_order_detail is None:
        raise HTTPException(status_code=404, detail="Order Detail not found")
    db.delete(db_order_detail)
    db.commit()
