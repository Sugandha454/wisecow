# Use an official Ubuntu as the base image
FROM ubuntu:latest

# Install dependencies and cowsay
RUN apt-get update && \
    apt-get -y install fortune cowsay 
RUN apt-get install -y netcat-openbsd
RUN cp -pr /usr/games/fortune /bin/fortune
RUN cp -pr /usr/games/cowsay /bin/cowsay
# Print a message using cowsay and fortune

# Set the working directory
WORKDIR /app

# Copy the script into the container
COPY wisecow.sh /app/wisecow.sh

# Make the script executable
RUN chmod +x /app/wisecow.sh

# Modify .bashrc to set cowsay as fortune


# Expose the port that the server will run on
EXPOSE 4499

# Run the script
CMD ["/app/wisecow.sh"]
