import shutil
from pathlib import Path

from fastapi import FastAPI, HTTPException, Request, UploadFile
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/vault", StaticFiles(directory="vault"), name="vault")
app.mount("/static", StaticFiles(directory="static"), name="static")

vault = Path("vault")
vault.mkdir(exist_ok=True)

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def home(req: Request):
    files = sorted([file.name for file in vault.iterdir() if file.is_file()])

    return templates.TemplateResponse(
        request=req, name="index.html", context={"files": files}
    )


@app.post("/upload")
async def upload(file: UploadFile):
    if file.filename:
        file_path = vault / file.filename
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    return RedirectResponse(url="/", status_code=303)


@app.get("/delete/{file_name}")
async def delete(file_name: str):
    file_path = vault / file_name
    if file_path.exists() and file_path.is_file():
        file_path.unlink()
        return RedirectResponse(url="/", status_code=303)
    return HTTPException(status_code=404, detail=f"file {file_name} not in vault")
