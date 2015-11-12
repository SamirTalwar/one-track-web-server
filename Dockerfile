FROM python:3

EXPOSE 80

COPY script script
RUN chmod +x script
ENTRYPOINT ["./script"]
