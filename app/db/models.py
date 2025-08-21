from app.db.database import Base
from sqlalchemy import Column , Integer , String  , Date , TIMESTAMP , func , Float
class PspData(Base):
    __tablename__ = "psp_data"

    id = Column(Integer , primary_key = True , index = True , autoincrement=True)
    report_date = Column(Date , nullable=False )
    state = Column(String , nullable=False)
    key = Column(String , nullable=True)
    value = Column(String, nullable=True)
    inserted_at = Column(TIMESTAMP , server_default=func.now())

