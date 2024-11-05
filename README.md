# GitWorkflowIntro


## Overview

This repo serves as an activity for students to practice the common git workflow commands.  Each student in the cohort will commit a short blurb about themselves including a picture. 

## Python Version

* Python 3.10.4
* pip 22.0.4

## Build Instructions 

```pip install flask```

```flask run```


## Contributing

After creating your fork of this repository, add an upstream link to the original repo. 

```git remote add upstream https://github.com/CTI-CodeDay/GitWorkflowIntro.git```

Create your own feature branch where you will commit your changes

```
git branch <your_branch_name>
git checkout <your_branch_name>
```

Frequently pull the latest changes from the main branch. 

```
git checkout main
git pull upstream main
git checkout <your_branch_name>
git merge main
```
<!-- Temporary change for pull request submission -->
