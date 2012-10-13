subscribed
==========

.. image::
    https://secure.travis-ci.org/sigmavirus24/subscribed.png
    :alt: Build Status
    :target: https://travis-ci.org/sigmavirus24/subscribed

`Gittip: Support this project <https://www.gittip.com/sigmavirus24>`_

This is just a small flask app using github3.py_ to display which users are 
subscribed to which repositories. It can be used using endpoints like:

- ``/login``, e.g., ``/sigmavirus24``
- ``/login/repo``, e.g., ``/sigmavirus24/subscribed``

This information isn't available to everyone via the GitHub website, but it is 
available via the API.


.. links
.. _github3.py: https://github.com/sigmavirus24/github3.py
