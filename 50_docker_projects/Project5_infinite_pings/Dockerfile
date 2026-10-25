FROM ubuntu:22.04
WORKDIR /app

COPY entrypoint.sh .
# Grant execution permissions to the script
RUN chmod +x entrypoint.sh

CMD ["./entrypoint.sh"]
