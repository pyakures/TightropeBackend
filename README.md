# Tightrope Backend

Tightrope is a calender based mental health application designed to give users a visual representation of their work-life balance and pursuade user to make an informed decision to better their mental health.

This project was a senior capstone project for the computer science & enginnering department at the [University of Nevada, Reno](https://www.unr.edu/cse). The team members for this project were Mackenzie Z, Sahil P, Demitri B, Michael D, and Cooper F.

This project is a Django based python backend and uses [Tightrope](https://github.com/pyakures/Tightrope) for the front end user interface. This project was forked from the [original source code](https://github.com/mdoradocode/TightropeBackend) to update documentation.

#### Note: This project is deprecated and no longer maintained by the developers.

## Building & Running

For setting up Tightrope Backend for use on a local machine, follow the steps below.

Clone the repository to a local disk space using Github.

### macOS:

1. Ensure python is installed:
   python --version
   This should be version 3.9 or greater. If it shows as 2.x, you may have python3 installed. Simply do: python3 --version

   If this is the case, you can either change it using another guide or you can do all python commands using python3 instead of python.

2. Navigate to the project root folder and create a virtual environment and activate it:
   python -m venv venv  
   source venv/bin/activate

3. Install the requirements using pip:
   pip install -r requirements.txt

   #### Note: If you run into an issue while installing the dependencies, you might have to install postgres. For example: brew install postgresql.

4. Create a super user for the database
   python manage.py createsuperuser

5. Run migrations:
   python manage.py makemigrations
   python manage.py migrate

6. Start the Django project using:
   python manage.py runserver

Please refer to the [original source code documentation](https://github.com/mdoradocode/TightropeBackend/blob/main/ReadMe.txt) if needed.
