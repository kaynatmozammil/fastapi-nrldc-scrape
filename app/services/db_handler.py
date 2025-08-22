from sqlalchemy.orm import Session
from app.db.models import PspData
from datetime import datetime, date , timedelta

def insert_data(db: Session, records: list):
    if not records:
        return

    db.query(PspData).delete()
    db.commit()

    entries = []
    for rec in records:
        report_date = rec.get("report_date")
        if isinstance(report_date, str):
            report_date = datetime.strptime(report_date, "%Y-%m-%d").date()
        elif isinstance(report_date, datetime):
            report_date = report_date.date()
        elif not isinstance(report_date, date):
            report_date = date.today()
        report_date = report_date - timedelta(days=1)
        entry = PspData(
            report_date=report_date,
            state=rec.get("State"),
            Thermal=float(rec.get("Thermal") or 0),
            Hydro=float(rec.get("Hydro") or 0),
            Gas_Naptha_Diesel=float(rec.get("Gas_Naptha_Diesel") or 0),
            Solar=float(rec.get("Solar") or 0),
            Wind=float(rec.get("Wind") or 0),
            Others_Biomass_Cogen_etc=float(rec.get("Others_Biomass_Cogen") or 0),
            Total=float(rec.get("Total") or 0),
            Drawal_Sch=float(rec.get("Drawal_Sch") or 0),
            Act_Drawal=float(rec.get("Act_Drawal") or 0),
            UI=float(rec.get("UI") or 0),
            Requirement=float(rec.get("Requirement") or 0),
            Shortage=float(rec.get("Shortage") or 0),
            Consumption=float(rec.get("Consumption") or 0),
        )
        entries.append(entry)

    db.add_all(entries)
    db.commit()
