#!/usr/bin/env bash
# sets up the web servers for the deployment of web_static
apt-get update
apt-get install -y nginx
mkdir -p /data/web_static/releases/test
mkdir /data/web_static/shared/
echo "Holberton School" > /data/web_static/releases/test/index.html
ln -s /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
file=/etc/nginx/sites-available/default
cp $file $file.original
sed -i 's|^server {|server {\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n|' $file
service nginx restart
