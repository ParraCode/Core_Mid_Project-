FROM python:3.9.7

WORKDIR /api

COPY ./requirements.txt /api

RUN pip install -r requirements.txt

COPY ./ /api

CMD ["uvicorn", "app:main"]