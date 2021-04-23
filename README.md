# init

## extension
Fork this repository and make a pull request. Each extension should just have one module. The extension should be in a directory that specify the extension name. Look at the <i>/exts/hello_world extension</i> to get acquainted with the structure.

Make sure to change the <b>EXTENSION.json</b> along with the pull request.

The work must have the following files in itself:
1. <b>mext:</b> instruction of installing the work.
2. <b>requirements:</b> you may want create it with `pip freeze` or `pip install pipreqs && pipreqs`
3. <b>config.py:</b> if you want to config anything else, you can write your code in the config.py file, which will run before installing the extension

The responsibility of the work, including testing, quality, and etc, lies with the author.

## packages
If you want to initialize something more than extension, you should fork this repository and make a pull request with the following template:

```
NAME: project name - exactly like a github repository name
TITLE: project title | could be none
DESCRIPTION: a brief of the project | could be none
KEYWORDS: relevant keywords | could be none
USERNAME: github author username
```
Make sure to change the <b>PACKAGES.json</b> along with the pull request.
The project must have the following files in the project:

1. <b>LICENSE:</b> license file could be anything
2. <b>README.md:</b> readme file could be anything. there's no template for README.md files.
3. <b>mext:</b> instruction of installing the project.

## mext

mext file is what project uses it to install the code and have the following syntax:

```python
move util/hello.py to core/util
makedir modules/hello and add modules/hello/hello_world.py
['util/hello.py', 'modules/hello/hello_world.py']
```

Currently .mext supports the following commands: 
2. <b>makedir:</b> create a new directore if it doesn't exist. Then, add a file to the directory.
3. <b>move:</b> it moves files. If the file already exists, the previous file will be replaced.

After acceptance, the username will be the leader of the project. The responsibility of the work, including testing, quality, and etc, lies with the author.
