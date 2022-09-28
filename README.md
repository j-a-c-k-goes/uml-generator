# UML Class Diagram

While reading [The Object Oriented Thought Process](https://www.oreilly.com/library/view/object-oriented-thought-process/9780135182130/), I wanted to reinforce the early concepts I have encountered by making a Python program which generates a simple Unified Modeling Language Class diagram; and outputs to a markdown file (located in outputs directory).  

- - -

## Installation
##### Installs Virtual Environment, Package manger
`brew install poetry (If you do not already have Poetry installed)`

##### Clone the repository
`gh repo clone j-a-c-k-goes/uml-generator`

- - -

## Use

##### Run script using bash

`open ~/.bash_profile`

`source ~/uml-generator/run-uml.sh` (Copy this into bash profile)

**Close bash profile**

**Return to your terminal**

`source ~/.bash_profile`

`uml` (Runs the script using bash shortcut)

##### (Run this way if you prefer not to use the bash script)

`python3 src/app/uml.py` 

##### Change into the outputs directory

`cd outputs/`

##### Open the file (Or run another command on the file)

`<open> <output-file>`

- - -

## Future Builds
* Construtor included in UML Diagram
* Parameter to control output file type
