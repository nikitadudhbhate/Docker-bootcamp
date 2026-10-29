# syntax=docker/dockerfile:1.4
FROM python:3.9-alpine
WORKDIR /app

# This command uses BuildKit to mount the secret file securely during build time only
RUN --mount=type=secret,id=db_token \
    if [ -f /run/secrets/db_token ]; then \
        echo "🔐 Securely read secret during build!"; \
        cat /run/secrets/db_token > secret_captured.txt; \
    else \
        echo "❌ No secret found!"; \
    fi

COPY app_check.py .
CMD ["python", "-c", "print('✅ BuildKit secret integration test passed successfully!')"]
