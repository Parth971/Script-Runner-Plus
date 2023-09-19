# Use the official Mosquitto image as a parent image
FROM eclipse-mosquitto:2

# Expose MQTT ports
EXPOSE 1883
EXPOSE 9001

# Copy your Mosquitto configuration file to the container
COPY mosquitto.conf /mosquitto/config/mosquitto.conf

# Start Mosquitto
CMD ["mosquitto", "-c", "/mosquitto/config/mosquitto.conf"]
