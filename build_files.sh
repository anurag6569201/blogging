# Install dependencies
pip install -r requirements.txt

# Collect static files (if applicable)
python3.9 manage.py collectstatic --noinput
