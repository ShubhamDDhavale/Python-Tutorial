Installation Guide

install vscode 
https://www.youtube.com/watch?v=bN6DE-4uFNo

install python 
https://www.youtube.com/watch?v=C3bOxcILGu4 for python 13

install anaconda
https://www.youtube.com/watch?v=UTqOXwAi1pE

install git
https://www.youtube.com/watch?v=iYkLrXobBb

References 
https://www.w3schools.com/python/
https://pypi.org/project/numpy/

Create Conda environment
conda create --name myenv
conda create --name myenv python=3.11

Activate conda environment
conda activate myenv
conda deactivate


python -m venv venv
venv\Scripts\activate
source venv/bin/activate
deactivate


Run commands 
python main.py

flask
Django python manage.py runserver
fastapi uvicorn main:app --reload
tensorflow python -c "import tensorflow as tf; print(tf.__version__)"
scrapy scrapy crawl spider_name
celery celery -A tasks worker --loglevel=info
streamlit streamlit run app.py
