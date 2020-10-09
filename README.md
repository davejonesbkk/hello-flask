# hello-flask
Simple hello world web app with Flask in Docker

Build the image:

    docker build -t hello-flask:latest .
    
Run the container:

    docker run -d -p 5000:5000 hello-flask 
