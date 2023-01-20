# python-object_relational_mapping
## Background Context
In this project, we will link two amazing worlds: Databases and Python!

In the first part, we will use the module MySQLdb to connect to a MySQL database and execute our SQL queries.

In the second part, we will use the module SQLAlchemy - an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, our biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. We won’t write any SQL queries only Python code. Last thing, our code won’t be “storage type” dependent. We will be able to change our storage easily without re-writing our entire project.

## Requirements
- install MySQL on Ubuntu 20.04 using the command `sudo apt install mysql-server`
- install MySQLdb in the following procedure
`sudo apt-get install python3-dev \n
sudo apt-get install libmysqlclient-dev \n
sudo apt-get install zlib1g-dev \n
sudo pip3 install mysqlclient`
- install SQLAlchemy `sudo pip3 install SQLAlchemy`
