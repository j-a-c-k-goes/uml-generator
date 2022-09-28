# UML Class Diagram

While reading [The Object Oriented Thought Process](https://www.oreilly.com/library/view/object-oriented-thought-process/9780135182130/), I wanted to reinforce the early concepts I have encountered by making a Python program which generates a simple Unified Modeling Language Class diagram; and outputs to a markdown file (located in outputs directory).  
- - -

## Installation
`brew install poetry (if you do not already have poetry)`

`gh clone git@github.com:j-a-c-k-goes/uml-generator.git`

## Use
`source ~/<bashprofile>`

`uml`

`python3 src/app/uml.py` (use this if you prefer not to use the bash script)

`cd outputs/`

`<open> <output-file>`

## Future Builds
* Construtor included in UML Diagram
* Parameter to control output file type
