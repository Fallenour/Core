##################################################################################################
#                                           Flask                                                #
##################################################################################################

# entire flask environment,  application, and demo flask app #

# Build environment #
app install python3-pip python3-dev nginx
pip install venv gunicorn flask

# Build flask project file #
nano project.py

from flask import Flask


app = Flask(__name__)

@app.route("/")
def h():
    return "test"

if __name__ == "__main__":
    app.run(host = "0.0.0.0")

# Build WSGI server #
nano wsgi.py

from project import app as application


if __name__=="__main__":
    app.run()

# Run flask application on WSGI server and bind it #
gunicorn --bind 0.0.0.0:8000 wsgi



# Sources #
https://www.linode.com/docs/guides/create-restful-api-using-python-and-flask/prog_lang_app.txt
https://www.linode.com/docs/guides/create-restful-api-using-python-and-flask/
https://blog.miguelgrinberg.com/post/using-celery-with-flask
https://www.tutorialspoint.com/flask/flask_application.htm
https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3
https://realpython.com/python-microservices-grpc/
