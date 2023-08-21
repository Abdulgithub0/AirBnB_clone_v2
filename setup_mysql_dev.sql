-- a script that prepares a MySQL server for this project
-- a development database called hbnb_dev_db will be used
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE DATABASE IF NOT EXISTS performance_schema;
CREATE USER IF NOT EXISTS "hbnb_dev"@"localhost" IDENTIFIED BY "hbnb_dev_pwd";
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO "hbnb_dev"@"localhost";
GRANT SELECT ON "performance_schema" TO "hbnb_dev"@"localhost";
FLUSH PRIVILEGES:
