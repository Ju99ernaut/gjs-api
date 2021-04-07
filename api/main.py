import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import templates

import config
import data

from constants import API_TAGS_METADATA

config.parse_args()
app = FastAPI(
    title="Grapesjs API",
    description="Simple API for grapesjs and grapesjs-template-manager",
    version="1.0.0",
    openapi_tags=API_TAGS_METADATA,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080/", "http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(templates.router)


@app.get("/")
async def root():
    return {
        "docs": "api documentation at /docs or /redoc",
    }


if __name__ == "__main__":
    data.setup()
    uvicorn.run("main:app", host=config.CONFIG.host, port=int(config.CONFIG.port))
