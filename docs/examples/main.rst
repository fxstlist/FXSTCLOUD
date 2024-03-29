Main Example
=======================
You can create your bot by using the :doc:`fxstcloud.Bot </fxstcloud/bot>` class.

.. hint::
    If you are using Pycord with Prefix commands, use ``fxstcloud.PrefixBot`` instead.

- You can load all of your cogs at once with :meth:`~fxstcloud.bot.Bot.load_cogs`.
- If you pass in a webhook URL, errors will be sent to that webhook.
- You can set the language for user messages, for example if an application command error occurs.
- A custom on_ready message will be printed, unless you set ``ready_event=None``.

.. literalinclude:: ../../examples/pycord.py
   :language: python
   :caption: Pycord

.. literalinclude:: ../../examples/dpy.py
   :language: python
   :caption: Discord.py
