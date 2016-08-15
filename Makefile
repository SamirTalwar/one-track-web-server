TAG = samirtalwar/one-track-web-server

build:
	docker build --tag=$(TAG) .

check: build
	./test $(TAG)
	flake8 app.py