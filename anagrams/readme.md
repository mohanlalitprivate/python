# Anagram Finder
## Requirements

- Python 3.0 or latest
- ```yourfilename``` Any file which has words in it, with assumption of each line containing exactly one word.
- Make sure to provide the exact file path at the run time (file could be in sub dir, in same dir or any other dir)
- Example from 'src' dir (above step)```> python anagram.py path/to/your/file``` 
    (assuming you have set the path to invoke Python 3 using this command)
    
- Dir 'tests' contains tests, hence the file requirements.txt and tox.ini
- Create virtual env and after switching to that env, run ```pip install -r requirements.txt```
- To run test simply type ```tox``` or ```py.test``` from 'tests' dir