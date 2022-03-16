.. AmazonEcho documentation master file, created by
   sphinx-quickstart on Thu Mar  3 20:02:32 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to AmazonEcho's documentation!
======================================


.. image:: amazonechoprocess.PNG
:alt: High level overview of Amazon echo program


*

Database used SQLite, database table called audio, with columns id (int) , audio_name (text), data (blob)
category (text), SHORT_DEC (text)

*

.. automodule:: txt_to_speech
    :members: text_to_speech

.. automodule:: speech_to_txt
    :members: speech_to_text

.. automodule:: answer_service
    :members: answer_mode

.. automodule:: database_entry
    :members:

.. automodule:: database_retriv
    :members:

.. automodule:: listening_service
    :members:

.. automodule:: play_service
    :members:

.. automodule:: main
    :members:

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
