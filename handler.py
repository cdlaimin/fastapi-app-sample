#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from src.utils.log_init import logger_loguru

from src.router.api import router

app = FastAPI(
    title="Sample Backend",
    description=("API for Sample Backend."),
    docs_url="/",
)
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    logger_loguru.info(
        'UTL= {} host={} header = {}'.format(request.url, request.client.host, request.headers))
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

app.include_router(router=router)
app.logger = logger_loguru
