Blog
====

My static blog generated with pelican.

Currently hosted at [mthpower.uk](http://mthpower.uk)

### Installation

`git clone git@github.com:mthpower/blog.git`

`pip install -r requirements.txt`

### Development

`./develop_server.sh start`

... hack and type away ...

`./develop_server.sh stop`

### Generate and deploy to production

`pelican content -s publishconf.py`

`make s3_upload`
