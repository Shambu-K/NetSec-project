# This Dockerfile sets up an Nginx web server
# with a custom configuration file

FROM nginx:latest

# Copy our custom Nginx configuration file
COPY nginx.conf /etc/nginx/nginx.conf

# Expose the default HTTP port
EXPOSE 80

# Start Nginx with our custom configuration file
CMD ["nginx", "-g", "daemon off;"]
