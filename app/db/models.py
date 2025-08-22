from app.db.database import Base
from sqlalchemy import Column , Integer , String  , Date , TIMESTAMP , func , Float 
from app.db.database import Base
from datetime import datetime

class PspData(Base):
    __tablename__ = "psp_data"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    report_date = Column(Date, nullable=False)
    state = Column(String, nullable=False)
    Thermal = Column(Float, nullable=True)
    Hydro = Column(Float, nullable=True)
    Gas_Naptha_Diesel = Column(Float, nullable=True)
    Solar = Column(Float, nullable=True)
    Wind = Column(Float, nullable=True)
    Others_Biomass_Cogen_etc = Column(Float, nullable=True)
    Total = Column(Float, nullable=True)
    Drawal_Sch = Column(Float, nullable=True)
    Act_Drawal = Column(Float, nullable=True)
    UI = Column(Float, nullable=True)
    Requirement = Column(Float, nullable=True)
    Shortage = Column(Float, nullable=True)
    Consumption = Column(Float, nullable=True)

    inserted_at = Column(TIMESTAMP, default=datetime.now) 

