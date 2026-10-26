FROM python:3.9-alpine
WORKDIR /app

# 1. Create a dedicated system group and user named 'appuser'
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# 2. Copy the script into the container
COPY check_user.py .

# 3. Change ownership of the app directory so our non-root user can read/execute it
RUN chown -R appuser:appgroup /app

# 4. Switch to the non-root user. All subsequent commands and PID 1 run as 'appuser'
USER appuser

CMD ["python", "check_user.py"]
