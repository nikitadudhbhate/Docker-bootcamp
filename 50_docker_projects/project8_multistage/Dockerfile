# --- STAGE 1: The Heavy Builder Environment ---
FROM golang:alpine AS builder
WORKDIR /app
COPY main.go .
# Compile the code into a single binary file named 'myapp'
RUN go build -o myapp main.go

# --- STAGE 2: The Microscopic Production Environment ---
FROM alpine:latest
WORKDIR /app
# The magic command: Copy ONLY the binary from Stage 1. Leave the Go compiler behind!
COPY --from=builder /app/myapp .

CMD ["./myapp"]
