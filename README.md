# eduTAP central documentation

This is the repository of the official documentation of eduTAP.

Its HTML pages are located at https://doc.edutap.eu

## Authoring

This documentation is written using [Sphinx](https://www.sphinx-doc.org/) and [MyST](https://myst-parser.readthedocs.io/), a rich and extensible flavour of Markdown for authoring technical and scientific documentation.f

For the local authoring preview, you

1. need Python 3.11+ and uv to be installed.
2. clone the repository and init submodules

   ```bash
   git clone https://github.com/edutap-eu/documentation.git
   cd documentation
   git submodule update --init --recursive
   ```

3. run the following commands in the cloned repositories directory:

   ```bash
   uv venv
   source ./venv/bin/activate
   make docs-live
   ```
1. go to http://localhost:8000 to view the documentation.

Each time you save a file, this part gets re-rendered and reloaded in the browser.

## Build and deployment

Changes to the main branch are rendered and deployed with GitHub Actions on each push.
It uses GitHub Pages for hosting.

# License

The documentation is licensed under [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/).
