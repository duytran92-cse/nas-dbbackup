REGISTRY=registry.novogenialab.com

build:
	sudo docker build -f docker/Dockerfile-dev -t not-a-square-zero-backup-tools/api-web/dev .

release-test:
	sudo docker build --no-cache -f docker/Dockerfile-test -t not-a-square-zero-backup-tools/api-web/test .
	sudo docker tag not-a-square-zero-backup-tools/api-web/test $(REGISTRY)/notasquare-zero/backup-tools/api-web/test
	sudo docker push $(REGISTRY)/notasquare-zero/backup-tools/api-web/test
