# response_collector

The purpose of this repo is to have a docker container for testing the protocol of a couple of routers.

## Composition

After running the docker container there will be two components:

*	A python flask web server that is answering with static response
*	A Stunnel server configuration file to setup the proxy server

## How to run

To create the docker image:
```make build```

To execute the docker container:
```make run```

Then you need to execute also another instance for the docker container:
```
docker exec -it <container_id> bash
```

Run the python back end server in the first instance:
```
python3 flask_app.py
```

and the stunnel proxy server in the second one:
```
stunnel stunnel_server.conf
```

Now the container is ready!

## MISSING

The psk.txt is missing because there is the password not encrypted.