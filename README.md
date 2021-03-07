# python-modbus

> Modbus communication sample in python

## IDE

Using Visutal Studio Code

### Visual Studio Code Extensions Setup

Use extensions:

- Auto Rename Tag
- Code Runner
- Debugger for Chrome
- Docker
- Path Intellisense
- Prettier - Code formatter
- Python
- Python Docstring Generator
- Python-autopep8
- TabNine Autocomplete AI
- Theme: Oceanic Next
- Todo Tree

File > Preference > Settings > User Settings:
```JSON
"auto-rename-tag.activationOnLanguage": [
    "html",
    "xml",
    "php",
    "javascript",
    "python"
  ],
  "editor.formatOnPaste": false,
  "editor.formatOnSave": true,
  "editor.insertSpaces": true,
  "editor.wordWrap": "on",
  "files.watcherExclude": {
    "**/.git/objects/**": true,
    "**/.git/subtree-cache/**": true,
    "**/node_modules/**": true,
    "**/nodec/**": true,
    "**/.hg/store/**": true
  },
  "files.associations": {
    "*.thor": "ruby",
    "*.jsx": "javascript",
    "*.phe": "json"
  },
  "prettier.singleQuote": true,
  "telemetry.enableTelemetry": false,
  "telemetry.enableCrashReporter": false,
  "todo-tree.tree.showScanModeButton": false,
  "update.mode": "none",
  "workbench.colorTheme": "Oceanic Next (dimmed bg)",

  "autoDocstring.docstringFormat": "google",
  "python.linting.enabled": true,
  "python.linting.pycodestyleEnabled": true,
  "python.linting.pylintEnabled": true,
  "python.linting.pydocstyleEnabled": true,
  "python.linting.pydocstyleArgs": [
    "--ignore=D203,D211,D213,D406,D407,D408,D409,D410"
  ],
  "python.pythonPath": "/usr/bin/python3.6",
  "python.testing.unittestEnabled": false,
  "[python]": {
    "editor.detectIndentation": false,
    "editor.insertSpaces": true,
    "editor.tabSize": 4
  },
  "tabnine.experimentalAutoImports": true
}
```

See [Makefile](Makefile) and [Makefile.common](Makefile.common) for more options.


## Usage example

Installing required packages:
```bash
$ make init
```
```
Running the project:
```bash
$ make run
```
See [Makefile](Makefile) for more options.

# Repository

[main repository](https://github.com/luisprox/python-modbus/src/master/)
[issues](https://github.com/luisprox/python-modbus/issues?status=new&status=open)
[clone address](git@github.com:luisprox/python-modbus.git)

# Meta

Luis Ricardo Batista Prox – luis.prox@procontroltec.com.br
PRO-Control Tecnologia.

See [LICENSE](LICENSE) for more information.
