# Udacity - Full Stack - Project 1 - Trailer Site

## Quick Description

This is a class project for Udacity's Full Stack Nanodegree class.  Technically, this was an excercise in Python 2.7 using basic inheritance, gaining familiarity with using modules, and requesting third-party APIs.  Functionally, this is a collection of scripts that create an HTML page to showcase movies.

## Outline

*entertainment_center.py*

Here is where you want to instantiate movies based off your own provided IMDB ID's and Youtube URL's.

*media.py*

This file holds the classes that construct your movie instances, based on the provided IMDB ID's, it will request movie data from the Open Movie Database (omdbapi.com).  You shouldn't need to touch this, but may want to read it to see what data can be accessed from the movie instance.

*fresh_tomatoes.py*

Slightly modified class template that is used to generate the HTML file.

*fresh_tomatoes.html*

Every time entertainment_center.py is run, it will create (and over-write) a HTML page with this name and open it in the system's default browser. This file is an example based off what is currently in entertainment_center.py.

## How to Run

Note:  This uses the [Requests module](http://docs.python-requests.org/en/master/), in the terminal you may need to ```pip install requests```

To run simply run in IDLE or in the terminal run:

```python entertainment_center.py```
