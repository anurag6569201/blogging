# Install dependencies
pip install -r requirements.txt

# Collect static files (if applicable)
python manage.py collectstatic --noinput

# Run migrations (if applicable)
python manage.py migrate