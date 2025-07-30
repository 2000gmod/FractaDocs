Data bindings
=============

Fracta has variable declarations in the form of **Data Bindings**. 
They are similar to what other languages call variables.

They are declared with the ``var`` and ``const`` keywords. Any data binding is local to the scope it's defined in, and any inner scope.

.. code-block:: fracta
    :linenos:
    :caption: Example (errors are highlighted)
    :emphasize-lines: 3, 6, 8

    func Main() void {
        var local1 f32 = 0.0f;  // floating point type
        const local2 i32;       // error, no initializer

        const local3 auto = 5;  // local3 is inferred to be of type 'i32'
        const local4 auto;      // error, no initializer, can't infer type

        local3 += 1;            // error, local3 is a const binding.
    }


Data bindings declared with the ``const`` keyword can't have their values changed
after initialization, and may be optimized out by the compiler.

Variable bindings will default to zero-initialization of their storage unless given an initializer.
Constant bindings need an initializer (no default-init constants).

Mutable references may only point to variable bindings (``var`` keyword).

Global data bindings are **not** legal in Fracta.



Syntax
-------

``(var|const) identifier (T|auto) [= E]``.

Where T is a type expression, and E is an expression used as an initializer. If the binding is declared as constant **or** if it uses type inference (``auto``),
**an initializer expression is required**.