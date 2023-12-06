build:
	docker build -t response_collector .

run:
	docker run -it -p 54321:443 --rm response_collector
