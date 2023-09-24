## Site Generator
Downloads and saves website assets and metadata locally.
### Local setup

Build image locally
`docker build --no-cache -t fetch_module .`

Fetch site and metadata
`docker run -v $(pwd):/usr/src/module -it fetch_module fetch.py [urls]...`

Fetch metadata
`docker run -v $(pwd):/usr/src/module -it fetch_module fetch.py --meta url`
