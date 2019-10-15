# parallel-demo
## how to run:
stack build
stack exec parallel-demo-exe

## output from project creation
output from "stack new":

Downloading template "new-template" to create project "parallel-demo" in parallel-demo/ ...

The following parameters were needed by the template but not provided: author-name
You can provide them in /home/riley/.stack/config.yaml, like this:
templates:
  params:
    author-name: value
Or you can pass each one as parameters like this:
stack new parallel-demo new-template -p "author-name:value"


The following parameters were needed by the template but not provided: author-email, author-name, category, copyright, github-username
You can provide them in /home/riley/.stack/config.yaml, like this:
templates:
  params:
    author-email: value
    author-name: value
    category: value
    copyright: value
    github-username: value
Or you can pass each one as parameters like this:
stack new parallel-demo new-template -p "author-email:value" -p "author-name:value" -p "category:value" -p "copyright:value" -p "github-username:value"

Looking for .cabal or package.yaml files to use to init the project.
Using cabal packages:
- parallel-demo/

Selecting the best among 16 snapshots...

* Matches lts-14.9

Selected resolver: lts-14.9
Initialising configuration using resolver: lts-14.9
Total number of user packages considered: 1
Writing configuration to file: parallel-demo/stack.yaml
All done.

