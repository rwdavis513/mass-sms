from app.main import main, get_phone_list


def test_get_phone_list():
    phone_list = get_phone_list()
    assert isinstance(phone_list, list)


def test_main():

    main()