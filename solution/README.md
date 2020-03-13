## Installation / Usage places API

#### Dependencies
* You can use the virtual environment you want, just install the requirements-dev.txt with pip:
	```
	$ pip install -r requirements-dev.txt
	```
* **Note:** requirements.txt has gunicorn and psycopg2 just for heroku you do not need in your env.

* Create an **.env** file in solution/myapi and insert the following variables:
	```
	SECRET_KEY=InsertASecretKeyHere
	DEBUG=True
	```

#### Run API in your local machine
* Ensure you are in solution/myapi. Create the database and runserver:
	```
	$ python3 manage.py migrate
	```
	```
	$ python3 manage.py runserver
	```

#### Run tests
* Ensure you are in solution/myapi and run:
	```
	$ coverage run manage.py test
	```
* You can view the coverage report and generate the html running:
	```
	$ coverage report
	```
	```
	$ coverage html
	```
* Find the html in /solution/myapi/htmlcov/index.html

#### Endpoints

* **You can use heroku or your local endpoint**

* Base endpoint:
	```
	https://bcp-places-api.herokuapp.com
	http://127.0.0.1:8000
	```

* Request Syntax to create a place:

		response = client.post(
			"/place/",
			data={
				"name": "String",
				"slug": "Slug",
				"city": "String",
				"state": "String"
			}
		)

* Request Syntax to get all places:
		
		response = client.get("/place/")

* Request Syntax to get a specific place:
	
		response = client.get("/place/<int:id>/")

* Request Syntax to update a place:
	
		response = client.put(
			"/place/<id>/",
			data={
				"name": "String",
				"slug": "Slug",
				"city": "String",
				"state": "String"
			}
		)
	
* Request Syntax to delete a place:
		
		response = client.delete("/place/<id>/")

* **Delete a place returns 204 status only. The other methods contain response.status and response.data**

* Response Syntax to create, update and get a specific place:
	
		{
			"id": Int,
			"name": String,
			"slug": "Slug",
			"city": "String",
			"state": "String",
			"created_at": "String", # '2020-03-13T04:08:19.957061Z'
			"updated_at": "String", # '2020-03-13T04:08:19.957061Z'
		}

* Response Syntax to get all places:
	
		[
			{
				"id": Int,
				"name": String,
				"slug": "Slug",
				"city": "String",
				"state": "String",
				"created_at": "String", # '2020-03-13T04:08:19.957061Z'
				"updated_at": "String", # '2020-03-13T04:08:19.957061Z'
			}
		]


#### Status table

| Code | Status |
|:-------:|:---------:|
| 200   | OK |
| 201   | CREATED |
| 204   | NO_CONTENT |
| 400   | BAD_REQUEST |
| 404   | NOT_FOUND |
