#!/usr/bin/env python
# -*- coding: utf-8 -*-

import uvicorn
import os

if __name__ == "__main__":
    cpu_nums = os.cpu_count()
    uvicorn.run('handler:app', host="0.0.0.0", port=8000, workers=cpu_nums)
