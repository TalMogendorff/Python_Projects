FROM python:3.9.7

ADD main.py .

RUN pip install speedtest
RUN pip uninstall enum34

CMD ["python", "./main.py"]