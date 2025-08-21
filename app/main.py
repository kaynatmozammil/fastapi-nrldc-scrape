from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from app.db.database import engine
from app.db import database, models
from app.services import scraper, pdf_parser, data_cleaner, db_handler

# models.Base.metadata.drop_all(bind=engine)   
models.Base.metadata.create_all(bind=engine) 

app = FastAPI(title="NRLDC PSP Report API", debug=True)


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/nrldc_data")
def process_nrldc_data(db: Session = Depends(get_db)):
    pdf_path = scraper.download_latest_pdf()
    if not pdf_path:
        return {"error": "No PDF found to download"}

    data_frame = pdf_parser.parse_pdf(pdf_path)
    if data_frame is None or data_frame.empty:
        return {"error": "No table extracted from PDF"}

    json_data = data_cleaner.clean_data(data_frame)

    # Step 4: Insert into DB
    db_handler.insert_data(db, json_data)

    return {
        "status": "success",
        "records_inserted": len(json_data)
    }


@app.get("/psp_data")
def get_psp_data(db: Session = Depends(get_db)):
    records = db.query(models.PspData).all()
    return JSONResponse(content=jsonable_encoder(records))
