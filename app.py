############Glogle#########
import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys
##############Ocean###########
import sqlite3
from flask import Flask
######Configure_OCEAN#########
DATABASE = "./flaskr.db"
SECRET_KEY = "pudim"
USERNAME = "admin"
PASSWORD = "admin"
######Aplicação OCEAN#########
app = Flask(__name__)
app.config.from_object(__name__)
#@app.route('/')
#def index():
    #leitura=open("./arqText.txt", "r")
    #print (leitura.read())
    #leitura.close()
    #return (leitura)
def connect_db():
    return sqlite3.connect(DATABASE)
##############Google###########
def _upload():

    _upload_widget = fileupload.FileUploadWidget()

    def _cb(change):
        global file_contents
        decoded = io.StringIO(change['owner'].data.decode('utf-8'))
        filename = change['owner'].filename
        print('Uploaded `{}` ({:.2f} kB)'.format(
            filename, len(decoded.read()) / 2 **10))
        file_contents = decoded.getvalue()

    _upload_widget.observe(_cb, names='data')
    display(_upload_widget)

_upload()