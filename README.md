Please follow this Google Drive link https://drive.google.com/file/d/1b-n_dGcGawaDBWVbU9MQ7L4FbmK0JBaw/view?usp=sharing for the video introduction. Please download the video for better quality.

Take-home Assignment for Senior Backend Engineer Project

To run this API, we need a MySQL with a database, a few tables in the database, and a user with access to the database.

To run the application:

1. Copy app.py, login.html and users.txt in a folder

2. Now, from the folder, execute the following command:
   
        python3 app.py

4. It will expose the following four API with the given URLS (for the first time, use the login.html to pass the database credential)
   
       a. Index page: http://localhost:5000/
   
       b. Pass user details: http://localhost:5000/users (open login.html and pass database credentials.

       c. Retrieve Database Schema: http://localhost:5000/schema/dbname

       d. Search for a Table in a Database: http://localhost:5000/table/dbname/tablename
   
           
        
