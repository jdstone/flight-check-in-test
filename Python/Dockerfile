FROM python:3.13.0-alpine3.20

WORKDIR /flight-check-in-test-suite

COPY requirements.txt /flight-check-in-test-suite/

RUN pip3 install -r requirements.txt

COPY config.py /flight-check-in-test-suite/
COPY gunicorn_config.py /flight-check-in-test-suite/
COPY app/ /flight-check-in-test-suite/app/

ENTRYPOINT ["gunicorn"]
CMD ["--config", "gunicorn_config.py", "app:create_app()"]
