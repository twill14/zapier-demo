# Greetings

Greetings to any Zapiens who decided to check this out.

I wanted to take the time to demonstrate at least a fraction of my resolve regarding my interest in what you all are about.

And so with that, I wanted to present just a tiny framework I'd been working on in my spare time for the site.

Naturally this work isn't meant to be professional grade nor do I expect you to find much practical use of it, but I do hope that it serves as a plesant example of just some of the work I'd look forward to doing.

### Summary

Here i've built a small automation framework using pytest that cover some very basic black box smoke testing scenarios.

It also comes with some simple reporting via html link generation.

Supports Python Versions [36, 37, 38]

### Instructions

To use the repo you should only need to clone the repo to your machine and then install the framework with two commands:

1. `python setup.py install` or `py setup.py install` (depending on your setup)
2.  And then in the project folder you might need to install pytest unless you already have it with: 
    - `pip install pytest`
3. Right now we have two types of very simple tests. Smoke and HomePage. To run you can type:
    - `py pytest -m home` or `py pytest -m smoke`

    Or for all tests:
    - `py pytest -m "home or smoke"`
4. The default is in Chrome, but if you want to try firefox just add 
    - `--browser firefox` to the lines above
5. Finally, if you'd like to generate reports when running the tests be sure to add:
    - `--html="results.html"`
    
So for a full example of the points above you could run: 

    `pytest -m smoke --browser chrome --html="results.html"`

#### Bonus Notes for Tech Peeps

1. If you'd like to checkout or tweak the project for any reasons, I'd suggest using PyCharm IDE with Anaconda. As a whole, I've found the process to be far smoother compared to other package/env management tools
2. I used the `webdriver_manager` driver libraries as a means of providing some convenience in case someone tries to run the tests whom don't have chrome or geckodriver in their PATH
 
 That being said though, it seems that the library is best compatible with windows and not mac (is is not available in the mac version of anaconda package library), however, if you do find there to be complications while trying to check out the code in an ide via MacOS, i'd recommend removing lines 3 and 4 from `conftest.py` and then removing the driver install methods from lines 42 and 44:
 
 
    `driver = webdriver.Chrome(ChromeDriverManager().install())` --> `driver = webdriver.Chrome()`

  and:
  
     `driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())` --> `driver = webdriver.Firefox()`
     
  This way you can simply leverage the gecko and chrome webdrivers installed on the mac machines in your machine's PATH

For windows you can also try replacing the code for the drivers with the absolute path in which your own driver.exe is stored:

    `driver = webdriver.Chrome(executable_path=r'C:\path\to\chromedriver.exe')`
