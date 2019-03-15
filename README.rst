========
DryYAML
========

.. image:: https://img.shields.io/pypi/v/dryyaml.svg
        :target: https://pypi.python.org/pypi/dryyaml

.. image:: https://img.shields.io/travis/bmritz/dryyaml.svg
        :target: https://travis-ci.org/bmritz/dryyaml

.. image:: https://readthedocs.org/projects/dryyaml/badge/?version=latest
        :target: https://dryyaml.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/bmritz/dryyaml/shield.svg
     :target: https://pyup.io/repos/github/bmritz/dryyaml/
     :alt: Updates


A way to completely stop repeating yourself in YAML configs.

* Free software: MIT license
* Documentation: https://dryyaml.readthedocs.io.

Installation
------------
To install dryyaml, use pip:

.. code-block:: bash

   $ pip install dryyaml


How it works
------------
A DryYAML config file is like a regular YAML config file, plus Jinja2_ variables and expressions. DryYAML transforms a DryYAML config file into plain vanilla YAML by passing the parsed YAML *above* each line of code to Jinja as the context under which each line in the DryYAML template is rendered. 

An example might help sort that out. Here is some example DryYAML with a simple jinja variable:

.. code-block:: yaml

   node1: val1
   node2:
     subnode1: subval1
     subnode2: {{ node1 }}

And here is what that would look like after running it through DryYAML:

.. code-block:: bash

   $ dryyaml -f test-yaml.yaml 
   node1: val1
   node2:
     subnode1: subval1
     subnode2: val1


Features
--------

* Write YAML with Jinja2_ variables and expressions included to give more control
* The context dictionary passed to the template at any point in the YAML file is the parsed YAML above that YAML line.
* DryYAML is a superset of YAML. Vanilla YAML will be parsed by DryYAML as expected.
* Hide parent nodes from the final YAML output by starting the keys with _

.. _Jinja2: http://jinja.pocoo.org/docs/

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
