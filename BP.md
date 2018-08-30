# Python best practices
This project will be creating following these practices

### Values

    - "Build tools for others that you want to be built for you." - Kenneth Reitz
    - "Simplicity is alway better than functionality." - Pieter Hintjens
    - "Fit the 90% use-case. Ignore the nay sayers." - Kenneth Reitz
    - "Beautiful is better than ugly." - [PEP 20][]
    - Build for open source (even for closed source projects).

### General Development Guidelines

    - "Explicit is better than implicit" - [PEP 20][]
    - "Readability counts." - [PEP 20][]
    - "Anybody can fix anything." - [Khan Academy Development Docs][]
    - Fix each [broken window](http://www.artima.com/intv/fixit2.html) (bad design, wrong decision, or poor code) *as soon as it is discovered*.
    - "Now is better than never." - [PEP 20][]
    - Test ruthlessly. Write docs for new features.
    - Even more important that Test-Driven Development--*Human-Driven Development*
    - These guidelines may--and probably will--change.

#### Naming

- Variables, functions, methods, packages, modules
    - `lower_case_with_underscores`
- Classes and Exceptions
    - `CapWords`
- Protected methods and internal functions
    - `_single_leading_underscore(self, ...)`
- Private methods
    - `__double_leading_underscore(self, ...)`
- Constants
    - `ALL_CAPS_WITH_UNDERSCORES`

Avoid getter and setter methods.

**Yes**
```python
person.age = 42
```

**No**
```python
person.set_age(42)
```
#### Imports

Import entire modules instead of individual symbols within a module. For example, for a top-level module `canteen` that has a file `canteen/sessions.py`,

**Yes**

```python
import canteen
import canteen.sessions
from canteen import sessions
```

**No**

```python
from canteen import get_user  # Symbol from canteen/__init__.py
from canteen.sessions import get_session  # Symbol from canteen/sessions.py
```

#### Documentation

Use one-line docstrings for obvious functions.

```python
"""Return the pathname of ``foo``."""
```

Multiline docstrings should include

- Summary line
- Use case, if appropriate
- Args
- Return type and semantics, unless ``None`` is returned

- Use action words ("Return") rather than descriptions ("Returns").
- Document `__init__` methods in the docstring for the class.

```python
class Person(object):
    """A simple representation of a human being.

    :param name: A string, the person's name.
    :param age: An int, the person's age.
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

##### On comments

Use them sparingly. Prefer code readability to writing a lot of comments. Often, small methods are more effective than comments.

*No*

```python
# If the sign is a stop sign
if sign.color == 'red' and sign.sides == 8:
    stop()
```

*Yes*

```python
def is_stop_sign(sign):
    return sign.color == 'red' and sign.sides == 8

if is_stop_sign(sign):
    stop()
```

### Testing

Strive for 100% code coverage, but don't get obsess over the coverage score.

#### General testing guidelines

- Use long, descriptive names. This often obviates the need for doctrings in test methods.
- Tests should be isolated. Don't interact with a real database or network. Use a separate test database that gets torn down or use mock objects.
- Prefer [factories](https://github.com/rbarrois/factory_boy) to fixtures.
- Never let incomplete tests pass, else you run the risk of forgetting about them. Instead, add a placeholder like `assert False, "TODO: finish me"`.

#### Unit Tests

- Focus on one tiny bit of functionality.
- Should be fast, but a slow test is better than no test.
- It often makes sense to have one testcase class for a single class or model.