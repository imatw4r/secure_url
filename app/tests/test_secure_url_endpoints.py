from models import SecureUrl


def test():
    print(SecureUrl.objects.all())
    assert False