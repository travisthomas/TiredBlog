FROM python:3.7-alpine
RUN apk add --update \
    sqlite \
    && pip3 install pipenv \
    && rm -rf /var/cache/apk/*
COPY . /app
WORKDIR /app
RUN pipenv install --system
#EXPOSE 5000
CMD ["python", "./blog.py"]
