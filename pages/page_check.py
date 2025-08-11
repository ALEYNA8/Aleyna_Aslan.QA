# The career_page_check function collectively checks the visibility of important sections on the CareerPage using assert.
def career_page_check(career_page):
    assert career_page.is_our_locations_visible(), "'Our Locations' section not visible!"
    assert career_page.is_teams_section_visible(), "'Teams' section not visible!"
    assert career_page.is_life_at_insider_visible(), "'Life at Insider' section not visible!"

# The home_page_check function performs basic page checks on the HomePage.
def home_page_check(home_page):
    assert home_page.is_on_home_page(), "Not on home page!"

