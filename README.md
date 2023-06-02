# Fast Api
## _Download code from fastapi_
[Download Here](https://ulease.in:8181/docs#/code/files_download_code__get).

## Installation
Install the dependencies from requiremnets and start the server.

```

cd eastvantage
pip install -r requirements.txt


## edit env_vars.txt and pass your db parameters
# export EASTVANTAGE_DB_PORT=your_port
# export EASTVANTAGE_DB_HOST=your_host
# export EASTVANTAGE_DEFAULT_DB=defaultdb
# export EASTVANTAGE_DB_NAME=your_db_name
# export EASTVANTAGE_DB_USER=doadmin
# export EASTVANTAGE_DB_PWD=your_passw

# command to run after editing env_vars.txt
source env_vars.txt
python3 create_db.py
python3 main.py

```
