FROM python:3-slim

EXPOSE 80

COPY app.py app
RUN chmod +x app
ENTRYPOINT ["./app"]
CMD ["--help"]
