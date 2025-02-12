# pull official base image
FROM python:3.11-slim

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && \
    apt-get -y install build-essential gdal-bin python3-gdal libgdal-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

# make wait-for-it.sh executable
# RUN chmod +x wait-for-it.sh

# run wait-for-it.sh
# CMD ["./wait-for-it.sh", "books-db:5432", "--"]

# make start_notes_api.sh executable
RUN chmod +x start_books_api.sh

# command to start gunicorn
CMD ["./start_notes_api.sh"]