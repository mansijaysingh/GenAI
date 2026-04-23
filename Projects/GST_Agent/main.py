from fastapi import FastAPI, UploadFile,File
import shutil
import os


app=FastAPI()

UPLOAD_DIR="uploads"
if not os.path.exists(UPLOAD_DIR):
  os.makedirs(UPLOAD_DIR)


@app.post("/upload-bill/")
async def upload_bill(file:UploadFile=File(...)):
  file_location=f"{UPLOAD_DIR}/{file.filename}"
  with open(file_location, "wb+") as file_object:
    shutil.copyfileobj(file.file, file_object)

  return {"info": f"File '{file.filename}' successfully saved at '{file_location}'"}