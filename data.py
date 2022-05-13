class Phone(object):

 def __init__(self,model,color):
     self.color=color
     self.model=model
 def start(self):
     print("working")

 def stop(self):
     print("stopped")

samsung=Phone("A5","black")
print(samsung.start())

    