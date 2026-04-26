class Task:
    def __init__(self, taskId, taskDescription, dueDate, tags):
        self.taksId = taskId
        self.description = taskDescription
        self.dueDate = dueDate
        self.tags = set(tags)
        self.isCompleted = False

    def hasTag(self, tag):
        return tag in self.tags

    def active(self):
        return not self.isCompleted

    def getDueDate(self):
        return self.dueDate

    def markCompleted(self):
        self.isCompleted = True

    def getName(self):
        return self.description

class TodoList:

    def __init__(self):
        self.newTaskId = 1
        self.usersTaks = collections.defaultdict(dict)

    def addTask(self, userId: int, taskDescription: str, dueDate: int, tags: List[str]) -> int:
        taskId = self.newTaskId
        self.newTaskId += 1
        task = Task(taskId, taskDescription, dueDate, tags)
        self.usersTaks[userId][taskId] = task
        
        return taskId

    # ordered by dueDate and only not completed
    def getAllTasks(self, userId: int) -> List[str]:
        return list(map(lambda task: task.getName(), self.sortTasksByDueDate(self.getActiveTaskByUser(userId))))
        
    def getTasksForTag(self, userId: int, tag: str) -> List[str]:
        tasksForTag = filter(lambda task: task.hasTag(tag), self.getActiveTaskByUser(userId))
        return list(map(lambda task: task.getName(), self.sortTasksByDueDate(tasksForTag)))
        
    def completeTask(self, userId: int, taskId: int) -> None:
        task = self.usersTaks[userId].get(taskId)
        if task:
            task.markCompleted()

    def getActiveTaskByUser(self, userId):
        return list(filter(lambda task: task.active(), self.usersTaks[userId].values()))

    def sortTasksByDueDate(self, tasks):
        return list(sorted(tasks, key = lambda task: task.getDueDate()))
        

# Your TodoList object will be instantiated and called as such:
# obj = TodoList()
# param_1 = obj.addTask(userId,taskDescription,dueDate,tags)
# param_2 = obj.getAllTasks(userId)
# param_3 = obj.getTasksForTag(userId,tag)
# obj.completeTask(userId,taskId)