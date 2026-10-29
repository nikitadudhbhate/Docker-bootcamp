FROM python:3.9-alpine
WORKDIR /app
COPY greeter.py .

# ENTRYPOINT locks in the executable engine
ENTRYPOINT ["python", "greeter.py"]

# CMD provides the default argument if the user doesn't pass anything
CMD ["DevOps Engineer"]
