HASH_MODULUS = 1_000_000_007


def deepHash(obj, seen):
    if obj is None or isinstance(obj, (bool, int, float, str)):
        return hash(obj) % HASH_MODULUS

    objId = id(obj)
    if objId in seen:
        return 131
    # seen maps ids to the objects themselves rather than being a set of ids.
    # Holding a reference keeps each object alive until hashing finishes.
    # Otherwise a temporary object, like a (key, value) tuple from
    # dict.items(), could be freed and have its id reused by a different
    # object, which would then be wrongly skipped as already seen.
    seen[objId] = obj

    if isinstance(obj, (list, tuple)):
        values = obj
    elif isinstance(obj, set):
        values = sorted(obj, key=id)
    elif isinstance(obj, dict):
        values = list(obj.items())
    elif hasattr(obj, '__dict__'):
        return deepHash(vars(obj), seen)
    else:
        return deepHash(repr(obj), seen)

    result = 0
    for value in values:
        result = (result * 31 + deepHash(value, seen)) % HASH_MODULUS
    return result


def appHash(wrapper, stateHashAttrs):
    seen = {}
    items = [(k, v) for k, v in vars(wrapper).items() if k != '_app']
    items += [(attr, getattr(wrapper, attr, None)) for attr in stateHashAttrs]

    result = 0
    for name, value in sorted(items, key=lambda kv: kv[0]):
        result = (result * 31 + deepHash(name, seen)) % HASH_MODULUS
        result = (result * 31 + deepHash(value, seen)) % HASH_MODULUS
    return result
