import requests
from bs4 import BeautifulSoup
import re

url = 'https://digitallibrary.un.org/search?cc=Voting+Data&ln=en&as=1&rm=&sf=latest+first&so=d&rg=50&c=Voting+Data&c=&of=hb&fti=0&fct__2=General+Assembly&fct__9=Vote&fti=0&as_query=JTdCJTIyZGF0ZV9zZWxlY3RvciUyMiUzQSU3QiUyMmRhdGVUeXBlJTIyJTNBJTIyY3JlYXRpb25fZGF0ZSUyMiUyQyUyMmRhdGVQZXJpb2QlMjIlM0ElMjJhbGx5ZWFycyUyMiUyQyUyMmRhdGVGcm9tJTIyJTNBJTIyJTIyJTJDJTIyZGF0ZVRvJTIyJTNBJTIyJTIyJTdEJTJDJTIyY2xhdXNlcyUyMiUzQSU1QiU3QiUyMnNlYXJjaEluJTIyJTNBJTIydGl0bGUlMjIlMkMlMjJjb250YWluJTIyJTNBJTIyYWxsLXdvcmRzJTIyJTJDJTIydGVybSUyMiUzQSUyMktvcmVhJTJDJTIwRGVtb2NyYXRpYyUyMiUyQyUyMm9wZXJhdG9yJTIyJTNBJTIyQU5EJTIyJTdEJTJDJTdCJTIyc2VhcmNoSW4lMjIlM0ElMjJhbGwtZmllbGQlMjIlMkMlMjJjb250YWluJTIyJTNBJTIyYWxsLXdvcmRzJTIyJTJDJTIydGVybSUyMiUzQSUyMiUyMiUyQyUyMm9wZXJhdG9yJTIyJTNBJTIyQU5EJTIyJTdEJTVEJTdE&action_search=placeholder#searchresultsbox'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

table = soup.find('table', id="main-content")

#なにがどう取れてるのかまったくわからん。




