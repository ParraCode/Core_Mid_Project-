FROM python:3.9.7

WORKDIR /dashboard

COPY ./requirements.txt /dashboard

RUN pip install -r requirements.txt

COPY ./ /dashboard

ENV PORT=8080

CMD ["sh", "-c", "streamlit run --server.port $PORT streamlit.py"]