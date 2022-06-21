import pytest
import os
from datetime import datetime


def pytest_addoption(parser):
    parser.addoption("--envs", action="store", default="prod")
    parser.addoption("--is_headless", action="store", default=True)


@pytest.fixture
def envs(request):
    return request.config.getoption("--envs")


@pytest.fixture
def is_headless(request):
    return request.config.getoption("--is_headless")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    test_fn = item.obj
    docstring = getattr(test_fn, '__doc__')
    if docstring:
        report.nodeid = docstring

    if "incremental" in item.keywords:
        if call.excinfo is not None:
            parent = item.parent
            parent._previousfailed = item


def pytest_runtest_setup(item):
    previousfailed = getattr(item.parent, "_previousfailed", None)
    if previousfailed is not None:
        pytest.xfail("previous test failed (%s)" % previousfailed.name)
