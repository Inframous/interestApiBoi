FROM python:3.10

# Install required packages
RUN apt-get update && \
    apt-get install -y wget gnupg2 unzip python3 python3-pip curl && \
    rm -rf /var/lib/apt/lists/*

# Download and install Google Chrome
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list && \
    apt-get update && \
    apt-get install -y google-chrome-stable && \
    rm -rf /var/lib/apt/lists/*

# Create a non-root user to run the app


# Set the working directory to the home folder of the app user
WORKDIR /app


# Install requirements
COPY requirements.txt .
RUN pip3 install -r /app/requirements.txt

# Copy the Python app to the container
COPY . . 

EXPOSE 80

# Run the Python app
CMD ["python3", "app.py"]