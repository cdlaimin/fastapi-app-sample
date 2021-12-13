FROM tiangolo/uvicorn-gunicorn:python3.9

COPY ./ /app/
WORKDIR /app
#COPY ./pip.conf /root/.pip/
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "./main.py"]




