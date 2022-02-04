FROM python:3.10-slim

# Install pip requirements  
COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt

WORKDIR /app
COPY ./app .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]