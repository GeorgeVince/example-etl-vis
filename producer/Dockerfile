FROM python:3.10-slim

# Install pip requirements  
COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt

WORKDIR /app
COPY ./app .

RUN apt-get update -y
RUN apt-get install -y curl
RUN curl https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh > wait-for-it.sh
RUN chmod +x wait-for-it.sh

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]