# bastard
A Python 2.x module that allows a sub class to know its parent class

---

The contained decorator `bastard.recognized`, when used on a sub class, allows to replace the usual

    super(cls, self).some_method()

with the hopefully easier to understand

    self.parent.some_method()

Additionally, there's a further decorator, `bastard.recognizer`, that expects the to-be-used name of the parent as argument.

---

Thus, one can do stuff like this:

```python
class Roose(object):
    lastname = "Bolton"
    recognize = recognizer("father")

class Ramsay(Roose):
    lastname = "Snow"
    def __init__(self):
        if hasattr(self, "father"):
            self.lastname = self.father.lastname

print "Before recognition:", Ramsay().lastname # Will be: Snow
Ramsay = Roose.recognize(Ramsay)
print "After recognition: ", Ramsay().lastname # Will be: Bolton
```

...but it's better to see the enclosed [example](example.py) for how to use the module.

---

Note that this will probably not be very useful in Python 3.x code...

