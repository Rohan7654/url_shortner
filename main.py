import base64
import io
from fastapi.encoders import jsonable_encoder
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from fastapi import FastAPI, Request, Response
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import segno
import time
import pyshorteners
from PIL import Image
from fastapi.staticfiles import StaticFiles

app = FastAPI()
shortner = pyshorteners.Shortener()

template = Jinja2Templates(directory='templates')
app.mount("/static", StaticFiles(directory="static"), name="static")
origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/shortenurl/{url:path}",)
async def shortenurls(url: str,request: Request):
    query = request.url.query
    if query:
        url += '?' + query
    shortned_url = shortner.tinyurl.short(url)
    qrcode = segno.make(url)
    time_stamp = str(round(time.time()))
    qr_filename = "QR_Code_"+time_stamp+".png"
    qrcode.save(qr_filename,scale=5)
    with open(qr_filename, "rb") as image_file:
       encoded_image_string = base64.b64encode(image_file.read())
    return JSONResponse(content=jsonable_encoder([
        {
        "img":encoded_image_string.decode('utf-8'),
        "shortned_url": shortned_url
       }
    ]))

@app.get("/",response_class=HTMLResponse)
async def root(request: Request):
    return template.TemplateResponse(
        request=request,
        name= "index.html", context={})