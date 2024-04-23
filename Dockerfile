FROM python:3.9

EXPOSE 5000

WORKDIR /app
COPY . /app

# Keeps python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONBUFFERED=1

# Install pip requirements
RUN pip install --upgrade pip
COPY requirements.txt .

RUN python -m pip install -r requirements.txt

CMD ["gunicorn", "--bind", "0.0.0.0:5000" ,"app:app"]



