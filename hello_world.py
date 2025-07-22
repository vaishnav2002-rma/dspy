import dspy 

class HelloWorld(dspy.Predict):
    def __init__(self):
        super().__init__(signature="name -> message")

    def forward(self, name:str) -> str:
        return f"Hello {name}, All the best with dspy"
    
predictor = HelloWorld()
print(predictor(name="Vaishnav"))