## Enviorment: 
.venv\Scripts\activate
deactivate

## Start API
python manage.py runserver

## Run tests for a specific app
python manage.py test api

## Run tests for a specific module
python manage.py test api.tests.test_models

## Run a specific test case
python manage.py test api.tests.test_trips_repository.TestTripsRepository.test_save_suggestion