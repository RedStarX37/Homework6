import os
from file_manager import view_creator, view_os_info


def test_mkdir():
    os.mkdir('test_folder')
    assert 'test_folder' in os.listdir()
    os.rmdir('test_folder')


def test_view_os():
    assert view_creator == 'm01-rimmel'


def test_view_creator():
    assert view_creator == 'win32'