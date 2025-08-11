def career_page_check(career_page):
    assert career_page.is_our_locations_visible(), "'Our Locations' section not visible!"
    assert career_page.is_teams_section_visible(), "'Teams' section not visible!"
    assert career_page.is_life_at_insider_visible(), "'Life at Insider' section not visible!"

def home_page_check(home_page):
    assert home_page.is_on_home_page(), "Not on home page!"
    # Gerekirse burada HomePage'in diğer kontrollerini de ekleyebilirsin.
