#!/usr/bin/python
# -*- coding: utf-8 -*-

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from src.logs.log_init import log_init, sys_log
import time

from src.router.api import router

app = FastAPI(title="Sample Backend",
              description=(
                  "API for Sample Backend."
              ),
              docs_url="/", )
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router=router)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    sys_log.info(f"start request path={request.url.path}")
    start_time = time.time()
    response = await call_next(request)
    process_time = (time.time() - start_time) * 1000
    formatted_process_time = '{0:.2f}'.format(process_time)
    sys_log.info(
        f"finished request path={request.url.path} time_duration={formatted_process_time}ms status_code={response.status_code}")
    return response


# 初始化日志
log_init()
