# VS code setting.json

```python
{
    "window.zoomLevel": 1,
    "editor.tabSize": 2,
    "[python]": {
        "editor.insertSpaces": true,
        "editor.tabSize": 4
    },
    "python.languageServer": "Pylance",
    "python.analysis.extraPaths": [
        "./sources"
    ],
    "workbench.startupEditor": "none",
    "workbench.editorAssociations": {
        "*.ipynb": "jupyter-notebook"
    },
    "notebook.cellToolbarLocation": {
        "default": "right",
        "jupyter-notebook": "left"
    },
    "terminal.integrated.defaultProfile.windows": "Git Bash",
    "explorer.confirmDelete": false,
    "editor.renderWhitespace": "all",
    "editor.fontFamily": "D2coding, Consolas, 'Courier New', monospace",
    "liveServer.settings.donotShowInfoMsg": true,
    // Django
    "files.associations": {
        "**/*.html": "html",
        "**/templates/**/*.html": "django-html",
        "**/templates/**/*": "django-txt",
        "**/requirements{/**,*}.{txt,in}": "pip-requirements"
    },
    "emmet.includeLanguages": {
        "django-html": "html"
    },
}
```

