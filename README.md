This project use the JCDecaux's API : https://developer.jcdecaux.com/#/opendata/vls?page=getstarted

# Get started

1. Download the project from github :
```script
git clone https://github.com/RolletQuentin/
cd JCDecaux_api_test
```

2. It is recommended to use virtual environement for python :
```script
python3 -m venv env
source env/bin/activate
```

3. Download all the dependencie with pip :
```script
pip install -r requirements.txt
```

4. Add a config file in the src folder in the project. This config file must be named config.json :
```json
{
    "api_key": "your_api_key"
}
```

5. You can now run the application !
```script
python3 main.py
```
By default, only the first example is running. To see the two other examples, please uncomment the lines at the end of the main.py file