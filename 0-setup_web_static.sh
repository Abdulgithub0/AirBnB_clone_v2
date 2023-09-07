#!/usr/bin/env bash
# a Bash script that sets up web servers for the deployment of web_static

#install nginx if not installed
if ! dpkg -l | grep -q nginx ; then
	sudo apt-get update
	sudo apt-get install -y nginx
fi

# check for /data/ and its subdirectories if they exist otherwise create
list_dir=("/data/" "/data/web_static/" "/data/web_static/releases" "/data/web_static/shared" "/data/web_static/releases/test/")
for dir in "${list_dir[@]}"; do
	if [ ! -d "$dir" ]; then
		sudo mkdir -p "$dir"
	fi
done

# Create a fake HTML file /data/web_static/releases/test/index.html (with simple content, to test your Nginx configuration)

if [ ! -f "/data/web_static/releases/test/index.html" ]; then
	sudo touch "/data/web_static/releases/test/index.html"
fi

fake_content=$(cat <<EOF
<!DOCTYPE html>
<html>
	<head>
		<title>fake html</title>
	</head>
	<body>
		<h1>Hello World from fake html</h1>
	</body>
</html>
EOF
)

echo "$fake_content" | sudo tee "/data/web_static/releases/test/index.html" >/dev/null

# Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder.
# If the symbolic link already exists, it should be deleted and recreated every time the script is ran.

if [ -h "/data/web_static/current" ]; then
	sudo rm -rf "/data/web_static/current"
fi

sudo ln -sf "/data/web_static/releases/test" "/data/web_static/current"

#Give ownership of the /data/ folder to the ubuntu user AND group (you can assume this user and group exist).
#This should be recursive; everything inside should be created/owned by this user/group.
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static 

content=$(cat <<EOF
server {
	listen 8000 default_server;
	listen [::]:8000 default_server;
	add_header X-Served-By $HOSTNAME;
	
	root /var/www/html;
	index index.html;

	server_name _;

	location = /hbnb_static {
		alias /data/web_static/current;
		index index.html;
	}

	location = /redirect {
		return 301 https://www.alxafrica.com;
	}

	error_page 404 /error.html;
	location /404 {
		internal;
		error_page 404 /error.html;
	}
}
EOF
)

echo "$content" | sudo tee /etc/nginx/sites-enabled/default >/dev/null
sudo service nginx restart
