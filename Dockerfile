FROM alpine:3.4

RUN apk add --update musl py-pip bash
RUN pip install falcon==1.1.0rc1 falcon-cors gunicorn

WORKDIR /app
COPY src src
COPY tests tests
ENV PYTHONPATH=/app

EXPOSE 80
CMD ["gunicorn", "-b", "0.0.0.0:80", "--reload", "--chdir", "src", "app:api"]
