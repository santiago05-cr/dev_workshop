
# Python Workshop

This is a repo to remember the basics of python programming language.


<div align="center">  
<a href="https://www.python.org/" target="_blank"><img style="margin: 10px" src="https://profilinator.rishav.dev/skills-assets/python-original.svg" alt="Python" height="50" /></a>  
</div>

## How to start

Fork the current repo. Look in the right corner.

Now the repo is in tour profile.

Clone the repo in your local machine in a new and empty directory.

In your terminal 

```bash
  mkdir my-new-directory
  cd my-new-directory
```

```bash
  git clone <the repo link> .
```


## Open Visual Sctudio Code

After clone the project, open Visual Studio Code the working directory.
In the terminal of Visual Studio Code create a new Virtual Environment

```bash
  python -m venv myvenv
```

Active the venv (Linux)

```bash
  source myvenv/bin/activate
```

Install requirements

```bash
  pip install -r requirements.txt
```

Start solving the tests.


## Commit changes

To run tests, you should to complete the tests and commit them.

```bash
  git add <file>
  git commit -m "your msg"
  git push -u origin main
```

### Then go to your github repo

Look in the actions tab.

![image](https://github.com/sigmotoa/dev_workshop/blob/main/Screenshot%20at%20Feb%2027%2008-22-50.png) 

You will find the tests running.

When all will pass you've finished the workshop.

Send much commits as you need.

# Updatings.

If your teachers send you an advice, you should to add a new remote to receive the new changes.

> [!WARNING]
> You should to use previously
> ```bash
>   git status
> ```
> Your local repo should be clean after receive the new updates.

```bash
  git remote add original https://github.com/sigmotoa/dev_workshop.git
  git pull original main
  
```



