# Test task for backend developer

1. Clone this project;
2. Build and run the project using Docker; 
`docker-compose up -d --build`;
3. After launching please check `localhost:80` in your browser - you have to see simple form with a login and password 
input fields, and submit button. You can click submit button to be sure local version application is working as well 
as backend part of the application sending to you "empty" response.
4. Migrations task:
    - using the basic migration tools of the Django framework create empty tables for users and for users sessions, 
    tables names isn't important;
    - using the basic migration tools of the Django framework populate table with a users. You should add at least one user;  
    - using the basic migration tools of the Django framework create empty table for goods, table name should be `goods`. 
    This table should have the same structure as `json` file located in `data/goods.json` and additionally should have
    id field with autoincrement as a primary key. At this step table should be empty.
Please be note, new migrations files should appear at the folder `migrations/migrations/*`;   
5. Backend code task... So turn back to clause 3. You have to create code on the backend part that should check eather
user exist in table with a users or not after click a submit button:
    - If user exist there should be:
        - create a record to the table with a users sessions with a specifying date and time of session opening;
        - backend code should read `json` file located in `data/goods.json` and transfer all data from this file to 
        the table `goods` that you already have been created (code should add records to the table every time when 
        the user were found);
        - return a `json` with a success information;
    - If the user does not exist there should be: 
        - return a `json` with information that user does not exist;
6. In the process of creating backend code:
    - you can use both standard mechanisms built into the Django framework or create your own classes, methods, functions etc.
    - it's not necessary to take care about data validation on a backend part, but if you will do it - it will be great;
7. How we will be checked:
    - project should be launching using Docker;
    - after project launch we execute command for migration applying. In the database should be created tables for 
    users (at least with one record), users sessions (empty) and table `goods` (empty).
    - on the page `localhost:80` we type not existing user login and password and should receive information user 
    doesn't exist and no other actions should happen;
    - on the page `localhost:80` we type user login and password (please sent us the password if you are planing to 
    use password encryption) from the table users and should receive information about successful login. In the table 
    users sessions should appear new row. The table `goods` should be populated with all record from the file 
    `data/goods.json`, please be note that populating should happen every time when user exist, no need to take care
    about duplicating records;
8. After you finish please create an archive with your solution and send it to your supervisor by **email**.
