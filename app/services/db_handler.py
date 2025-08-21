from sqlalchemy.orm import Session
from app.db.models import PspData
from datetime import datetime

def insert_data(db: Session, records: list):
    db.query(PspData).delete()
    db.commit()
    for rec in records:
        entry = PspData(
            report_date=rec["report_date"],
            state=rec["state"],
            key=rec["key"],
            value=rec["value"]
        )
        db.add(entry)
    db.commit()
    db.refresh(entry)  

