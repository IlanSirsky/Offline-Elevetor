import sys
import pygame
import Ex1
from LinkedList import *
from Building import *
from Call import *

if __name__ == "__main__":

    args = sys.argv[1:]
    path_json = args[0]
    path_csv_input = args[1]
    callData:[Call] = Ex1.ReadCSV(path_csv_input)
    ourBuilding:Building = Ex1.ReadJson(path_json)
    ourBuilding.elevators.sort()

    callCounter = 0

    # activate the pygame library .
    # initiate pygame and give permission
    # to use pygame's functionality.
    pygame.init()

    size = 800

    # create the display surface object
    # of specific dimension..e(500, 500).
    win = pygame.display.set_mode((size, size))

    # set the pygame window name
    pygame.display.set_caption("Offline Elevator")

    pygame.font.init() # you have to call this at the start,
                       # if you want to use this module.
    myfont = pygame.font.SysFont('Comic Sans MS', 30)

    minFloor = ourBuilding._minFloor
    maxFloor = ourBuilding._maxFloor

    elevators = len(ourBuilding.elevators)

    space = 50

    # object current co-ordinates
    x = 120
    y = 0 + space

    spacesSize = int(((size - space) / (maxFloor - minFloor)))  # size between floors
    print(spacesSize)

    # velocity / speed of movement
    vel = int(spacesSize / 10)  # 1 sec

    elevatorsPos = []
    floorsPos = {}

    elevatorsList = []
    elevatorsSpeed = []
    elevatorsMode = []

    # dimensions of the object
    width = int((size-x)/elevators)
    height = int((size-space)/(maxFloor-minFloor+1))

    counter = maxFloor
    for i in range(space, size, height):
        floorsPos[counter] = i
        counter -= 1

    for i in range(elevators):
        elevatorsPos.append(floorsPos[0])
        elevatorsList.append(LinkedList())
        elevatorsSpeed.append(vel * ourBuilding.elevators[i]._speed)
        elevatorsMode.append(0)

    # Indicates pygame is running
    run = True

    mode = -1

    timer = 0.0

    # infinite loop
    while run:

        for calls in callData[callCounter:]:
            time, src, dst = calls.GetData()
            if timer>=time:
                elev = calls.GetElevator()

                state = calls.GetState()
                if elevatorsList[elev].head is None:
                    elevatorsList[elev].addlast(dst)
                    elevatorsList[elev].add(src)
                elif state == Call.UP:
                    if elevatorsList[elev].getLast() > dst:
                        a = Node(dst)
                        a.next = elevatorsList[elev].tail
                        a.prev = elevatorsList[elev].tail.prev
                        elevatorsList[elev].tail.prev = a
                        a.prev.next = a
                    else:
                        elevatorsList[elev].addlast(dst)

                    a = elevatorsList[elev].head
                    while src > a.val:
                        a = a.next

                    if a == elevatorsList[elev].head:
                        elevatorsList[elev].add(src)
                    else:
                        b = Node(src)
                        b.next = a
                        b.prev = a.prev
                        a.prev = b
                        b.prev.next = b
                elif state == Call.DOWN:
                    if elevatorsList[elev].getLast() < dst:
                        a = Node(dst)
                        a.next = elevatorsList[elev].tail
                        a.prev = elevatorsList[elev].tail.prev
                        elevatorsList[elev].tail.prev = a
                        a.prev.next = a
                    else:
                        elevatorsList[elev].addlast(dst)

                    a = elevatorsList[elev].head
                    while src < a.val:
                        a = a.next

                    if a == elevatorsList[elev].head:
                        elevatorsList[elev].add(src)
                    else:
                        b = Node(src)
                        b.next = a
                        b.prev = a.prev
                        a.prev = b
                        b.prev.next = b
                callCounter+=1
            else:
                break

        # creates time delay of 100ms
        pygame.time.delay(100)
        timer+=0.1

        if(timer > 1000):
            run = False

        # iterate over the list of Event objects
        # that was returned by pygame.event.get() method.
        for event in pygame.event.get():

            # if event object type is QUIT
            # then quitting the pygame
            # and program both.
            if event.type == pygame.QUIT:
                # it will make exit the while loop
                run = False
        # stores keys pressed

        for i in range(elevators):
            if elevatorsList[i].head is None:
                elevatorsMode[i] = 0
            else:
                if elevatorsPos[i] > floorsPos[elevatorsList[i].getFirst()]:
                    elevatorsMode[i] = 1
                else:
                    elevatorsMode[i] = -1

                if elevatorsPos[i] - floorsPos[elevatorsList[i].getFirst()] == 0:
                    pygame.time.delay(250)
                    elevatorsList[i].delete()

        for i in range(elevators):
            if elevatorsList[i].head is None:
                elevatorsMode[i] = 0

            if elevatorsMode[i] == 1 and elevatorsPos[0] > space and elevatorsPos[i] >= floorsPos[elevatorsList[i].getFirst()]:
                # decrement in y co-ordinate
                if elevatorsPos[i] - elevatorsSpeed[i] < floorsPos[elevatorsList[i].getFirst()]:
                    elevatorsPos[i] = floorsPos[elevatorsList[i].getFirst()]
                else:
                    elevatorsPos[i]-=elevatorsSpeed[i]

            # if down arrow key is pressed
            if elevatorsMode[i] == -1 and elevatorsPos[0] < size - height and elevatorsPos[i] <= floorsPos[elevatorsList[i].getFirst()]:
                # increment in y co-ordinate
                if elevatorsPos[i] - elevatorsSpeed[i] > floorsPos[elevatorsList[i].getFirst()]:
                    elevatorsPos[i] = floorsPos[elevatorsList[i].getFirst()]
                else:
                    elevatorsPos[i]+=elevatorsSpeed[i]

        # completely fill the surface object
        # with black colour
        win.fill((0, 0, 0))

        header = myfont.render("Offline Elevator       Time: {:.1f}".format(timer), False, (255, 255, 255))
        win.blit(header, (0,0))

        # drawing object on screen which is rectangle here
        # draw elevators and vertical lines
        for i in range(elevators):
            pygame.draw.rect(win, (255, 0, 0), (x+i*width, int(elevatorsPos[i]), width, height))

            pygame.draw.line(win, (255, 255, 255), (x+i*width, space), (x+i*width, size))

        # draw horizontal line
        for i in range(space, size, height):
            pygame.draw.line(win, (255, 255, 255), (0, i), (size, i))

        for i in range(minFloor,maxFloor+1):
            textsurface = myfont.render(str(maxFloor+minFloor - i), False, (255, 255, 255))
            win.blit(textsurface, (int(x/2), (i-minFloor) * int(((size-space)/(maxFloor-minFloor+1))) + space))

        # it refreshes the window
        pygame.display.update()

    # closes the pygame window
    pygame.quit()