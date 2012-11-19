import inspect
import imp

def is_subclass(subklass, klass, exclude_identity=True):

    return inspect.isclass(subklass) and issubclass(subklass, klass) and (subklass is not klass and exclude_identity or not exclude_identity)

def is_instance(main_klass, klass):

    return isinstance(main_klass, klass)

def load_module(name, path=None):

    fp, pathname, description = imp.find_module(name, [path, ])
    return imp.load_module(name, fp, pathname, description)