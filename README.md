For realtime /chat

docker run -p 6379:6379 -d redis:2.8

web: newrelic-admin run-program gunicorn backend_2018.wsgi
