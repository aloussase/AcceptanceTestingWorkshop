from main import add_todo, list_todos, mark_complete
from behave import given, when, then


@given("I have a ToDo {text}")
def step_impl(context, text):
    add_todo(text)


@when("I complete the ToDo")
def step_impl(context):
    todo_id = list_todos()[0]['id']
    mark_complete(todo_id)


@then("the ToDo is marked as complete")
def step_impl(context):
    assert list_todos()[0]["completed"] == True
