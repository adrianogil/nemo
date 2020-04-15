# nemo
Tool to find and analyze Unity projects

Current version has the following output per project found:
```
Project <ProjectName>
  Path <ProjectPath>
  Total CS scripts: <Number of csharp scripts> ( LOC: <csharp LOC>)
  Total shader scripts: <Number of shader scripts> ( LOC: <shader LOC>)
```

# Command line options

```
nemo <path>
```

## Planned features
- Using a search query
```
nemo -q <search-query>
```

## Installation

Add the following lines to your bashrc:
```
export NEMO_DIR=<path-to-nemo>/nemo/
source $NEMO_DIR/src/bashrc.sh
```
(WIP I am going to create a better setup)

## Contributing

Feel free to submit PRs. I will do my best to review and merge them if I consider them essential.

## Development status

This is a very alpha software. The code was written with no consideration of coding standards and architecture. A refactoring would do it good...