# Python Project Development

This is how I do Python development today.

## Tools

- `black` formatting source files
- `isort` to organize imports
- `mypy` static type checking
- `pylint` linting errors
- `poetry` for package management
- `pyproject.toml` centralizes all tooling config

## Prerequisites

To run this, you first need to install these tools:

- pyenv https://github.com/pyenv/pyenv
- pipx https://pipx.pypa.io/stable/installation/
- poetry https://python-poetry.org/
- make https://www.gnu.org/software/make/

## VSCode Extensions

- MS Python Extension [[link](https://marketplace.visualstudio.com/items?itemName=ms-python.python)]
- Mypy for type checking (I use the pre-release version) [[link](https://marketplace.visualstudio.com/items?itemName=ms-python.mypy-type-checker)]
- Black for formatting [[link](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter)]
- Isort for sorting imports [[link](https://marketplace.visualstudio.com/items?itemName=ms-python.isort)]
- Pylint for linting [[link](https://marketplace.visualstudio.com/items?itemName=ms-python.pylint)]

Note: if you clone this repository and open with VSCode, the `.vscode/extensions.json` file should suggest you to install them.

## VSCode Settings

```
{
    // makes the project tree cleaner by hiding pycache and other files
    "files.exclude": {
        "**/.classpath": true,
        "**/.factorypath": true,
        "**/.project": true,
        "**/.pytest_cache": true,
        "**/.settings": true,
        "**/__pycache__": true
    },
    // makes the project tree cleaner by adding newlines at the end of files and removing trailing whitespace
    "files.insertFinalNewline": true,
    "files.trimTrailingWhitespace": true,
    // shows in-line suggestions as you type
    "editor.inlineSuggest.enabled": true,
    // sets black as the formatter
    "editor.defaultFormatter": "ms-python.black-formatter",
    // runs black whenever you save a file
    "editor.formatOnSave": true,
    // defines a ruler at 120 characters (matches the configuration in pyproject.toml for black)
    "editor.rulers": [
        120
    ],
    // enables isort
    "isort.check": true,
    // uses isort from the active .venv
    "isort.importStrategy": "fromEnvironment",
    // runs isort whenever you save a file
    "editor.codeActionsOnSave": {
        "source.organizeImports": "explicit"
    },
    // configure cache settings for mypy (faster execution) and force mypy to check untyped definitions
    "mypy-type-checker.args": [
        "--cache-dir=.mypy_cache/.vscode",
        "--check-untyped-defs"
    ],
    // uses mypy from the active .venv
    "mypy-type-checker.importStrategy": "fromEnvironment",
    // mypy runs on workspace (nice to know if you're breaking things elsewhere) but only recommended for smaller repos as it gets slower with larger code bases
    "mypy-type-checker.reportingScope": "workspace",
    "mypy-type-checker.severity": {
        "error": "Error",
        "note": "Information"
    },
    // disables pylint on typing (defaults to lint on save, which is faster)
    "pylint.lintOnChange": false,
    // uses pylint from the active .venv
    "pylint.path": [
        "pylint"
    ],
    // visual aid when reading code by showing function return types, variable types and call argument names
    "python.analysis.inlayHints.callArgumentNames": "all",
    "python.analysis.inlayHints.functionReturnTypes": true,
    "python.analysis.inlayHints.variableTypes": true,
    // enables pytest and disables unittest when collecting and running tests from the workspace
    "python.testing.pytestEnabled": true,
    "python.testing.unittestEnabled": false
}
```

## Checking Formatting, Linting and Type-checking for the entire project

https://github.com/user-attachments/assets/7a04bd96-0027-4aac-8f1c-2b4b1fe049b5

## Linting and Type Checking on Save

https://github.com/user-attachments/assets/d18370c2-9823-49fa-813e-a988c96e19e9

## Format, Organize Imports on Save

https://github.com/user-attachments/assets/6b6370ba-49b1-47b8-94cc-7011d0ad020f

