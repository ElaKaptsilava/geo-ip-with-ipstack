<img src="https://media.giphy.com/media/M9gbBd9nbDrOTu1Mqx/giphy.gif" width="100"/>

# Content of project
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
<details>
<summary>Click here to see general information about <b>Project</b>!</summary>
<b>Geolocation API with ipstac</b>. This is a Django REST framework project that uses the ipstack API to provide geolocation information for any IP address interacting with external API from https://ipstack.com/.
The project demonstrates how to integrate the ipstack API with Django REST framework, and how to use serializers, viewsets, permissions, and other features of the framework.
- A web app that allows users to enter an IP address and see the corresponding location data on a map, as well as other details such as country, city, currency, time zone, etc.
- A REST API that exposes the same functionality as the web app, but returns the data in JSON</p>
</details>

## Technologies
<ul>
<li>Django</li>
<li>Django REST Framework</li>
<li>Docker & Docker-compose</li>
<li>REST API</li>
</ul>

## Setup
<ul>
  <li><h4>Clone the reposotory</h4></li>
  <pre><code>$ git clone https://github.com/ElaKaptsilava/geo-ip-with-ipstack.git</code></pre>
  <li><h4>Running the application</h4></li>
  <pre><code>$ docker-compose build</code></pre>
  <pre><code>$ docker-compose up</code></pre>
  <li><h4>Create super user</h4></li>
  <pre><code>$ python manage.py createsuperuser</code></pre>
</ul>
