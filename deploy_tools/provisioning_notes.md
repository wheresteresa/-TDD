Provisioning a new site
=======================

## Required packages:

* nginx
* python 3.8
* virtualenv + pip
* Git

eg, on Ubuntu:
		
		sudo add-apt-repository ppa:fkrull/deadsnakes
		sudo apt-get install nginx git python 3.8 python3.8-venv


## Nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with, e.g., staging.my-domain.com

##Systemd service

* see gunicorn-systemd.template.service
* replace SITENAME with, e.g., staging.my-domain.com

## Folder structure:
Assume we have a user account at /home/username

/home/username
|____sites
		|____SITENAME
				|____database
				|____source
				|____static
				|____virtualenv