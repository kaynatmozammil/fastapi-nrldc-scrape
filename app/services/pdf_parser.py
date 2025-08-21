import camelot
import os

def parse_pdf(file_path: str):
    tables = camelot.read_pdf(file_path, pages="1", flavor="lattice")
    df = tables[0].df  
    
    if os.path.exists(file_path):
        os.remove(file_path)

    return df
