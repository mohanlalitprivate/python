# Anagram Finder
## Requirements

- Python 3.0 or latest
- ```yourfilename``` Any file which has words in it, with assumption of each line containing exactly one word.
- Make sure to provide the exact file path at the run time (file could be in sub dir, in same dir or any other dir)
- Example from 'src' dir (above step)```> python anagram.py path/to/your/file``` 
    (assuming you have set the path to invoke Python 3 using this command)
    
- Dir 'tests' contains tests, hence the file requirements.txt and tox.ini
- Create virtual env learn more from ```https://virtualenvwrapper.readthedocs.io/en/latest/install.html```
- If you have pip3 ```pip3 install virtualenvwrapper``` you will see a dir .virtualenv in your home dir
# virtualenvs
- MAC instructions  
- export WORKON_HOME=$HOME/.virtualenvs
- export PROJECT_HOME=$HOME/your/project/dir 
- export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3
- source /usr/local/bin/virtualenvwrapper.sh
# Creating virtual env
- $> workon
- $> mkvirtualenv temp
- $> workon temp
- And after switching to that env, run ```pip install -r requirements.txt```
- To run test simply type ```tox``` or ```py.test``` from 'tests' dir

# To run as server
- Run ```python app.py```
- Server listens on port 5000
- Go to localhost:5000
- To find anagrams api url is ```http://localhost:5000/anagrams/<your-word>```
- Example ```http://localhost:5000/anagrams/stop```

# To create a docker image
- Modify ```app.py```
- Comment out ```app.run(port=5000)```
- Uncomment ```app.run(host='0.0.0.0')```
- Create docker image
- Go to folder ```anagrams``` this is where the Dockerfile is
- run ```docker build --tag python-anagram-docker .```
- Tag it ```docker build --tag python-anagram-docker .```
- In case you want to version it ```docker tag python-anagram-docker:latest python-anagram-docker:v1.0.0```
- Run ```docker run --publish 5000:5000 --name python-anagram-container -d python-anagram-docker```
- To stop docker ```docker stop python-anagram-container```
- To start again ```docker start python-anagram-container```