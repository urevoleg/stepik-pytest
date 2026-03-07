# tests/test_profile.py
import pytest


# НЕТ ИМПОРТОВ ИЗ CONFTEST

@pytest.mark.profile
def test_profile_page_for_admin(admin_user):
    """
    Проверяет, что у пользователя, полученного из фикстуры,
    есть доступ к админским настройкам профиля.
    """
    assert admin_user.name == "Admin"
    assert admin_user.is_admin()