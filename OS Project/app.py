import flask
from flask import Flask, render_template # for web app
from tkinter import * 
import tkinter.filedialog ,os
from PIL import Image, ImageTk, ImageDraw, ImageOps, ImageEnhance
import pytesseract, re, itertools
import pytesseract
import subprocess
import PIL     #star import not used due to namespace conflict of Image function(present in both Tkinter and PIL)
from os.path import join
pytesseract.pytesseract.tesseract_cmd = '/Users/janan/OneDrive/Desktop/OS Project/Tesseract-OCR/tesseract.exe'
import threading 
import time

app = Flask(__name__)


@app.route('/')
def base():
    return render_template('base.html')

@app.route('/image.html', methods = ['GET','POST'])
def image():
    return render_template('image.html')

@app.route('/text.html', methods = ['GET','POST'])
def text():
    return render_template('text.html')

if __name__ == '__main__':
    app.run()
