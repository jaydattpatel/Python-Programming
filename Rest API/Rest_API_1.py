'''
author : Jaydatt Patel 

REST stands for REpresentational State Transfer.

A URL is used by a browser or other program to specify what server to connect to and what page to ask for. Like other things that will be interpreted by computer programs, URLs have a very specific formal structure. If you put a colon in the wrong place, the URL won not work correctly. The overall structure of a URL is:

<scheme>://<host>:<port>/<path>?key=val&key&val

Step 1: the client makes a request to the server.
If the request only involves fetching data, the client sends a message of the form GET <path>, where <path> is the path part of the URL
If the request involves sending some data (e.g., a file upload, or some authentication information), the message starts with POST
In either case, the client sends some HTTP headers. These include:
    - The type of client program. This allows the server to send back different things to small mobile devices than desktop browsers (a “responsive” website)
    - Any cookies that the server previously asked the client to hold onto. This allows the server to continue previous interactions, rather than treating every request as stand-alone. It also allows ad networks to place personalized ads.

After the HTTP headers, for a POST type communication, there is some data (the body of the request).

Step 2: the server responds to the client.
The server first sends back some HTTP headers. These include:
    - a response code indicating whether the server thinks it has fulfilled the request or not.
    - a description of the type of content it is sending back (e.g., text/html when it is sending html-formatted text).
    - any cookies it would like the client to hold onto and send back the next time it communicates with the server.
After the headers come the contents. This is the stuff that you would see if you ask to “View Source” in a browser.

In this format, the URL has a standard structure:
    - the base URL
    - a ? character
    - one or more key-value pairs, formatted as key=value pairs and separated by the & character.

For example, consider the URL https://itunes.apple.com/search?term=Ann+Arbor&entity=podcast.

'''

import requests
import json

page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
print("type(page) : ",type(page))
print("page.text[:150] : ",page.text[:150]) # print the first 150 characters
print("page.url : ", page.url) # print the url that was fetched
print("------")
x = page.json() # turn page.text into a python object
print("type(x) : ",type(x))
print("---first item in the list---")
print(x[0])
print("---the whole list, pretty printed---")
print(json.dumps(x, indent=4)) # pretty print the results
