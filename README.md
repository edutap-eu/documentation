# eduTAP central documentation

This is the documentation of eduTAP.

The official documentation's HTML pages are located at https://doc.edutap.eu

## Authoring

For the local authoring preview, you first need Python 3.11 to be installed.
Then you need to clone the repository.
Then have to run the following commands in the cloned repositories directory:

```bash
python -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
make livehtml
```

Then go to http://localhost:8000 to view the documentation.

Each time you save a file, the part gets re-rendered and reloaded in the browser.

## Build and deployment

Changes to the main branch are rendered and deployed with GitHub Actions on each push.
It uses GitHub Pages for hosting.

# License

The documentation is licensed under [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/).
