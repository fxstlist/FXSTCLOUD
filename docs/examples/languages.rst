Language
=======================
You can modify the default language files and even create your own language files.

.. note::

   The following languages are available by default:

   - English (``en``)
   - German (``de``)


Modify language files
---------------------

1. Create a JSON file with the prefix ``Fx_`` somewhere in your project.

   - If you want to modify the English language file: ``Fx_en.json``.
   - If you want to create a new language file: ``Fx_[language].json``.

   If you want to create a French language file, the file name could be ``Fx_fr.json``.

2. Search the :ref:`language files <language>` and find keys you want to override.

   - Include any keys that you want to override in your JSON file.

3. Pass the language string into :meth:`~fxstcloud.bot.Bot` to set your language.

.. code-block:: python

   bot = fxstcloud.Bot(language="fr")  # French (loaded from Fx_fr.json)

If your bot supports **multiple languages**, set ``language`` to ``auto`` to
automatically detect the language. You can set a fallback language with ``default_language``.

The fallback language is used when no language file is found for the detected language.

.. code-block:: python

   bot = fxstcloud.Bot(language="auto", default_language="en")


.. _language:

Language files
--------------

.. literalinclude:: ../../fxstcloud/internal/language/en.json
   :language: python
   :caption: The default language file for English.

.. literalinclude:: ../../fxstcloud/internal/language/de.json
   :language: python
   :caption: The default language file for German.
