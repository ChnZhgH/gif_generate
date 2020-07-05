FROM python:3.7
RUN apt-get update \
    && mkdir /code
WORKDIR /code
COPY . .
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]