#!/bin/bash

# Parse command line arguments
environment="production"  # Default to production
for arg in "$@"
do
    case $arg in
        --environment=*)
            environment="${arg#*=}"
            shift
            ;;
        *)
            # Unknown argument
            ;;
    esac
done

# Collect static files
python manage.py collectstatic --no-input

# Run different commands based on environment parameter
if [ "$environment" = "local" ]; then
    # Run Django dev server for local development
    python manage.py runserver 0.0.0.0:8000
else
    # Run Gunicorn server for other environments (staging, production)
    gunicorn books_api_service.wsgi:application -b 0.0.0.0:8000
fi