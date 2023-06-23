FROM python:3.10-bookworm

# set work directory
WORKDIR /app

# copy project
COPY . /app

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /app/

ENTRYPOINT ["python3", "./model-server/model.py"]