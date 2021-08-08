import os
import uvicorn
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')
MAX_WORKER = int(config.get('CONFIG', 'MAX_WORKER'))

if __name__ == '__main__':
    cpu_nums = os.cpu_count()
    uvicorn.run(app='handler:app', host='0.0.0.0', port=8000, workers=cpu_nums * MAX_WORKER)
