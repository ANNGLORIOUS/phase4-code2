# SA. Week 2 Code Challenge: LATESHOW

#### By **{List of contributors}**
This project was created and is sole property of Annglorious mueni.

## Project Overview
Welcome to the Late Show API! This application allows you to manage episodes, guests, and their appearances on a late-night show. It provides RESTful endpoints for retrieving and adding data related to the show's episodes and guests.

### Features
1. Retrieve all episodes and guests.
2. Fetch details of a specific episode, including its guest appearances.
3. Add new appearances for guests in episodes.
4. Data persistence with SQLite.

### API Endpoints
1. Homepage
* GET /
Returns a welcome message.

2. Episodes
* GET /episodes
Retrieve all episodes.

* GET /episodes/<int:id>
Retrieve a specific episode by its ID.

3. Guests
* GET /guests
Retrieve all guests.

4. Appearances
* POST /appearances
- Add a new appearance. Requires JSON payload with:
    - rating: Integer (1-5)
    - episode_id: Integer (ID of the episode)
    - guest_id: Integer (ID of the guest)



## Setup/Installation Requirements
* One would need either linux or wsl for window users
* A copy of visual basic code installed
* A github account

1. Open your terminal and go to the directory you wish to work from.
2. Go to the following url using ur github account https://github.com/ANNGLORIOUS/phase4-code2
3. Go to the code tab and clone the ssh key
4. Go back to the terminal and type git clone <-followed by the ssh key you copied /cloned ->
5. Enter your new cloned repository and type in code .
6. On the visual studio code that has now opened, go to the the run tab.
7. Install the requied packages and set up the required database:

      #### Steps to follow:
      1. Create a virtual environment by, pipenv install && pipenv shell.
      2. Initialize the database - flask db init
                                    -flask db migrate -m "Initial migration."
                                    -flask db upgrade
      5. Usage - To run the application, execute the following command:
                                            -python app.py  
      4. Seed the database, python seed.py.  


## Technologies Used
This program is built purely with python, flask, flask-sqlalchemy,flask-migrate and sqlite(for development) using the visual code environment.

## Support and contact details
For any issues please email me at annglorious.mueni@student.moringaschool.com
### License
Apache License 2.0


