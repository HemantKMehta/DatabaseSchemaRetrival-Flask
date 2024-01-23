Please follow this google drive link https://drive.google.com/file/d/1b-n_dGcGawaDBWVbU9MQ7L4FbmK0JBaw/view?usp=sharing for the video introduction. Please download the video for better quality. 

Take-home Assignment for Senior Backend Engineer Project

I have developed this database schema extraction API in Flask. I have used MySQL database. It has three main endpoints along with a welcome end point with API details. The subsequent paragraphs discuss the main endpoints:

    1. Endpoint to provide database credentials: This is the essential endpoint to be invoked first before other two endpoints to set the database username and password. This endpoint should be used to pass the database credential to be used by other two endpoints (to get schema of a database and to search table in a database).
      
        URL: http://localhost:5000/users
        
        Input: username and password, passed from the login.html file from the project folder using http post method.
        
        Output: Stores the credential to the users.txt file in the project home folder.

    2. Endpoint to retrieve database schema: This endpoint displays the database name, name and column details of all tables in the database. 
    
      URL: http://localhost:5000/schema/<dbname> 
      
      Input: MySQL database name passed as flask route parameter 
      
      Output: Start with the database name and then one by one following details of each table 
      
          1. Table name,
          
          2. Column details of the table 
    
    3. Endpoint to search a table in database: This endpoint searches for a given table name in the given database. If the table is found it will display the column details of the table. 
      
      URL: http://localhost:5000/table/<dbname>/<tablename> 
      
      Input: MySQL database name and a table name passed as flask route parameter
      
      Output: It displays the column details of the table if it is found in the database, otherwise it displays: there is no table in the database with name <tablename>
