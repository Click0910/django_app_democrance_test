This is a tech assessment for democrance.

The Project is built in Django and Django Rest Framework. This project is just a prototype that simulate the data flow in the process when an user make a quote and buy an insurance policy.
This is just a prototype and is not ready for production. Handler errors, exceptions, more unit testing, must to be added and consider (for now I don’t have full requirements).


------------------------

**Structure**

This project follow the next structure:

	django_project
	|	myproject/
	|	|-- myproject/
	|	|-- customers/
	|	|-- quotes/
	|	|-- manage.py


As I mentioned before, this is just a prototype. One good improvement could be instead of have just two Django apps (customer and quotes) taking into account that in a real project the code tends to get bigger and scale would be better to add a third Django app (for example policy), like this:

	django_project
	|	myproject/
	|	|-- myproject/
	|	|-- customers/
	|	|-- quotes/
    |	|-- policies/
	|	|-- manage.py

-----------------------

**DB**

The project use de SQLite DB that comes by default with Django, However for production and in a real project the DB must to be migrated to a robust SQL DB like Postgres. In case that the schema of the data will be dynamic, transactions wont be important and we are looking for performance, a NoSQL DB can works perfectly.


----------------------

**Caching**

In a real project and in order to reduce the stress in the main DB, is important to implement a caching strategy for example using and implementing a Redis server.
I wrote the next article in medium.com: 
https://medium.com/@nicolas1009/integrating-redis-with-backend-in-minikube-a-step-by-step-guide-part-3-806f00851606 \

The article is part of an article series that I’m writing about a search engine implementation. The article describe how to implement for development Purposes a Redis server and integrated with a backend (in the article is implemented using FastAPI but the principles are same)
This is my medium profile: 

https://nicolas1009.medium.com/


----------------------------------

**Endpoints and doc.**

In a real project is recommended to write the documentation using Swagger for exaple, but for this test with this readme 
doc will be enough.

This project have the next endpoints:


1. POST http://127.0.0.1:8000/api/v1/create_customer

    {
        "first_name": "Ben",
        "last_name": "Stokes",
        "dob": "25-06-1991"
    }
2. GET http://127.0.0.1:8000/api/v1/search  -> List all the customers.
3. POST http://127.0.0.1:8000/api/v1/quotes 

   {
     "customer": 123,  // ID of an existing user
     "policy": 456,    // ID of an existing policy
     "age_band": "25-35", // Example age band
     "quoted_premium": "150.00" // Quoted premium as a decimal string
   }

4. POST http://127.0.0.1:8000/api/v1/quotes/<int:pk>/accept/

    {
      "type": "personal-accident",
      "premium": "100.00",
      "cover": "50000.00",
      "state": "new",
      "is_accepted": false,
      "customer": 1
    }
5. PUT http://127.0.0.1:8000/api/v1/quotes/<int:pk>/update/ -> You can think as a pyment

    {
      "type": "personal-accident",
      "premium": "100.00",
      "cover": "50000.00",
      "state": "new",
      "is_accepted": true,
      "customer": 1
    }
6. GET http://127.0.0.1:8000/api/v1/policies -> List all the policies.
7. GET http://127.0.0.1:8000/api/v1/policies/<int:pk>/ -> Get policy details.
8. GET http://127.0.0.1:8000/api/v1/policies/<int:pk>/history/ -> Get policy history


More endpoints can be added on base of requirements.
Endpoints need to be improved with more exceptions and more handle error.

----------------

**Execution:**

You can execute using a dokcer or locally:

_****_docker**_**_


docker build -t my_django_app .

docker run -p 8000:8000 my_django_app


**__****_or locally**__****_

pip install requirements.txt

cd myproject

python manage.py runserver 



