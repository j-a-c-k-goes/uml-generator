import sys

""" Program Composes UML Class Diagrams """

class UML():
    # Class contructor requries UML class name 
    def __init__(self, className):
        self.className = className
        self.attributes = list()
        self.methods = list()

    # Getters and Setters for UML Class Name
   
    def setClassName(self): className = self.className; return className
    def getClassName(self): return self.className
    def newClassName(self, newName):
        print(f"\nupdate: Class name changed! New class name: {newName}\n")
        self.className = newName
        return self.className 
    
    # Getters and settters for UML attributes 
   
    def setAttributes(self):
        enteringAttributes = True
        print('\nATTRBUTES:\n')
        while enteringAttributes:
            attribute = str(input( "Enter attribute's name: " ))
            dataType = str(input( "Enter the attribute's data type (String, int, ...): " ))
            visibility = self.visibility()
            self.attributes.append( { "attribute": attribute, "type": dataType, "visibility": visibility } )
            confirm = str(input( "Are you still entering attributes (y/n)? " ))
            if ( confirm.lower() == "n" ) or ( confirm.lower == "" ): break
            else: print("\nUpdate: prepare to enter the next attribute\n")
        return self.attributes

    def getAttributes(self): return attributes
    
    # Getters and setter for UML methods
    def setMethods(self):
        print('\nMETHODS:\n')
        enteringMethods = True
        while enteringMethods:
            method = str(input( "Enter method's name: " ))
            dataType = str(input( "Enter method's return data type (String, void, ..): " ))
            visibility = self.visibility()
            self.methods.append( { "method":method, "type":dataType, "visibility": visibility} )
            confirm = str(input( "Are you still entering methods (y/n)? " ))
            if (confirm.lower() == "n") or (confirm.lower == ""): break
            else: print("\nUpdate: prepare to enter the next method\n")
        return self.methods
    
    def getMethods(self): return methods
    
    # Format for printing/display
    def format(self, data):
        formatting = []  
        for element in data:
            results = []
            for value in element.values():
                results.append(value)
            if results[2] == 'PRIVATE':
                formatted = f'-{ results[0] }:{ results[1] }'
            else:
                 formatted = f'+{ results[0] }:{ results[1] }'
            formatting.append(formatted)
        return formatting

    # Determine visibility for a given attribute/method
    def visibility(self):
        gettingVisibility = True
        while gettingVisibility:
            vis = str(input('Is the attribute PUBLIC or PRIVATE: '))
            condition = ( vis.upper() == 'PUBLIC' ) or ( vis.upper() == 'PRIVATE' )
            if not condition:
                print('Must enter PUBLIC or PRIVATE')
            else:
                gettingVisiblity = False
                return vis
        
    # Output to file
    def output(self, className, attrs, methods):
        path = f'../../outputs/'
        filename = f'uml-{ self.className }.md'
        with open(f'{ path }/{ filename }', "w") as file:
            title = f'# { className }'
            body = 'This is a UnifiedModelingLanguage starter diagram. Edit from here.'
            tableHead = f'| `{ className }`                 |'
            tableSep = f'| ------------------------------- | '
            tableSepAlt = f'| =============================== | '
            file.write(title); file.write('\n')
            file.write(body); file.write('\n'); file.write('\n')
            file.write(tableHead); file.write('\n')
            file.write(tableSep); file.write('\n')
            for attr in attrs: 
                file.write(f'| { attr } |');file.write('\n')
            file.write(tableSepAlt); file.write('\n')
            for method in methods: 
                file.write(f'| { method } |'); file.write('\n')
        print('Done writing UML to markdown file.') 

if __name__ == "__main__":
    prompt = str(input("Enter name of class: "))
    uml = UML(prompt)
    className = uml.setClassName()
    attrs = uml.setAttributes()
    attrs = uml.format(attrs) # formatted
    methods = uml.setMethods()
    methods = uml.format(methods) # formatted
    uml.output(className, attrs, methods)