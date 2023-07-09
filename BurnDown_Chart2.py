
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np  # for np.linspace()

# Define your story points and estimated effort for each
story_points_dict = {
    'Create & Log-In to Profile': 14,
    'Post a Research Design': 14,
    'Describe the Desired Collaboration': 14,
    'Add Key Words for Search of Posts': 10,
    'Ability to Search Research Designs based upon Interests and Skills': 10,
    'Browse Posts based on CGU Departments, Fields. Topics, Key Words': 10,
    'Ability to Connect with and Discuss Research Interests with Potential Collaborators and follow Users': 10,
    'Easy-To-Use Interface that can be Used with minimal experience': 20
}

# Print the Dictionary
print(story_points_dict)

# Assume each task takes 12 days to complete
task_days = 12

# Sprint lasts as many days as there are tasks multiplied by the number of days each task takes
days = list(range(1, len(story_points_dict)*task_days + 1))

# Ideal story points will decrease uniformly over the course of the sprint
# We use np.linspace to create a list of linearly spaced values from the total story points to 0, with length equal to len(days)
ideal_story_points = list(np.linspace(sum(story_points_dict.values()), 0, len(days)))

df = pd.DataFrame({'Day': days, 'Ideal Story Points': ideal_story_points})

plt.figure(figsize=(10, 6))
plt.plot(df['Day'], df['Ideal Story Points'], linestyle='--', label='Ideal')
plt.xlabel('Day')
plt.ylabel('Story Points')
plt.title('Burn Down Chart')
plt.legend()
plt.grid(True)
plt.show()
