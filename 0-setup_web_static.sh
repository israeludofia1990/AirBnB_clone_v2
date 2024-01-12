#!/usr/bin/env bash
# bash script that sets up web server

# Install nginx if it does not already exist
if ! command -v nginx &> /dev/null; then
	sudo apt update
	sudo apt install -y nginx
fi

# create directory if it does not already exist
sudo mkdir -p /data/web_static/releases/test/
echo "Fake HTML Page!!!" | sudo tee /data/web_static/releases/test/index.html

# variable to store link and target path
link_path="/data/web_static/current"
target_path="/data/web_static/releases/test/"
nginx_config="/etc/nginx/nginx.conf"

#create a symbolic link and delete if the link already exist
if [ -L "$link_path" ]; then
	sudo rm "$link_path"
fi
sudo ln -s "$target_path" "$link_path"

# Give ownership of the /data/ folder to the ubuntu user
sudo chown -hR ubuntu:ubuntu /data/

# add the new location block to the server configuration
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

sudo service nginx start

exit 0
