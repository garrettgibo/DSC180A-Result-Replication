FROM ucsdets/datascience-notebook:2020.2-stable

USER root

# Move to working directory /build
WORKDIR /build
COPY . .

RUN pip install pandas

CMD ["python", "run.py", "test"]