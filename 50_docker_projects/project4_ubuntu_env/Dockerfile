FROM ubuntu:22.04
WORKDIR /app

# Set default environment variables
ENV USER_NAME="Anonymous User"
ENV ROLE="Guest"

COPY app.sh .
# Linux requires you to give a script permission to execute before running it
RUN chmod +x app.sh

CMD ["./app.sh"]
