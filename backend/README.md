## Enviorment:

.venv\Scripts\activate
deactivate

## Start API

python manage.py runserver

# Run tests for a specific app

python manage.py test api --settings=wander_wise.test_settings

## Run tests for a specific module

python manage.py test api.tests.test_models

# Run a specific test case

python manage.py test api.tests.test_open_ai_service --settings=wander_wise.test_settings
python manage.py test api.tests.test_trips_service --settings=wander_wise.test_settings
python manage.py test api.tests.test_views --settings=wander_wise.test_settings
