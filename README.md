# RESTfull API

1. Clone repository
```sh
git clone 
```
2. Change dir to project folder
```sh
cd 
```
3. Create virtual environment
```sh
python3 -m venv .venv
```
4. Activate environment
```sh
source ./.venv/bin/activate
```
5. Install dependency
```sh
pip install -r ./requirements
```
6. Run tests
```sh
pytest
```
7. Run localy
```sh
python ./start.py
```
8. Build and start project in docker ([docker](https://docs.docker.com/engine/install/) must be installed on your machine)
```sh
docker compose -f compose-dev.yaml up -d --build
```
9. project avaliable on  http://0.0.0.0:8000/docs
10. Stop docker container
```sh
docker compose -f compose-dev.yaml down && docker network prune --force
```
