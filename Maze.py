from Actor import * 
from pyamaze import maze,COLOR
from collections import deque
import sys
oo=sys.maxsize
UNVISITED=oo
VISITED=1
FIRE=-oo

class Maze:

    def __init__(self,width,height,GoalState=None,ActorState=None,FireState=None):
        self.theMaze=maze(width,height)
        self.Agent=Actor(self.theMaze,ActorState)
        self.Fire=Actor(self.theMaze,(0,width),color=COLOR.red)
        self.Grid=[[UNVISITED]*width]*height
        self.Functions={}
        self.Goal=GoalState
        self.FireQueue=deque()
        self.ActorQueue=deque()

    def  InitialiseActor(self,state):
        if(not bool(self.ActorQueue)): # Check if empty. If not empty, means initialised before
            print("Error: ActorQueue already initialised :)")
            exit()
        self.Actor.theGUI.position=state
        self.ActorQueue.append(state)

    def  InitialiseFire(self,state):
        if(not bool(self.FireQueue)): # Check if empty. If not empty, means initialised before
            print("Error: FireQueue already initialised :)")
            exit()
        self.Fire.theGUI.position=state
        self.FireQueue.append(state)

    def SetGoal(self,state):self.Goal=state

    def FireSpread(self):
        size=len(self.FireQueue)
        for i in range(size):
            self.Fire.NowState(self.FireQueue[0])
            self.Fire.draw()
            self.Grid[self.Fire.State]=FIRE
            self.FireQueue.popleft()
            self.FireQueue.extend(self.Fire.Actions())

    def SearchFunction(self,Key,Cost=None):
        if(Key not in self.Functions.keys):
            print("ERROR: No function with name '"+Key+"' :)")
        self.Functions[Key](Cost)

    def LessGo(self):
        if(not self.Goal or not self.Agent.State or not self.Fire.State):
            print("ERROR: Set all your States first :)")
            exit()
        self.theMaze.CreateMaze(loopPercent=100)
        self.Actor.theGUI.footprints=True
        self.Fire.theGUI.footprints=True



#--------------------------------------------------------------------------
# Enter your Search Algorithms here

    def UCS(self,Cost=None):
        if(not Cost):
            print("ERROR: Chose UCS Search with no Cost Inserted :)")
            exit()
        


        



        