from fastapi import FastAPI, Depends, HTTPException, Query, Request, Path
from fastapi.responses import HTMLResponse, FileResponse

from typing import List, Optional
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

@app.get("/")
async def index():
    html_home = "<h1>Приложение Fishing Shop запущенно</h1>"
    return HTMLResponse (content = html_home)

@app.get("/home", response_class=FileResponse)
async def home():
    return "static/home.html"