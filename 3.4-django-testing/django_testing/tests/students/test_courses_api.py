import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from students.models import Course, Student


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


@pytest.mark.django_db
def test_get_course(client, course_factory):
    course = course_factory(_quantity=1)
    response = client.get('/api/v1/courses/' + str(course[0].id) + '/')
    assert response.status_code == 200
    data = response.json()
    assert data['name'] == course[0].name


@pytest.mark.django_db
def test_get_course_list(client, course_factory):
    courses = course_factory(_quantity=10)
    response = client.get('/api/v1/courses/')
    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(courses)
    for i, course in enumerate(data):
        assert course['name'] == courses[i].name


@pytest.mark.django_db
def test_get_course_by_id(client, course_factory):
    courses = course_factory(_quantity=10)
    test_course_id = 2
    response = client.get('/api/v1/courses/', {'id': courses[test_course_id].id})
    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] == courses[test_course_id].name


@pytest.mark.django_db
def test_get_course_by_name(client, course_factory):
    courses = course_factory(_quantity=10)
    test_course_id = 2
    response = client.get('/api/v1/courses/', {'name': courses[test_course_id].name})
    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] == courses[test_course_id].name


@pytest.mark.django_db
def test_create_course(client):
    response = client.post('/api/v1/courses/', data={'name': 'test_course', })
    assert response.status_code == 201
    data = response.json()
    assert data['name'] == 'test_course'


@pytest.mark.django_db
def test_patch_course(client, course_factory):
    course = course_factory(_quantity=1)
    old_name = course[0].name
    response = client.patch('/api/v1/courses/' + str(course[0].id) + '/', data={'name': old_name + 'new_name'})
    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] != old_name
    assert data[0]['name'] == old_name + 'new_name'


@pytest.mark.django_db
def test_patch_course(client, course_factory):
    course = course_factory(_quantity=1)
    response = client.delete('/api/v1/courses/' + str(course[0].id) + '/')
    assert response.status_code == 204
