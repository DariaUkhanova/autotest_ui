from playwright.sync_api import sync_playwright, expect
import pytest


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state):

        chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        title_text = chromium_page_with_state.get_by_test_id("courses-list-toolbar-title-text")
        expect(title_text).to_be_visible()

        folder_icon = chromium_page_with_state.get_by_test_id("courses-list-empty-view-icon")
        expect(folder_icon).to_be_visible()

        empty_results_text = chromium_page_with_state.get_by_test_id("courses-list-empty-view-title-text")
        expect(empty_results_text).to_be_visible()

        empty_result_description = chromium_page_with_state.get_by_test_id("courses-list-empty-view-description-text")
        expect(empty_result_description).to_be_visible()

