FROM python:slim
RUN mkdir /app
WORKDIR /app
COPY . /app/
RUN pip install -r requirements.txt
CMD ["uvicorn", "app:app", "--host", "0.0.0.0"]