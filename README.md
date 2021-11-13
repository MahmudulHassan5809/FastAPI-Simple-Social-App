## Project  Description
	Small and Simple Social App Using FastAPI , Sqlalchemy, Postgres, JWT
	Live Link : https://fatapi-social-5809.herokuapp.com/docs

## Project Feature
	This project has mainly two section
	Account  section (Create , Update account)
	Post Section (Add , Read, Update, Delete Post & Like Post)

## ENV VARIABLE
	Create a .env file & put these ENV variable value
	DATABASE_HOSTNAME=localhost
	DATABASE_PORT=5432
	DATABASE_PASSWORD=********
	DATABASE_NAME=********
	DATABASE_USERNAME=********
	SECRET_KEY=********
	ALGORITHM=HS256
	ACCESS_TOKEN_EXPIRE_MINUTES=30

## To Run This Project
	Install all the dependencies  
	Create virtual env 
	python3 -m venv ./venv
	Activate venv 
	source venv/bin/activate
	pip install -r requirements.txt
	Run the app 
	uvicorn app.main:app --reload