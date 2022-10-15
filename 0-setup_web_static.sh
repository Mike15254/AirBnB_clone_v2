#!/usr/bin/env bash
# sets up server
apt-get -y update
apt-get -y install nginx
mkdir -p /data/web_static/shared/ /data/web_static/releases/test/
echo \
'<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>' > /data/web_static/releases/test/index.html
rm -f /data/web_static/current
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -hR ubuntu:ubuntu /data
CONF="server {
	listen 80 default_server;
	listen [::]:80 default_server;
	root /var/www/html;
	index index.html index.htm index.nginx-debian.html;
	server_name _;
	location / {
		try_files \$uri \$uri/ =404;
	}
	if (\$request_filename ~ redirect_me){
		rewrite ^ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
	}
	error_page 404 /404.html;
	location = /404.html {
		root /var/www/error/;
		internal;
	}
	location /hbnb_static/ {
		alias /data/web_static/current/;
	}
}"
echo "$CONF" > /etc/nginx/sites-available/default
service nginx reload
