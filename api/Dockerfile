FROM python:3.9.7

WORKDIR /api

COPY ./requirements.txt /api

RUN pip install -r requirements.txt

COPY ./ /api

ENV PORT=8080

CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port $PORT"]