TAG = samirtalwar/one-track-web-server

build:
	docker build --tag=$(TAG) .

check: build
	./test $(TAG)
	flake8 app.py

push: build check
	git push
	docker push $(TAG)
