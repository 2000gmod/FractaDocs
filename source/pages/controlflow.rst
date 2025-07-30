Control Flow
============

Fracta has support for  several program control flow structures. 

Conditionals
------------

If and else
^^^^^^^^^^^

Fracta supports basic conditional control flow in the form of the ``if`` statement.

.. code-block:: fracta
    :linenos:

    const condition bool = SomeCondition();

    if condition {
        println("Inside the if branch.");
    }
    else {
        println("Inside the else branch.");
    }

The argument for the ``if`` statement must always evaluate to the ``bool`` type.


You may also chain several ``if`` and ``else`` statements together:

.. code-block:: fracta
    :linenos:

    const i i32 = GetRandomNumber() % 10; // i is a random number in the range [0, 9].

    if i < 5 {
        println("i is less than 5");
    }
    else if i <= 7 {
        println("i is between 5 and 7")
    }
    else {
        println("i is either 8 or 9");
    }

As you can see, the comparison operators for the default types evaluate to the ``bool`` type, allowing their usage in conditional logic.


Switch
^^^^^^

You may use ``switch`` statements to branch on a integer value or variant field.

.. code-block:: fracta
    :linenos:
    :caption: Switching on an integer.

    const i i32 = GetRandomNumber() % 10; // i is a random number in the range [0, 9].

    switch i {
        case 0: println("i is 0!"); // single statement case.
        case 1: { 
            println("i is 1!"); // multiple statement case.
            println("Interesting...");
        }
        default: { // executes if every other branch fails to match.
            println("i may be something else...");
        }
    }


.. code-block:: fracta
    :linenos:
    :caption: Switching on an variant.

    import std::io { println, printf };

    type DivisionResult {
        layout variant {
            Error,
            Valid { result f64; }
        }
    }

    func Divide(a f64, b f64) DivisionResult {
        if b == 0.0 {
            return DivisionResult::Error;
        }
        return DivisionResult::Valid { result = a / b };
    }

    func Main() i32 {
        const result = Divide(1.0, 0.0);

        switch result {
            case Error: {
                println("Divided by 0!");
            }
            case Valid obj: {
                printf("The result of the division is: %f\n", obj.result);
            }
        }

        return 0;
    }

Loops
-----

Fracta has support for both ``while`` (condition based) and ``for`` (iterator based) loops.


While loop
^^^^^^^^^^