# build_files.sh
echo "Build Start"
python -m pip install -r requirements.txt
python manage.py collectstatic --noinput --clear

echo "BuildEnd"