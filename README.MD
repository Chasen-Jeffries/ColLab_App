To run the BurnDown_Chart2.py script (first insure that Python3 is loaded. download from the official Pythion website). The following libraries, using pip, will need to be installed: Pandas along with matplotlib. Run the following in your terminal/shell:
  pip install pandas
  pip install matplotlib
Once Pythoin and the necessary libraries are installed, the script can be run.

The output will be a plot representing the burn down chart. The x-axis is the number of days, and the y-axis is the remaining story points. The chart includes the actual story points line (in blue, if using the default settings). The blue ideal line represents the theoretical progress if the team burns down story points at a constant rate.

Once progress is made, the chart can be updated with the actual time spent on each story point and actual progress can be tracked to the ideal progress to track the teams estimated completion time and to ascertain if incremental effiort is required to complete timely or if respurces may need to be realigned.

STEPS INVOLVED IN CREATING AND MAINTAINING A BURNDOWN CHART:
A burn down chart, in software development, is a graphical representation of work left to do versus time. It's often used in agile project management, particularly in Scrum, to track the progress of a sprint or a project.

Here are the steps to create a burn down chart:

1. Define the Sprint Backlog: Determine what work needs to be done during a sprint. This includes estimating the number of story points (or hours) each task will take.

2. Create the Chart: Draw a graph where the x-axis represents time (in days of the sprint) and the y-axis represents the total amount of work left at the start of the sprint (in story points or hours). We used Python for this taskm but can use other tools or can be drawn out manually.

3. Plot the Ideal Burn Down Line: Draw a line from the top left corner (start of the sprint, total work) to the bottom right corner (end of the sprint, no work left). This line represents the ideal progress of the sprint.

4. Track the Actual Progress: Each day of the sprint, calculate the remaining work and plot it on the chart. This creates the actual burn down line, which starts at the same point as the ideal line but might zig-zag up and down, depending on the team's progress.

5. Update Daily: The chart is updated at the end of each day as work is completed. Any changes in scope or work are also reflected on the chart.

The burn down chart is an effective tool for visualizing the progress of the sprint. It allows the team and stakeholders to quickly see if they're on track to complete all the work by the end of the sprint.
                                                                                                                                                                    
