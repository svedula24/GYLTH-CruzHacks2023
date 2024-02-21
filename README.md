## 1st Place - CruzHacks

## Inspiration
Our inspiration for tackling the issue of deforestation stems from a deep concern for the environment and a desire to make a positive impact. We saw a need for a tool that could bring the impact of deforestation to life, and make it tangible for people everywhere. The problem of deforestation is a global issue and affects everyone, and we believe that it is important for people to understand its consequences and take action to address it. That's why we decided to build a data visualization tool that would allow users to see the impact of deforestation in their own communities. This was designed to be an immersive and educational experience, one that would inspire people to understand the issue. We believe that this project has the potential to make a real difference in the fight against deforestation. By raising awareness and inspiring people to take action, we hope to contribute to a more sustainable future for our planet.

##Project Overview
We built a data visualization tool that shows deforestation at a current location inputted by the user based on data from 2007-2017, due to the current live satellite feed being inaccessible to analyze. Users are next prompted to take part in a simulation that shows them both what the location was like a decade ago and the present day which represents how deforestation will affect us in the future if we don't take any action.

## How It Works
**1. Users enter location coordinates through our web page, which are then utilized by the Google Earth Engine API. The API gathers data using the given parameters in order to plot the information on a Folium layer and utilizes Selenium to save the images. The saved images are analyzed using OpenCV to detect deforestation by examining the color and location of pixels. Finally, the program returns detailed images displaying the deforestation that has occurred in the specified area over the past decade.**

![Deforestation Detection Image](https://gateway.estuary.tech/gw/ipfs/bafkreicfdr5xod7toa4wwx5wyiuev6vzyed7c5v4fkzsw427sh2oeb7ofu)

**2. We utilized Unity3D and Niantic Lightship VPS Waypoint assets to model a scaled representation of Stevenson College at UCSC. This 3D interactive environment allows users to visualize and experience the potential consequences of deforestation in a vivid and educational manner.**

![UCSC Simulation Image](https://gateway.estuary.tech/gw/ipfs/bafkreia2zsbxrqkcvwo2g6zea2gjouppclvjcbzc2alfa6pyf3yxtwuzqu)

![Deforestation Simulation Image](https://gateway.estuary.tech/gw/ipfs/bafkreigfjfrsb3v4ymkp3o44scg7dhrkcahmugwes7bmje2t7t5vi6khxy)

**3. Users receive notifications with updates and resources obtained based on their selections. Images and files are uploaded to Estuary, which uses an Interplanetary File System(IPFS) allowing us to upload files to Filecoin and retrieve them. Doing this is beneficial as all images are open-sourced meaning users can audit that the information is raw and not edited or manipulated.**

![Twilio Image](https://gateway.estuary.tech/gw/ipfs/bafkreifpolkjzfc7g7vdd6pipnqsmpkkeulr4nnol6u7uufk7mvy7w5mpi)

## How we built it
![System Architecture](https://gateway.estuary.tech/gw/ipfs/bafkreibnptrlvnpasaybs4cx2nsj5kkqcyyqcqsj32ypvswb72hagwc2ti)



## Challenges we ran into
1. Discrepancies between the versions of our dependencies 
2. Integrating our front end with our back end--running our project on a server 
3. Loading different environments in our AR/VR simulation

## Accomplishments that we're proud of
We are proud that we were able to execute our project idea and build out a viable solution to raising awareness and combating a pressing issue.

## What we learned
1. Flask
2. Lightship
3. Folium 
4. Selenium
5. Google Earth Engine

## What's next for GLYTH
We plan on cleaning up the current components of our project and adding some more functionality. To better utilize Lightship VPS we plan to add our own locations for testing. We tried experimenting with creating our own, but given the timeframe of the hackathon, it made sense to leave this for future improvements. We also plan to create a more dynamic front end that can better integrate with other components of our project: more form data, using users' location, getting feedback from the user, improving the leaderboard, etc.!



https://user-images.githubusercontent.com/74890320/216852153-de046bfa-3f8b-4337-ba03-1bb2a67ab4f6.mov


