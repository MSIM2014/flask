# flask
I am following the Flask tutorial to write a variety of web applications in Python using the Flask framework. The url of the flask tutorial is http://flask.pocoo.org/docs/0.12/tutorial/. 

This web application is named Flaskar. It does the following things:
1. Let user sign in and sign out with credentials specified in the configuration. Only one user is supported.

2. When the user is logged in, they can add new entries to the page consisting of a text only address and a text only zipcode. The address and zipcode are not sanitized as we trust the users here. The home description at the entered address and zipcode are retrieved from Zillow API and are stored in the database with the address and zipcode.

3. The index page shows the address, zipcode and retrieved home description entered so far in reverse chronological order (newest on top) and the the user can add new ones from there if logged in. 
