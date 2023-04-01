FROM python:3.9-buster
# FROM tensorflow/tensorflow:latest-gpu-jupyter

WORKDIR /workspace
COPY . /workspace/

RUN apt-get update && apt-get install texlive-xetex texlive-fonts-recommended texlive-plain-generic pandoc -y

RUN pip install -r requirements.txt
