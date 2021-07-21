# makarov process
from numpy.random import choice
class mp:
    def __init__(self) -> None:
        self.nodes=[]
    def addNode(self, name, transition, isStart, isEnd):
        # Transition goes like ["balh":0.2, "Bah":0.3]
        self.nodes.append({"name":name, "to":transition, "start":isStart, "end":isEnd})
    def isThereNode(self, node):
        this=False
        for i in self.nodes:
            if i["name"]==node:
                this=True
        return this
    def getNode(self, node):
        for i in self.nodes:
            if i["name"]==node:
                return i
    def runNode(self, node: dict, limit, k):
        if node["end"]==True:
            print(f"{k}:It reaches end! I am {node.get('name')}")
            return
        if k>=limit:
            print(f"{k}:It reaches limit! I am {node.get('name')}")
            return
        if self.isThereNode(node["name"]):
            validNodes={}
            for i,v in node["to"].items():
                if self.isThereNode(i):
                    validNodes.update({i:v})
            selected=self.getNode(choice(list(validNodes.keys()), p=list(validNodes.values())))
            print(f"{k}:I am {node.get('name')}, I selected {selected.get('name')}")
            self.runNode(selected, limit, k+1)
        else:
            print(f"{k}:It's not valid node! {node.get('name')}")
    def sample(self, limit):
        starter=None
        for i in self.nodes:
            if i["start"]==True:
                starter=i
        self.runNode(starter, limit, 0)

myMP=mp()
myMP.addNode("Class 1", {"Class 2":0.5, "Facebook":0.5}, True, False)
myMP.addNode("Class 2", {"Class 3":0.8, "Sleep":0.2}, False, False)
myMP.addNode("Class 3", {"Pass":0.6, "Pub":0.4}, False, False)
myMP.addNode("Facebook", {"Facebook":0.9, "Class 1":0.1}, False, False)
myMP.addNode("Pass", {"Sleep":1.0}, False, False)
myMP.addNode("Pub", {"Class 1":0.2, "Class 2":0.4, "Class 3":0.4}, False, False)
myMP.addNode("Sleep", {}, False, True)
for i in range(5):
    myMP.sample(30)
    print("-----------")
