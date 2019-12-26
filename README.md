# REST_key_val_store

This is a RESTful API that supports the following HTTP requests:

- GET
- POST
- PATCH

These are the following endpoints:

 - ### /values/ GET
 This endpoint returns all the key-value pairs that are stored in the database.

 - ### /values?key=key1,key2 GET
 Returns the key-value pairs based on the query keys

 - ### /values/ POST
 Stores one or more key-value pairs

 - ### /values PATCH
 Updates one or more pairs with new values based on the keys
 