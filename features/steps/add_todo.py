from main import add_todo, list_todos
from behave import given, when, then


@given("I create a new empty ToDo list")
def step_impl(context):
    pass


@when("I add a Todo {text}")
def step_impl(context, text):
    context.todo = add_todo(text)


@then("I should see the ToDo in the list")
def step_impl(context):
    assert list_todos()[0]["text"] == '"Comprar pan"'
