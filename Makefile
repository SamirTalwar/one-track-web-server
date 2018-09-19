TAG = samirtalwar/one-track-web-server

.PHONY: build
build:
	docker build --tag=$(TAG) .

.PHONY: check
check: build Pipfile.lock
	./test $(TAG)
	pipenv run flake8 app.py

.PHONY: push
push: build check
	git push
	docker push $(TAG)

Pipfile.lock: .environment Pipfile
	pipenv sync

.environment:
	pipenv install --three
	touch .environment
