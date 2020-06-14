NOT_A_SQUARE_BACKUP_TOOLS_API_MYSQL_HOST_PORT=3330
NOT_A_SQUARE_BACKUP_TOOLS_API_WEB_HOST_PORT=8019
NOT_A_SQUARE_BACKUP_TOOLS_ADMIN_MYSQL_HOST_PORT=3331
NOT_A_SQUARE_BACKUP_TOOLS_ADMIN_WEB_HOST_PORT=8023
NOT_A_SQUARE_BACKUP_TOOLS_HOME=$(NOT_A_SQUARE_HOME)/not-a-square-zero-mysql-backup-tool

create-storage:
	sudo docker run -d --name=not-a-square-dev.backup-tools-api.mysql.storage \
		registry.novogenialab.com/notasquare-zero/images/standard-mysql:0.1 true
	sudo docker run -d --name=not-a-square-dev.backup-tools-admin.mysql.storage \
		registry.novogenialab.com/notasquare-zero/images/standard-mysql:0.1 true

clear-storage:
	-sudo docker stop not-a-square-dev.backup-tools-api.mysql.storage
	-sudo docker rm not-a-square-dev.backup-tools-api.mysql.storage
	-sudo docker stop not-a-square-dev.backup-tools-admin.mysql.storage
	-sudo docker rm not-a-square-dev.backup-tools-admin.mysql.storage

deploy:
	sudo docker run -d --name=not-a-square-dev.backup-tools-api.mysql \
		--volumes-from=not-a-square-dev.backup-tools-api.mysql.storage \
		-p $(NOT_A_SQUARE_BACKUP_TOOLS_API_MYSQL_HOST_PORT):3306 \
		registry.novogenialab.com/notasquare-zero/images/standard-mysql:0.1
	sudo docker run -d --name=not-a-square-dev.backup-tools-api.web \
		--link not-a-square-dev.backup-tools-api.mysql:mysql \
		-v $(NOT_A_SQUARE_BACKUP_TOOLS_HOME)/api-web/src/www:/opt/www \
		-p $(NOT_A_SQUARE_BACKUP_TOOLS_API_WEB_HOST_PORT):80 \
		not-a-square-zero-backup-tools/api-web/dev

	sudo docker run -d --name=not-a-square-dev.backup-tools-admin.mysql \
		-p $(NOT_A_SQUARE_BACKUP_TOOLS_ADMIN_MYSQL_HOST_PORT):3306 \
		registry.novogenialab.com/notasquare-zero/images/standard-mysql:0.1
	sudo docker run -d --name=not-a-square-dev.backup-tools-admin.web \
		--link not-a-square-dev.backup-tools-admin.mysql:mysql \
		--link not-a-square-dev.backup-tools-api.web:backup-tools-api \
		-v $(NOT_A_SQUARE_BACKUP_TOOLS_HOME)/admin-web/src/www:/opt/www \
		-p $(NOT_A_SQUARE_BACKUP_TOOLS_ADMIN_WEB_HOST_PORT):80 \
		not-a-square-zero-backup-tools/admin-web/dev

	sudo cp nginx/not-a-square-backup-tools-api-web /etc/nginx/sites-enabled
	sudo cp nginx/not-a-square-backup-tools-admin-web /etc/nginx/sites-enabled
	sudo service nginx reload

	sleep 30

	-sudo docker exec -it not-a-square-dev.backup-tools-api.mysql mysql -uroot -p123456 -e "CREATE DATABASE IF NOT EXISTS api_db;"
	-sudo docker exec -it not-a-square-dev.backup-tools-api.web python /opt/www/manage.py migrate

	-sudo docker exec -it not-a-square-dev.backup-tools-admin.mysql mysql -uroot -p123456 -e "CREATE DATABASE IF NOT EXISTS admin_db;"
	-sudo docker exec -it not-a-square-dev.backup-tools-admin.web python /opt/www/manage.py migrate
	-sudo docker exec -it not-a-square-dev.backup-tools-admin.web python /opt/www/manage.py linkstatic

clean:
	-sudo docker stop not-a-square-dev.backup-tools-admin.mysql
	-sudo docker stop not-a-square-dev.backup-tools-admin.web

	-sudo docker stop not-a-square-dev.backup-tools-api.mysql
	-sudo docker stop not-a-square-dev.backup-tools-api.web

	-sudo docker rm not-a-square-dev.backup-tools-admin.mysql
	-sudo docker rm not-a-square-dev.backup-tools-admin.web

	-sudo docker rm not-a-square-dev.backup-tools-api.mysql
	-sudo docker rm not-a-square-dev.backup-tools-api.web

	-sudo rm /etc/nginx/sites-enabled/not-a-square-backup-tools-api-web
	-sudo rm /etc/nginx/sites-enabled/not-a-square-backup-tools-admin-web


start:
	sudo docker start not-a-square-dev.backup-tools-api.mysql
	sudo docker start not-a-square-dev.backup-tools-api.web
	sudo docker start not-a-square-dev.backup-tools-admin.mysql
	sudo docker start not-a-square-dev.backup-tools-admin.web

stop:
	sudo docker stop not-a-square-dev.backup-tools-api.mysql
	sudo docker stop not-a-square-dev.backup-tools-api.web
	sudo docker stop not-a-square-dev.backup-tools-admin.mysql
	sudo docker stop not-a-square-dev.backup-tools-admin.web

migrate:
	-sudo docker exec -it not-a-square-dev.backup-tools-api.web python /opt/www/manage.py migrate
	-sudo docker exec -it not-a-square-dev.backup-tools-admin.web python /opt/www/manage.py migrate

ssh-api-mysql:
	sudo docker exec -it not-a-square-dev.backup-tools-api.mysql bash

ssh-api-web:
	sudo docker exec -it not-a-square-dev.backup-tools-api.web bash

ssh-admin-mysql:
	sudo docker exec -it not-a-square-dev.backup-tools-admin.mysql bash

ssh-admin-web:
	sudo docker exec -it not-a-square-dev.backup-tools-admin.web bash
