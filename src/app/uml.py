""" Program Composes UML Class Diagrams """

class UML():
    def __init__(self, className):
        self.className = className
    
    """ Class Name """
    def setClassName(self):
        className = self.className
        return className
    def getClassName(self):
        return self.className
    def newClassName(self, newName):
        print(f"\nupdate: Class name changed! New class name: {newName}\n")
        self.className = newName
        return self.className 
    
    """ Attributes """
    def setAttributes(self):
        global attributes
        attributes = []
        enteringAttributes = True
        while enteringAttributes:
            attribute = str(input("Enter name of attribute: "))
            dataType = str(input("Enter data type of attribute: "))
            attributes.append({"Attribute":attribute, "type":dataType})
            confirm = str(input("Are you still entering attributes (y/n)? "))
            if confirm.lower() == "n" or confirm.lower == "":
                break
            else:
                print("\nUpdate: prepare to enter the next attribute\n")
        return attributes
    def getAttributes(self):
        return attributes
    def formatAttributes(self):
        formatting = []  
        for element in attributes:
            results = []
            for value in element.values():
                results.append(value)
            formatted = f"-{results[0]}:{results[1]}"
            formatting.append(formatted)
        return formatting
    
    """ Methods """
    def setMethods(self):
        global methods
        methods = []
        enteringMethods = True
        while enteringMethods:
            method = str(input("Enter name of method: "))
            dataType = str(input("Enter data type of method: "))
            methods.append({"method":method, "type":dataType})
            confirm = str(input("Are you still entering methods (y/n)? "))
            if confirm.lower() == "n" or confirm.lower == "":
                break
            else:
                print("\nUpdate: prepare to enter the next method\n")
        return method
    def getMethods(self):
        return methods
    def formatMethods(self):
        formatting = []  
        for element in methods:
            results = []
            for value in element.values():
                results.append(value)
            formatted = f"+{results[0]}:{results[1]}"
            formatting.append(formatted)
        return formatting
        
    """ Output """
    def output(self, data):
        with open(f"./outputs/uml-{self.className}.md", "w+") as file:
            file.write(data)

if __name__ == "__main__":
    usrInput = str(input("Enter name of class: "))
    uml = UML(usrInput)
    className = uml.setClassName()
    umlAttrs = uml.setAttributes()
    umlAttrs = uml.formatAttributes()
    umlMethods = uml.setMethods()
    umlMethods = uml.formatMethods()
    data = f"""
# {className}
---
    
## Attributes
`{umlAttrs}`
    
---
    
## Methods
`{umlMethods}`
    """
    uml.output(data)
    
                 
        