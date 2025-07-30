Hello World
===========

The classic ``Hello, world!`` program in Fracta is relatively easy to understand.

.. code-block:: fracta
    :linenos:
    :caption: Hello world program in Fracta

    import std::io { println };

    func Main() void {
        println("Hello, world!");
    }

.. code-block:: shell
    :caption: Expected output

    Hello, world!


We can already see some features in Fracta, like the selective ``import`` statement. 
Execution starts at the ``Main`` function, as expected of procedural systems languages.