# Installation

## Dependencies

*These distributions will be installed automatically when installing Flask.*

- **Werkzeug** implements WSGI, the standard Python interface between applications and servers.

- **Jinja** is a template language that renders the pages your application serves.

- **MarkupSafe** comes with Jinja. It escapes untrusted input when rendering templates to avoid injection attacks.

- **ItsDangerous** securely signs data to ensure its integrity. This is used to protect Flask’s session cookie.

- **Click** is a framework for writing command line applications. It provides the flask command and allows adding custom management commands.

## Virtual environments

1. Create an Environment
- macOS/Linux
  $ mkdir myproject
  $ cd myproject
  $ python3 -m venv venv

- Windows
  > mkdir myproject
  > cd myproject
  > py -3 -m venv venv

2. Activate the Environment
- macOS/Linux
  $ . venv/bin/activate

- Windows
  *source for my personal laptop*
  *$ source venv/Scripts/activate*
  > venv\Scripts\activate 

## Install Flask
$ pip install Flask