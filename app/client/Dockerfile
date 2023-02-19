FROM python:3.10-alpine
WORKDIR /app
COPY client.py /app
ENV HOST_SRV_ARG ""
ENV PORT_SRV_ARG ""
CMD python client.py ${HOST_SRV_ARG} ${PORT_SRV_ARG}