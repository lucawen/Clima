cd /home/wbeirigo/chart
./phantomjs highcharts-convert.js -host 10.3.0.29 -port 3003

cd /home/wbeirigo/Clima/weather/proj
python manage.py runserver 10.3.0.29:8080
