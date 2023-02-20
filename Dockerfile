FROM  tensorflow/tensorflow:latest-gpu


WORKDIR /workspace
COPY . .

RUN pip install -r requirements.txt
