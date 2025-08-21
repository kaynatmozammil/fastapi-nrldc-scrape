import camelot
import os

def parse_pdf(file_path: str):
    tables = camelot.read_pdf(file_path, pages="1", flavor="lattice")

    if not tables or len(tables) < 2:
        # No second table found → cleanup
        if os.path.exists(file_path):
            os.remove(file_path)
        return None  

    # Get the 2nd table (index 1)
    df = tables[0].df  

    # Delete the PDF after parsing
    if os.path.exists(file_path):
        os.remove(file_path)

    return df
