build:
	docker build -t response_collector .

run:
	docker run -it -p 9999:9999 --rm response_collector bash
