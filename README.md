# UML Class Diagram

While reading [The Object Oriented Thought Process](https://www.oreilly.com/library/view/object-oriented-thought-process/9780135182130/), I wanted to reinforce the early concepts I have encountered by buidling a Python program which generates a simple Unified Modeling Language Class diagram; and outputs to a markdown file (located in outputs directory).  

- - -

## Installation
##### Installs Virtual Environment, Package manger
`brew install poetry (If you do not already have Poetry installed)`

##### Clone the repository
`gh repo clone j-a-c-k-goes/uml-generator`

- - -

## Use

#### Running the script 
There are at least two ways to run the UML builder — via the provided bash script OR via python3 command. Both require using the terminal, however.

##### Using the provided shell script
`sh run-uml.sh`

##### Using python3 command
`python3 ~/uml-generator/src/app/uml.py` 

#### Locating output
The script is designed to output UML diagrams as a amrkdown file. These are located within an Outputs directory.

##### Change into the outputs directory
`cd outputs/`

##### Open the file
`open <output-file>`

##### If you use SublimeText and have command-line tools insalled
`subl -<a,n> <outputFileName>`
- - -

## Future Builds
* Constructor included in UML Diagram ✅
* Parameter to control output file type
