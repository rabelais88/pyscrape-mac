
### Prerequisite

for MacOS :
`brew install libxml2 libxslt`

for Ubuntu : 
`sudo apt-get install -y libxml2-dev libxslt-dev libpython3-dev zlib1g-dev`

other than those, use `requirements.txt`

to unfreeze : `pip install -r requirements.txt`

getting template document for exercise : `wget http://www.hanbit.co.kr/store/books/full_book_list.html`

install mongodb(MacOS) :
```
// to install mongodb
brew install mongodb

// to start mongodb daemon
mongod
```
TIP: on Mac environments, VScode prohibits using two linters at the same time. just stick with one linter if the linter is not working. (command palette -> `Python:Select linter` and disable anything not necessary)