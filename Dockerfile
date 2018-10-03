FROM python:3.4

RUN apt update && apt install -y  python3-pip
RUN pip3 install FLASK==0.10.1 requests==2.5.1 
WORKDIR /app
COPY app /app
COPY cmd.sh /

EXPOSE 5000

CMD ["/cmd.sh"]

