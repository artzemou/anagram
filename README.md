# Run on local server

### npm i -s
### node index.js

This runs Python script anagram.py.
### Latest changes:
#### 2021-12-07 command line args
The script receives args from the command line using argparse.

```
usage: anagram.py [-h] [-b] [word]

Find the anagrams for a specific string of letters (French)

positional arguments:
  word         the starting point for the anagrams

optional arguments:
  -h, --help   show this help message and exit
  -b, --build  build the dict from the available text file
```
If no word is specified in the command line, "toupie" is used as a default.
("toupie" or not "toupie", that could be a question)

#### 2021-12-07 error logging
The script creates/updates a log file (anagram.log) using the logging library.
fulllog.py acts as a "façade" and combines the logging features  to direct the messages both to to the screen and to a rotating file.

### Known issues
#### Hardcoded filenames
Filenames are currently hard-coded and should be replaced by command line parameters.
This is a candidate new feature

#### Log and Json
There is a possible interference between the output of logging and the json data expected by the embedding JS script.
This needs to be checked.

#### Languages
It should be possible to run the same algorithm with other languages. Noticeably: english.
This is a candidate new feature.

