mkdir repos
cd repos
git clone https://github.com/CunhaLuis/alarmExample
cd alarmExample

sudo apt install python3-venv
sudo apt install python3-pip
python3 -m venv venv
. venv/bin/activate
pip install Flask

pip install flask_apscheduler
pip install requests




FLASK_APP=doctorOffice/doctorOffice.py NAME=Dr1 flask run
