import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.app import App  # noqa: E501
from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.new_app import NewApp  # noqa: E501
from openapi_server import util

app_list=[App(name='app1',tag='tag1',app_id=1),App(name='app2',tag='tag2',app_id=2)]

def add_app(new_app= None):  # noqa: E501
    """add_app

    Creates a new App in the store. Duplicates are allowed # noqa: E501

    :param new_app: App to add to the store
    :type new_app: dict | bytes

    :rtype: Union[App, Tuple[App, int], Tuple[App, int, Dict[str, str]]
    """
    return "stuff"
    if connexion.request.is_json:
        new_app = NewApp.from_dict(connexion.request.get_json())  # noqa: E501
    added_app = App(name=new_app.name(),tag=new_app.tag(), app_id=len(app_list))
    app_list.append(added_app )
    return [added_app,202]


def delete_app(app_id):  # noqa: E501
    """delete_app

    deletes a single App based on the ID supplied # noqa: E501

    :param id: ID of App to delete
    :type id: int

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    for item in app_list:
        if item.app_id == app_id:
            app_list.remove(item)
            return [None,204]
    return None


def find_app_by_id(app_id):  # noqa: E501
    """find_app_by_id

    Returns a user based on a single ID, if the user does not have access to the App # noqa: E501

    :param id: ID of App to fetch
    :type id: int

    :rtype: Union[App, Tuple[App, int], Tuple[App, int, Dict[str, str]]
    """
    for item in app_list:
        if item.app_id == app_id:
            return [item,200]
    return [App(),202]


def find_apps(tags=None, limit=None):  # noqa: E501
    """find_apps

    Returns all Apps from the system that the user has access to Write more documentation here And here!  # noqa: E501

    :param tags: tags to filter by
    :type tags: List[str]
    :param limit: maximum number of results to return
    :type limit: int

    :rtype: Union[List[App], Tuple[List[App], int], Tuple[List[App], int, Dict[str, str]]
    """
    tmplist=[]
    for tag in tags:
        for app in app_list:
            if tag == app.tag:
                tmplist.append(app)
    return tmplist
