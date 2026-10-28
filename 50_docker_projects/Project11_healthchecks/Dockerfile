FROM python:3.9-alpine
WORKDIR /app

# Alpine is so minimal it doesn't include curl by default. We install it for our health check.
RUN apk add --no-cache curl

COPY app.py .
EXPOSE 8080

# Native Docker Healthcheck Directive
HEALTHCHECK --interval=5s --timeout=3s --retries=3 \
  CMD curl -f http://localhost:8080/health || exit 1
  
CMD ["python", "app.py"]
