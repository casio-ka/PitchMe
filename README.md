# PitchMe
A web app where users will submit their one minute pitches and other users will vote on them and leave comments to give their feedback on them

## Description
[PitchMe](https://wpitchme.herokuapp.com/) is a web application that allows users to submit a pitch, and other users are allowed to vote on submitted pitches and leave comments to give their feedback on the pitches. 
For a user to submit a pitch, vote on a pitch or give feedback on a pitch they need to have an account. <br>

The pitches are organized by categories. Examples of categories: <br> 
- pickup lines
- interview pitches
- product pitches
- promotion pitches

## User Stories
A user can:
* view the different categories
* see the pitches other people have posted
* submit a pitch in any category
* comment on the different pitches and leave feedback
* vote on the pitch and give it a downvote or upvote

## Specifications
| Behavior        | Input           | Outcome  |
| ------------- |:-------------:| -----:|
| Register to be a user | Your email : mwangi@me.com <br> Username : 'your username' <br> Password : 'your password | New user is registered |
| Log in | Your email : 'your email' <br> Password : 'your password' | Logged in |
| See pitches from selected category | **Click** a category | Directed to a page with a list of pitches from the selected category |
| Create a pitch | **Click Create A Pitch** | An authenticated user is directed to a page with a form where the user can create and submit a pitch |
| See a pitch | **Click** on a pitch | A user is directed to a page containing the pitch, its comments and its votes |
| Comment on a pitch | **Click Comment** | An authenticated user is directed to a page with a form where the user can create and submit a comment on a pitch |
| Like on a pitch | **Click** on upward arrow | The vote on the pitch increases by one |
| Dislike on a pitch | **Click** on downward arrow | The votes on the pitch decreases by one |

## Setup/Installation Requirements

* Click [PitchMe](https://wpitchme.herokuapp.com/) <br/>


## Known Bugs


## Technologies Used
- Python3.8
- Flask
- Bootstrap4
- Postgres Database
- CSS
- HTML

### License

MIT (c) 2020 **[WainainaK](https://github.com/casio-ka)**