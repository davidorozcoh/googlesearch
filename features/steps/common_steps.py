from behave import step
from hamcrest import *
from utils.data_objects import *
from utils.page import Page


# common step search for a word in googlesearch

@step("I’m on the {homepage}")
def step_impl(context, homepage):
    context.section = homepage
    Page(context).open(dataElements[context.section]['url'])


@step("I type {input} into the search {web_element}")
def write_box(context, input, web_element):
    selector = dataElements[context.section][web_element]['selector']
    element = dataElements[context.section][web_element][selector]
    Page(context).fill(selector, element, input)
    Page(context).explicitWait(selector, element, 6)


@step('I click the Google {search} button')
def click_on(context, search):
    selector = dataElements[context.section][search]['selector']
    element = dataElements[context.section][search][selector]
    Page.explicitWait(context, selector, element, 5)
    Page(context).click(selector, element)


@step("I go to the search results page, and the first 3 results contain the word {result}")
def system_shows_message(context, result):
    check_message(context, result)


@step("I Search {input} by keyword in {web_element}")
def enter_result(context, input, web_element):
    write_box(context, input, web_element)


@step("I click on the first {result} link")
def result_link(context, search, result):
    click_on(context, search)
    selector = dataElements[context.section][result]['selector']
    element = dataElements[context.section][result][selector]
    Page.explicitWait(context, selector, element, 5)
    Page(context).click(selector, element)


@step("I go to the page, and the page title contains the word {link_text}")
def message(context, link_text):
    check_message(context, link_text)


# End common step googlesearch


@step("The user should see an {type_message} Message")
def check_message(context, type_message):
    message_expected = dataElements(context)[context.section][(type_message + "Message")]['text']
    selector = dataElements(context)[context.section][type_message + "Message"]['selector']
    element = dataElements(context)[context.section][type_message + "Message"][selector]
    Page.explicitWait(context, selector, element, 10)
    message_got = Page(context).getText(selector, element)
    assert_that(message_got, equal_to(message_expected))
