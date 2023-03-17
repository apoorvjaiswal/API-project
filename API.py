from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    # Here you can process the file as needed
    # For example, you could save it to disk using:
    # with open(file.filename, "wb") as f:
    #     f.write(file.file.read())
    
    # Create a JSON response containing any desired information
    response_data = {"message": "File received successfully!"}
    return JSONResponse(content=response_data)
