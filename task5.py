from task4 import app

def test_header_present(dash_duo):
    dash_duo.start_server(app)
    header = dash_duo.find_element("h1")
    assert header is not None
    assert "Soul Foods Pink Morsel Sales Visualiser" in header.text

def test_visualisation_present(dash_duo):
    dash_duo.start_server(app)
    graph = dash_duo.find_element("#sales-line-chart")
    assert graph is not None

def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)
    radio_items = dash_duo.find_element("#region-filter")
    assert radio_items is not None
    labels = dash_duo.find_elements("label")
    label_texts = [label.text for label in labels]

    assert "All" in label_texts
    assert "North" in label_texts
    assert "East" in label_texts
    assert "South" in label_texts
    assert "West" in label_texts