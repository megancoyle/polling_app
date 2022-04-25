=====
Polls
=====

Polls is a simple Django app to conduct Web-based polls. For each
question, visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "polls" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'polls',
    ]

2. Include the polls URLconf in your project urls.py like this::

    url(r'^polls/', include('polls.urls')),

3. Create your virtual environment: `python3 -m venv venv`

4. Activate the environment: `. venv/bin/activate`

5. Install the requirements: `pip install -r requirements.txt`

6. Run `python3 manage.py migrate` to create the polls models.

7. Start the development server, `python3 manage.py runserver` and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

8. Visit http://127.0.0.1:8000/polls/ to participate in the poll.
