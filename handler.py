#!/usr/bin/python
# -*- coding: utf-8 -*-

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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
app.include_router(router=router)
app.logger = logger_loguru
