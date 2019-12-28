# REST_key_val_store

This is a RESTful API that supports the following HTTP requests:

- GET
- POST
- PATCH

These are the following endpoints:

 - ### GET /values/
 This endpoint returns all the key-value pairs that are stored in the database.

 - ### GET /values?key=key1,key2
 Returns the key-value pairs based on the query keys

 - ### POST /values/
 Stores one or more key-value pairs

 - ### PATCH /values 
 Updates one or more pairs with new values based on the keys
 

 ## Running the Service

 After activating the virtual environment, just run the command ''' ./runservice.sh ''' in the terminal, the service will start right after the migrations.