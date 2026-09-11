""" 
Point                     Instance Method           Class Method             Static Method
=====                     ================          ============             =============
Decorator                 No decorator              @classmethod             @staticmethod
First parameter           self                      cls                      No automatic parameter
Receives Object           Class                     Nothing                  automatically
Access instance data      Yes                       No                       direct access No
Access class data         Yes                       Yes                      No direct access
Common use                Object behavior           Class-level behavior     Helper logic
Call style                obj.method()              Class.method()           Class.method()

"""