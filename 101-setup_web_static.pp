# puppet script that sets up web servers for the deployment of web_static
exec {'update system':
	provider => 'shell',
	command  => 'sudo apt-get update',
} ->
	
package {'nginx':
	provider => 'apt',
	ensure   => 'installed',
} ->

# exec {'create folders':
#	provider => 'shell',
#	command  => 'sudo mkdir -p /data/web_static/{shared,releases/test}',
#}->

file { '/data':
  ensure => 'directory',
} ->

file { '/data/web_static':
  	ensure => 'directory',
} ->

file { '/data/web_static/releases':
  	ensure => 'directory',
} ->

file { '/data/web_static/shared':
  	ensure => 'directory',
} ->

file {'/data/web_static/releases/test':
	ensure => 'directory',
} ->

file {'create index':
	ensure   => 'file',
	path     => '/data/web_static/releases/test/index.html',
	content  =>@(EOF)
<html>
	<head>
	</head>
	<body>
		Holberton School
	</body>
</html>
EOF
} ->

exec {'delete old symlink':
	provider => 'shell',
	command  => 'sudo rm -rf /data/web_static/current',
	unless   => 'test ! -e /data/web_static/current',
} ->
	
exec {'create new symlink':
	provider => 'shell',
	command  => 'sudo ln -sf /data/web_static/releases/test /data/web_static/current',
} ->

exec {'grant ownership':
	provider => 'shell',
	command  => 'sudo chown -R ubuntu:ubuntu /data/',
} ->

file {'update nginx file':
	ensure  => 'link',
	path    => '/etc/nginx/sites-enabled/default',
	content =>@(EOF)
server {
	listen 80 default_server;
	listen [::]:80 default_server;
	add_header X-Served-By $hostname;

	root /var/www/html;
	index index.html;

	server_name _;

	location /hbnb_static {
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
} ->
	
service {'nginx':
	ensure  => 'running',
} ->
	
exec {'restart nginx':
	provider => 'shell',
	command  => 'sudo service nginx restart',
}
