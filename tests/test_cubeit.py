from playwright.sync_api import Page, expect

BASE_URL = "http://127.0.0.1:8000"

def test_cubeit(page:Page):
    page.goto(BASE_URL)

    cube_btn = page.get_by_role("button", name="Cube")
    input_num_field = page.get_by_placeholder("enter number...")

    input_num_field.fill("3")
    cube_btn.click()

    result = page.locator("#result")
    expect(result).to_contain_text("27")


def test_empty_input(page:Page):
    page.goto(BASE_URL)

    cube_btn = page.get_by_role("button", name="Cube")
    input_num_field = page.get_by_placeholder("enter number...")

    input_num_field.fill("")
    cube_btn.click()

    result = page.locator("#result")
    expect(result).to_contain_text("Enter something!")
