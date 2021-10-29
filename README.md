# FlaskAndCraw
A simple Flask BackEndServer for me to Prictice Python And Flask  
Also a server For my Other Prictice

# 1.How to Use 
### Make sure you have a python environment , if you don't Check out this [Python Install](https://www.python.org/) 
  `pip3 install -r requirements.txt` install necessary package to run this project  
  `python main.py` start up server   (use CTRL+C to stop)
  
# 2.What package's do we use and for what?
* ## Flask  
  because we need a server To get information from other Web  
  And return the data we need to frontEnd
* ## Flask-Cors
  due to The #[CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) , So even we just want a localhost server  
  still need this to Prevnt not Allow from this origin issue  
* ## requests
  We need  some information from internet , But not all data have api to get .
  Sometimes we need to Craw a Webpage and extract some information . So we need this to get HtmlDoc use this package.
* ## Python
  A good Chioce to Craw Information we need . That's why we choose Flask for our server.
