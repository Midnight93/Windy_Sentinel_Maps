===========
Sentinelsat
===========

Sentinelsat makes searching, downloading and retrieving the metadata of `Sentinel
<http://www.esa.int/Our_Activities/Observing_the_Earth/Copernicus/Overview4>`_
satellite images from the
`Copernicus Open Access Hub <https://scihub.copernicus.eu/>`_ easy.

It offers an easy-to-use command line interface

.. code-block:: bash

  sentinelsat -u <user> -p <password> --location Berlin --sentinel 2 --cloud 30 --start NOW-1MONTH

and a powerful Python API.

.. code-block:: python

  from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt

  api = SentinelAPI('user', 'password')
  footprint = geojson_to_wkt(read_geojson('search_polygon.geojson'))
  products = api.query(footprint,
                       producttype='SLC',
                       orbitdirection='ASCENDING',
                       limit=10)
  api.download_all(products)


.. toctree::
   :caption: Contents:
   :maxdepth: 2

   install
   cli
   api_overview
   api_reference
   common_issues

.. toctree::
   :hidden:

   changelog

Indices and tables
==================

  * :ref:`genindex`
  * :ref:`modindex`
  * :ref:`search`
