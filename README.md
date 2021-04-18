# init

## extension, module, class
fork this repository and make a pull request with the following template:

```
NAME: work name
TITLE: work title
DESCRIPTION: a brief of the work
DEPENDENCIES: dependency modules
```
Make sure to change the <b>EXTENSION.json</b> if the work is an extension or <b>MODULES.json</b> if the work is a module along with the pull request.

The title must be soumething like this:
<br>
```<NAME>: <SPECIFIER>```
<br>
For example:
<br>
```torrent: extention```

The work must have the following files in the project:
1. <b>.mext:</b> Instruction of installing the work.


The responsibility of the work, including testing, quality, and etc, lies with the author.

## project
If you want to initialize something more than extension, module, or class, you should fork this repository and make a pull request with the following template:

```
NAME: project name - exactly like a github repository name
TITLE: project title
DESCRIPTION: a brief of the project
AUTHOR: leader name. It could be a nick name.
USERNAME: github author username
```
Make sure to change the <b>PROJECTS.json</b> along with the pull request.
The project must have the following files in the project:

1. <b>LICENSE:</b> License file could be anything
2. <b>README.md:</b> Readme file could be anything. there's no template for README.md files.
3. <b>.mext:</b> Instruction of installing the project.

## .mext

.mext file is what project uses it to install the code and have the following syntax:

```python

replace path/to/file.py with path/to/file.py
remove path/to/file.py
move path/to/folder in path2
```

Currently .mext supports the following commands: 
1. <b>replace:</b> it replaces files with new one.
2. <b>remove:</b> it removes directories or files. You can use * char for all.
3. <b>move:</b> it moves files and directories. You can use * char for all.

After acceptance, the username will be the leader of the project. The responsibility of the work, including testing, quality, and etc, lies with the author.
