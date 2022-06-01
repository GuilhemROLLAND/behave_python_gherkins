from re import X
from tkinter import Y
from behave import *

from Calculator import Calculator

x = 0
y = 0
sum = 0

tab_x = []
tab_y = []
tab_sum = []


@given(u'set x = {int}')
def step_impl(context, int):
    global x
    x = int


@given(u'set y = {int}')
def step_impl(context, int):
    global y
    y = int


@when(u'add x and y')
def step_impl(context):
    global sum, x, Y
    sum = Calculator.add(x, y)


@then(u'result must be equal to {val}')
def step_impl(context, val):
    global sum
    assert int(sum) == int(val)


@given(u'a set of values')
def step_impl(context):
    global tab_y, tab_sum, tab_x
    for row in context.table:
        tab_x.append(row['x'])
        tab_y.append(row['y'])


@when(u'add the values')
def step_impl(context):
    global tab_y, tab_sum, tab_x
    for i in range(len(tab_x)):
        tab_sum.append(Calculator.add(tab_x[i], tab_y[i]))


@then(u'result must be correct')
def step_impl(context):
    global tab_sum
    tab_sum_from_behave = []
    for row in context.table:
        tab_sum_from_behave.append(row['result'])
    for i in range(len(tab_x)):
        assert int(tab_sum[i]) == int(tab_sum_from_behave[i])
