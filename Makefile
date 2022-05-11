SHELL := /bin/bash

init: 
	(	python3 -m venv venv; \
		source venv/bin/activate; \
		python3 -m pip install --upgrade pip; \
		pip install -r ./requirements.txt;\
	)

freeze:
	(	source venv/bin/activate; \
		pip freeze > ./requirements.txt; \
	)

#########
flask_run:
	(	source venv/bin/activate; \
		# export FLASK_APP=app:app; \
		export FLASK_DEBUG=true; \
		flask run; \
	)
#########
terraform_init:
	(	cd ./terraform; \
		terraform init; \
	)

terraform_plan:
	(	cd ./terraform; \
		terraform plan; \
	)

terraform_apply:
	(	cd ./terraform; \
		terraform apply; \
	)

terraform_destroy:
	(	cd ./terraform; \
		terraform destroy; \
	)