build:
	docker build -t cle-no-te-nginx-proxy .

run-docker: clean build
	docker run -p 80:80 --name cle-no-te-nginx-proxy-container cle-no-te-nginx-proxy

backend:
	python3 backend.py

clean:
	docker rm -f cle-no-te-nginx-proxy-container
	docker rmi cle-no-te-nginx-proxy