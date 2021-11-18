# Offline Elevator Algrorithm
**Created by Eldad Tsemach and Ilan Sirisky**
 
This project consists of our algorithm for controlling the path of an elevator according to supplied parameters including source and destintation locations, call state and time of call, as well as Buildings that contain number of elevator.

## Goals
This algorithm and its implementation here were designed with simplicity and efficiency in mind.
The primary goal is to maximize elevator efficiency, which is achieved by minimizing the number of floors traveled during the lifetime of the elevator's journey.

## Algorithm
##### Idea: allocating the best elevator to each call by sorting the elevators'  time to finish for each call. As well as allocating new calls to each elevator by checking future calls that are happening in the time frame that the elevator is still moving towards other destinations.
- Firstly the algorithm reads the json and csv files, creating objects of them as buildings, elevators and calls.
- For each call:
    - If this call already has an elevator allocated to it then continue.
    - Check all of the elevators and calculate the time until they end their current mission + time to reach the next call source floor + source to it's next destination.
	- Sort all of the elevators by the time value we got.
	- Allocate the elevator at position 0 to the call - the elevator with the minimum time to finish the call.
	- For each call after the main call that is in the time frame of the elevator to finish all his tasks:
	   - If the state of the call is not as the main call, continue.
	   - Check if the elevator can reach the source of the call and pick it up on it's way to his destination. Check if the source floor is above or under the main call. For example: if the state of the call is *up* check if source floor is above the main call.
		    - Calculate time of the elevator to finish his current mission + the time elevator moves from his current position to the source floor of the main call + the time to reach the source floor of the new call from the source floor of the main call.
		    - Check if the time we calculated is after the time the new call is being made.
			    - Then allocate that call the same elevator as the same elevator we chose for the main call.

### Code Description
- `Building.p`, `Elevator.py` and `Call.py` : These contain the casing for the whole project with variables that are being read from the Building.json files and Calls.csv files.
- `ElevatorExecuter.py`: Contains the implementaion of our algrorithm described above.
- `LinkedList.py` and `gui.py`: These files include the lines of code for the GUI that shows how the elevators move at real time for each call being made from the Calls.csv files.

## Input/Output Examples
#### Example for Building.json input:

![](https://i.imgur.com/FgpYnIs.png)

#### Example for Calls.cvs input:

![](https://i.imgur.com/yfoKUzL.png)
- Colum B: time stamp for each call.
- Colum C: source floor.
- Colum D: destination floor.
- Colum F: elevator index allocation.

#### Output csv file:

![](https://i.imgur.com/JRWBcNW.png)

#### Output log:

![](https://i.imgur.com/qof9jsX.png)

# How to Run
We got 3 sections:
- Section 1 - Run the algorithm to allocate the best elevators.
- Section 2 - Run the simulator to see the results from the algorithm.
- Section 3 - Run the GUI to see how the elevators graphicly move.

Before each section download the files and extract them to a folder of your choice
###### Section 1:
1. Open cmd in your folder - you can do it by click on the folder path on the top window and type cmd.
2. Type `Ex1.py <json building path> <csv calls path> <csv output path>`.
Example: `Ex1.py .\data\Ex1_input\Ex1_Buildings\B5.json .\data\Ex1_input\Ex1_Calls\Calls_a.csv out.csv`.
3. You can see the <csv output> file has been created and changed column F in the excel. (Elevator column).

###### Section 2:
1. Open intellij.
2. Create a new java project.
3. In your elevator folder go to `.\data\Test_In_Java\`
4. Drag all of the folders into your project.
5. In your intellij go to the `.\libs` folder and right click on `Ex1_checker_V1.2_obf.jar`, and click on add to library.
6. go to .\src and open Ex1_tester.java
7. Change args as you want - args[0] - (not importent its you ID) , args[1] - enter the path to the building you chose in section 1, args[2] enter the path to the output (csv file) you got in section 1.
***Important:*** You need to drag the output (csv file) and building (json file) into your project inorder to use it in your project.
8. Run the Ex1_tester.java and see the results.

###### Section 3:
1. Open cmd in your elevator folder - you can do it by click on the folder path on the top window and type cmd.
2. Type `gui.py <json building path> <csv output path>`.

## GUI
Link for a preview of the GUI : https://youtu.be/enZNmPQF7yY.

## UML
![](https://i.imgur.com/8Rz6jW1.png)

## Literature Research
- [Elevator Scheduling](http://www.columbia.edu/~cs2035/courses/ieor4405.S13/p14.pdf)
- [Elevator Optimization Problem](https://towardsdatascience.com/elevator-optimization-in-python-73cab894ad30)
- [The Hidden Science of Elevators](https://www.popularmechanics.com/technology/infrastructure/a20986/the-hidden-science-of-elevators/)

Link to the main assignment: https://github.com/benmoshe/OOP_2021/tree/main/Assignments/Ex1.
