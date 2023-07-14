# ColLab (Collaborative Laboratory)
ColLab is an application designed to boost collaborative research by creating a bulletin board style website where students and faculty can post ideas for projects, research, and articles that they are interested in collaborating on with others. It uses python to access the data for each post within a repository as well as allow users to create new posts that are added to the repository. Users can browse posts based on school, department, or key-word or they can use a search function to lookup specific ideas or topics. The application will provide the information in a user-friendly manner, likely a bulletin board style. Finally, users can create a simple profile with relevant information that allows establishing connections (friending or following).

## How to run the Flask App:
Follow these instructions to successfully run our app:

1. Navigate to the requirements.txt file and ensure you have the required programs and library's
- Make sure you have the programs in the stated version (different versions may have differences that do not allow the successful running of the application)
2. Navigate to your command prompt (CMD)
3. Navigate to your desired folder and clone the repository on your local system
- Type "cd\" press enter
- Type "cd file_path" press enter (Insert your desired filepath where it says file_path)
- Go to the Github Repository, Click on Code in the repository on the Github Website and copy the given Github URL
- Type "git clone https://github.com/Chasen-Jeffries/Collab_App.git"
4. Navigate to this new folder in your filepath
- Type "cd\" press enter
- Type "cd file_path" press enter. (Insert the file_path to Collab_App. This should end in "\Collab_App")
5. Setup the Flask Environment
- Type "Set Flask_App=App_Code" press enter
- Type "flask run" press enter
- Navigate your browser to "http://127.0.0.1:5000" in the URL bar
- Enjoy the Collab App! 

#### NOTE: This assumes you have already set up a virtual environment
If you have not already set up a virtual environment, follow these steps before step 3.

1. Navigate to your desired folder path.
- Type "cd\" press enter
- Type "cd file_path" press enter. (Insert your desired filepath where it says file_path)
2. Create a virtual environment using the venv module.
- Type "python -m venv .env". This creates a virtual environment where you can input the Flask App
3. Activate the virtual environment.
- Type ".env\Scripts\activate" (for Mac users, use the following "source .env/bin/activate")


### Project Requirements expressed as user stories:
- As a user, I want to be able to create and log in to my profile
  - I want to be able to write a brief biography about me and my research interests.
- As a user, I want to be able to post my research ideas that I would like to work on collaboratively.
  - I want to be able to post my research design
  - I want to be able to state the type of collaboration desired. (i.e. data wrangling, domain expertise, etc)
  - I want to be able to add keywords for my posts (to id the field, topic, etc)
- As a user, I want to be able to browse and search other collaborative research ideas that I align with my interests and skills.
  - Browse based on department, field, or keywords
  - Search based on topic, keyword, or field.
  - Look at my friends, peers, professors posts
- As a user, I want to be able to connect with and talk to potential collaborators.
  - I want to be able to friend or follow other users
- As a user, I want an easy-to-use interface that can be used with minimal experience.  

### Project Stakeholders:  
- Users: students, professors, and others interested in working collaboratively on research projects.
- Developers: Developers who will build the application.
- Database specialists: Database management skills will be required to help in storing and managing the posts created by users.
- Project Manager: Oversees the development process and coordinates between different components of the project.  
- UX/UI Designer: Design the interface to ensure an easy-to-use application that is user friendly for first time users.  

### Completion Times Estimates:
- Create an intuitive user-profile page: 1-2 weeks
- Create an easy-to-use mechanic that allows users to post: 1-2 weeks
- Implement a bulletin-board style browsing interface: 2 weeks
- Implement a search function for user posts: 1-2 week
- Implement a function to save or favorite posts: 1 week
- Testing and development: 2-3 weeks

#### Possible Additions:
- Idea Bank: A bank of additional ideas for projects, research, or problems that people haven’t seen address. Individuals can post ideas they had, but do not necessarily want to work to give others the opportunity to answer those questions or solve those problems.
- Collarative Environment: Build a simple web/app environment that promotes easy collaboration between individuals on projects. This may include text or video messaging services, Git style collaborative tools, etc.



## Part B
### Milestone 1.0 Project Requirements tasks and group member allocation:

#### Milestone 1.0 Features:
- Frontend site
- Backend database
- User profile
- Posting ideas
- Browsing page

#### Iteration 1:
1. As a user, I want to be able to create and log in to my profile. (2 weeks)
- Front end user interface for sign-up and login - Bayan + Chasen + Zelal (4 days)
- Back end API for login - Bayan + Chasen + Zelal (5 days)
- Storing and access in login API - Bayan + Chasen + Zelal (5 days)

2. As a user, I want to be able to post my ideas for research that I would like to work on collaboratively. (3 Weeks)
- Front end user interface for posting - Manny + Navya (5 days)
- Editing and deleting posts - Manny + Navya (5 days)
- Back end API for posts - Manny + Navya (6 days)
- Storing and access posts on profile pages - Manny + Navya (5 days)

#### Iteration 2:
3. As a user, I want to be able to browse other research ideas that I align with my interests and skills.
- Front end user interface for browsing posts, bulletin-board style (*Name*)
- Back end API for browsing posts (*Name*)
- Accessing posts on browse page (*Name*)


### Milestone 2.0 Project Requirements tasks and group member allocation

#### Milestone 2.0 Features:
- User connection
- Search page
- Search results page

### Project Requirements tasks and group member allocation:
1. As a user, I want to be able to connect with potential collaborators.
- Front end user interface for adding friends & viewing friendslist (*Name*)
- Back end API for friending & friend list (*Name*)
- Accessing profiles for friending (*Name*)

2. As a user, I want to be able to search other research ideas based on a topic, keyword, username, or field.
- Front end user interface for searching page and results page (*Name*)
- Back end API for searching posts and results page (*Name*)
- Accessing posts on search results page (*Name*)


## How to run the BurnDown Chart
To run the BurnDown_Chart2.py script (first insure that Python3 is loaded. download from the official Pythion website). The following libraries, using pip, will need to be installed: Pandas along with matplotlib. Run the following in your terminal/shell:
- pip install pandas
- pip install matplotlib
Once Python and the necessary libraries are installed, the script can be run.

#### Output
The output will be a plot representing the burn down chart. The x-axis is the number of days, and the y-axis is the remaining story points. The chart includes the actual story points line (in blue, if using the default settings). The blue ideal line represents the theoretical progress if the team burns down story points at a constant rate.

Once progress is made, the chart can be updated with the actual time spent on each story point and actual progress can be tracked to the ideal progress to track the teams estimated completion time and to ascertain if incremental effiort is required to complete timely or if respurces may need to be realigned.

### STEPS INVOLVED IN CREATING AND MAINTAINING A BURNDOWN CHART:
A burn down chart, in software development, is a graphical representation of work left to do versus time. It's often used in agile project management, particularly in Scrum, to track the progress of a sprint or a project.

#### Steps to create a burn down chart:
1. Define the Sprint Backlog: Determine what work needs to be done during a sprint. This includes estimating the number of story points (or hours) each task will take.
2. Create the Chart: Draw a graph where the x-axis represents time (in days of the sprint) and the y-axis represents the total amount of work left at the start of the sprint (in story points or hours). We used Python for this taskm but can use other tools or can be drawn out manually.
3. Plot the Ideal Burn Down Line: Draw a line from the top left corner (start of the sprint, total work) to the bottom right corner (end of the sprint, no work left). This line represents the ideal progress of the sprint.
4. Track the Actual Progress: Each day of the sprint, calculate the remaining work and plot it on the chart. This creates the actual burn down line, which starts at the same point as the ideal line but might zig-zag up and down, depending on the team's progress.
5. Update Daily: The chart is updated at the end of each day as work is completed. Any changes in scope or work are also reflected on the chart.

The burn down chart is an effective tool for visualizing the progress of the sprint. It allows the team and stakeholders to quickly see if they're on track to complete all the work by the end of the sprint.
                                                                                                                                                                    
