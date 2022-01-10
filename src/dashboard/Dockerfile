FROM python:3.9.7

WORKDIR /dashboard

COPY ./requirements.txt /dashboard

RUN pip install -r requirements.txt

COPY ./ /dashboard

CMD ["streamlit", "run",  "streamlit.py"]