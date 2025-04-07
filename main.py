from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/upload_excel/")
async def upload_excel(file: UploadFile = File(...)):
    contents = await file.read()
    filename = f"uploads/{file.filename}"
    os.makedirs("uploads", exist_ok=True)
    with open(filename, "wb") as f:
        f.write(contents)
    return JSONResponse(content={"message": "Excel file uploaded successfully.", "filename": file.filename})

@app.post("/upload_dxf/")
async def upload_dxf(file: UploadFile = File(...)):
    contents = await file.read()
    filename = f"uploads/{file.filename}"
    os.makedirs("uploads", exist_ok=True)
    with open(filename, "wb") as f:
        f.write(contents)
    return JSONResponse(content={"message": "DXF file uploaded successfully.", "filename": file.filename})
