FROM python:slim as build
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
FROM build as runtime
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
