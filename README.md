# Lookbook

## Description
This is a platform that introduces a social aspect to online shopping. Users can follow friends and see what they shop for.

## Installation
Make sure you have [`pipenv`](https://docs.pipenv.org/en/latest/) installed.

### Setting up the Django Backend
1. `git clone https://github.com/lantingchiang/Lookbook.git` to clone the repository to your local machine
2. `pipenv install` to install all project dependencies
3. `pipenv shell` to activate the virtual environment
In the virtual environment...
4. `./manage.py makemigrations`
5. `./manage.py migrate`
6. `./manage.py runserver` and follow the url in the console

## Ongoing development
1. `git pull origin master` to get the most up to date code
2. `git branch [branchname]` to create a new branch
3. `git checkout [branchname]` to switch to new branch
4. Start developing :)
5. `git push origin [branchname]` to push local commits to remote repository
6. Make a pull request and request 1 reviewer in order to merge to master

## Documentation
### API Routes
<table>
  <tr>
    <th>Route</th>
    <th>Request Method</th>
    <th>Parameters</th>
    <th>Response</th>
  </tr>
  <tr>
    <td>"/api"</td>
    <td><code>GET</code></td>
    <td>NA</td>
    <td>Serves static page <code>home.html</code></td>
  </tr>
  <tr>
    <td><code>/api/products</code></td>
    <td><code>GET</code></td>
    <td>NA<td>
    <td>Renders all looks in reverse chronological order (feed page)</td>
  </tr>
  <tr>
    <td><code>/api/products</code></td>
    <td><code>POST</code></td>
    <td><td>
    <td>Allows creation of new product</td>
  </tr>
  <tr>
    <td>"/api/products/<int:pk>"</td>
    <td><code>GET</code></td>
    <td></td>
    <td>Shows detail view of product with given primary key</td>
  </tr>
  <tr>
    <td>"/api/products/<int:pk>"</td>
    <td><code>PUT/PATCH</code></td>
    <td></td>
    <td>Allows edits to product with given primary key</td>
  </tr>
  <tr>
    <td>"/api/products/<int:pk>"</td>
    <td><code>DELETE</code></td>
    <td></td>
    <td>Deletes product with given primary key</td>
  </tr>
</table>

### Accessing the admin site

[See official documentation here](https://docs.djangoproject.com/en/3.0/ref/contrib/admin/)
<ol>
  <li>Run <code>./manage.py createsuperuser</code> to create credentials for logging into admin site</li>
  <li>Enter username and password in command line as prompted</li>
  <li>Start the server by running <code>./manage.py runserver</code></li>
  <li>Access the admin site at http://127.0.0.1:8000/admin/</li>
  <li>Log in and create model instances!</li>
</ol>

