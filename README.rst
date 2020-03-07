Materialized tree for Django 3.x
================================

.. image:: https://github.com/kostya-ten/django_tree_materialized/workflows/Workflows/badge.svg
     :target: https://github.com/kostya-ten/django_tree_materialized/actions/
     :alt: GihHub Action

.. image:: https://requires.io/github/kostya-ten/django_tree_materialized/requirements.svg?branch=master
     :target: https://requires.io/github/kostya-ten/django_tree_materialized/requirements/?branch=master
     :alt: Requirements Status

.. image:: https://api.codacy.com/project/badge/Grade/8af689b2407342a08a42d6cb719ea51a
     :target: https://www.codacy.com/manual/kostya/django_tree_materialized?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=kostya-ten/django_tree_materialized&amp;utm_campaign=Badge_Grade
     :alt: Codacy grade

Requirements
""""""""""""""""""
* Python 3.6+
* A supported version of Django (currently 3.x)

Getting It
""""""""""""""""""
You can get Django tree materialized by using pip::

    $ pip install pip install django-tree-materialized

If you want to install it from source, grab the git repository from GitHub and run setup.py::

    $ git clone git://github.com/kostya-ten/django_tree_materialized.git
    $ cd django_tree_materialized
    $ python setup.py install


Installation
""""""""""""""""""
To enable ``django_tree_materialized`` in your project you need to add it to `INSTALLED_APPS` in your projects ``settings.py``

.. code-block:: python

    INSTALLED_APPS = (
        # ...
        'django_tree_materialized',
        # ...
    )


