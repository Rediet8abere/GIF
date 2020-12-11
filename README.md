# Welcome to Gif Search!

This Gif Search is made using python flask web framework.

The homepage shows you top ten trending gifs. There is also a search button where users
can type in words and get top 10 gifs based on the query.

You can also click on the random button to display 10 random gifs based on your search term.



#### CapRover Deployment
[Cap Gify!](https://gify-flask.dev.sendedoswags.me/)

## Docker Set Up
### Build
##### docker build -t gify-flask-app .

### RUN
##### docker run -d -p 5000:5000 gify-flask-app

### Check Created Image
#####  docker image ls

### Remove Image
#####  docker rmi [image_name]

### To Check what Container is Running
#####  docker ps -a

## Gif Project Badges
![Website](https://img.shields.io/website?down_color=lightgrey&down_message=offline&style=flat-square&up_color=blue&up_message=online&url=https%3A%2F%2Fstatuspage.freshping.io%2F49299-Gify)
