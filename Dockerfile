# Use a minimal Python base image
FROM python:3.9-alpine AS builder

# Set the working directory
WORKDIR /home/data

# Install only essential dependencies
RUN apk add --no-cache py3-pip && \
    pip install --no-cache-dir pandas numpy && \
    rm -rf /root/.cache/pip/* /var/cache/apk/*

# Copy required files
COPY script.py /home/data/script.py
COPY IF-1.txt /home/data/IF-1.txt
COPY AlwaysRememberUsThisWay-1.txt /home/data/AlwaysRememberUsThisWay-1.txt

# Ensure output directory exists
RUN mkdir -p /home/data/output && chmod +x /home/data/script.py

# Use a non-root user for security
RUN adduser -D myuser
USER myuser

# Reduce final image size by using a multi-stage build
FROM python:3.9-alpine
WORKDIR /home/data

# Copy only necessary parts from the builder stage
COPY --from=builder /usr/lib /usr/lib
COPY --from=builder /usr/bin /usr/bin
COPY --from=builder /home/data /home/data

# Run the script on container start
CMD ["python3", "/home/data/script.py"]


