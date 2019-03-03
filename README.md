
# Environment setup
In a folder, create a virtualenv with python 3.6 and install python dependencies
```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

# Configuration
Update the file `zappa_settings.json` with the parameters you want
Update the file `templates/upload_canvas_to_S3.html` with your AWS ACCESS KEY and AWS SECRET KEY

# Deployment
```
zappa init
zappa deploy dev
```

