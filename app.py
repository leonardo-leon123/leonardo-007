from flask import Flask, render_template, url_for, request
import requests
import os
subscription_key = "33aa870e5d29431887c452b2b3d95d17"

endpoint = "https://elsy.cognitiveservices.azure.com/"

languages_url = endpoint + "/text/analytics/v3.0/languages"

app = Flask(__name__)

@app.route('/',methods=["POST","GET"])
def index():
    if request.method == "POST":
        idioma = request.form['descripcion'] 
        documents= {
            "documents": [
            {
            "id": "1",
            "text": idioma
            }]
        } 
        headers = {"Ocp-Apim-Subscription-Key": subscription_key}
        response = requests.post(languages_url, headers=headers, json=documents)
        languages = response.json()
        idioma_encontrado = languages['documents'][0]['detectedLanguage']['name']            
    return render_template('007.html',idioma_encontrado = idioma_encontrado)
