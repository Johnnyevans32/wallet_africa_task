# wallet_africa_task

I used the bank transfer api to implement a bank transfer application for transferring money from one wallet to bank account using the deposit form.

Create an environment
Create a project folder and a venv folder within:

$ mkdir myproject
$ cd myproject
$ python3 -m venv venv
On Windows:

$ py -3 -m venv venv
If you needed to install virtualenv because you are using Python 2, use the following command instead:

$ python2 -m virtualenv venv
On Windows:

> \Python27\Scripts\virtualenv.exe venv
Activate the environment
Before you work on your project, activate the corresponding environment:

$ . venv/bin/activate
On Windows:

> venv\Scripts\activate
Your shell prompt will change to show the name of the activated environment.

Install Flask
Within the activated environment, use the following command to install Flask:

$ pip install Flask
Flask is now installed. Check out the Quickstart or go to the Documentation Overview.

Now Download my project repo

$ pip install -U https://github.com/Johnnyevans32/wallet_api_task/

Install virtualenv
If you are using Python 2, the venv module is not available. Instead, install virtualenv.

On Linux, virtualenv is provided by your package manager:

# Debian, Ubuntu
$ sudo apt-get install python-virtualenv

# CentOS, Fedora
$ sudo yum install python-virtualenv

# Arch
$ sudo pacman -S python-virtualenv
If you are on Mac OS X or Windows, download get-pip.py, then:

$ sudo python2 Downloads/get-pip.py
$ sudo python2 -m pip install virtualenv
On Windows, as an administrator:

> \Python27\python.exe Downloads\get-pip.py
> \Python27\python.exe -m pip install 
