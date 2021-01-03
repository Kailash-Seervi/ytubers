# ytubers
A website which helps people connect with popular Youtubers from different cities and collaborate with them in business events.

## How to run
1. Clone the repository by copying the clone link or download the compressed file.
2. Make sure the project file is available in your workspace.
3. Make sure you have a version of Python3 installed in your system.
4. Install Python virtual environment if you haven't already. Refer: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/
5. Create a new virtualenv. https://docs.python.org/3/library/venv.html
6. Activate the environment once installed.
7. Change the terminal directory to /tubers/
8. Run the following command to install all dependencies required for the project.
   `pip install -r requirements.txt`
9. Run the following commands in order to populate the SQLite database. `python3 manage.py makemigrations`, `python3 manage.py migrate`, `python3 manage.py collectstatic`
10. Now, you can run the Django server to see the output by running the following command `python3 manage.py runserver`

## Note:
For the user authentication I've used Django's built-in feature, also integrated Google and Facebook login.
For Google and Facebook login to work please refer the following documentation https://django-allauth.readthedocs.io/en/latest/providers.html#google and https://django-allauth.readthedocs.io/en/latest/providers.html#facebook

Thanks!!
