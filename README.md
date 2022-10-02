#  RVR Lab project built with Django and ChartJS
“RVR rover lab” project is developed with the motto of “It doesn’t matter where you look from. It’s all about the rovers for the exalted vision.”. As can be seen from the project logo, the reverse of “RVR” is also “RVR” which characterizes the word “rover”. However, in our motto, the first sentence depicts that our project is for people of all age groups regardless their cultural, ethnic, and educational background. Besides, the motto shows that the focus of the project is the rovers which play the main role for the exalted vision of spreading scientific resources all over the world.

In this demo version, Monitoring part of the project is built. Each second the sensor data is sent to the server (in this case, just random values) and the corresponding labels and graphs are updated in real time with the help of `django-channels`. It is the django-implemented version of WebSockets to provide  in-time interaction between client2client and server2server without the need of refresh.

### General Project Description (Beyond Demo)
RVR rover lab” contains 2 main parts called rover lab and software. In the rover laboratory, the simulated environments of Moon and Mars will be constructed, with the facilities containing the surface models of the mentioned satellite and the planet as well as real rover models for exploring these surfaces. The reason why we chose these space objects is their significance in the space exploration strategy of NASA and other partner space agencies. We have a strong believe that this project will inspire young people who can definitely be a member of “Artemis Generation”. When it comes to the software, the website will provide the connection between users and the rover laboratory, as a result of which the real rover models will be controlled by users. The real-time video from several cameras supplied on the rovers as well as data by different sensors of such as temperature, pressure, and etc. will be sent to the users through the website. By controlling the rovers, users will try to complete scientific tasks in the simulated environment within the time limitation. During the session, after completing each task the information about the appropriate missions in the history of space exploration will be given with the usage of media types such as music, infographics, artwork, videos, and the links to scientific media resources. 

# Technologies used
- Django
- DRF
- ChartJS
- Docker
- PostgreSQL

# Setup
First things first, install the dependencies:

`pip install -r requirements.txt`

Next step is to build and create the containers for a service.

`docker compose up --build -d`

Once the build is done, run the project as follows:

`python manage.py runserver`

That is it! Have fun!

