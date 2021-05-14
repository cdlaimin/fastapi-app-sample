FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN mkdir /proj/
COPY ./ /proj/
WORKDIR /proj
#COPY ./pip.conf /root/.pip/
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "./main.py"]




