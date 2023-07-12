## Library Management System
1. Created a library catalogue where the library staffs can add, edit or delete books. <br />
2. Also, library staffs can view the books loaned by each student. <br />
3. A book can only be loaned if it has a quantity of more than zero in the library catalogue. <br />
4. Each student can borrow many books at one time. <br />
5. Each book can be borrowed by many students. <br />
6. There are three tables or 'apps', for this project, namely, Student, BookLoan and Book. <br />
7. The database tables are created using the inheritance of the models class from Django. <br />
8. The CRUD operations for each tables are created using class-based views. <br />
9. There are three files needed for the deployment of Django on Heroku, runtime.txt, requirements,txt and Procfile
10. requirements.txt states the pip dependencies of the project
11. These three files should have the same file heritance level as manage.py

Technologies used: Django, SQLite, HTML, CSS <br />

Note: 
* To calculate the required return date, which is 14 days from the book issue date, override the save function in the BookLoan model
* To only allow books that have a quantity of more than zero to display on the book loan form, use limit_choices_to field in models.ForeignKey


## How to Start Django Server Locally (after git clone)
1. cd libman/libman
2. python3 -m venv venv
3. source venv/bin/activate
4. pip install -r requirements.txt
5. python manage.py runserver
<br />

Note:
* Skip Step 2 and Step 4 if venv available in local libman folder



