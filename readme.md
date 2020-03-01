# Greetings

Greetings to any Zapiens who decided to check this out.

I wanted to take the time to demonstrate at least a fraction of my resolve regarding my interest in what you all are about.

And so with that, I wanted to present just a tiny framework I'd been working on in my spare time for the site.

Naturally this work isn't meant to be professional grade nor do I expect you to find much practical use of it, but I do hope that it serves as a plesant example of just some of the work I'd look forward to doing.

## Summary

Here. i've built a small automation framework using pytest that cover some very basic black box smoke testing scenarios.

It also comes with some simple reporting via html link generation.
### Instructions

To use the repo you should only need to clone the repo to your machine and then install the framework with two commands:

1. `python setup.py install` or `py setup.py install` (dependin on your setup)
2.  And then in the project folder you might need to install pytest unless you already have it with: 
    - `py -m pytest`
    - `python -m pytest`

#### Quick Notes
   
1. I designed the framework to be compatible with Python versions 3.6 and 3.7 ideally.
2. The framework should be able to run on Mac or Windows but windows might be a smoother experience for people looking to tweak it more.

#### Bonus Notes for Tech Peeps

1. If you'd like to checkout or tweak the project for any reasons, I'd suggest using PyCharm IDE with Anaconda. As a whole, I've found the process to be far smoother compared to other package/env management tools
2. I used the `webdriver_manager` driver libraries as a means of providing some convienence in case someone tries to run the tests whom don't have chrome or geckodriver in their PATH
 
 That being said though, it seems that the library is best compatible with windows and not mac (is is not available in the mac version of anaconda package library), however, if you do find there to be complications while trying to check out the code in an ide via MacOS, i'd recommend removing lines 3 and 4 from `conftest.py` and then removing the driver install methods from lines 42 and 44:
 
 
    `driver = webdriver.Chrome(ChromeDriverManager().install())` --> `driver = webdriver.Chrome()`

  and:
  
     `driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())` --> `driver = webdriver.Firefox()`
     
  This way you can simply leverage the gecko and chrome webdrivers installed on the mac machines in PATH