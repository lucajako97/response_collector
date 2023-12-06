build:
	docker build -t response_collector .

run:
	docker run -it -p 54321:80 --rm response_collector bash
