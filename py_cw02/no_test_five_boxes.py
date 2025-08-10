from five_boxes import heaviest_box

def test_heavy01():
    heaviestBox = heaviest_box
    # heaviestBox([113,116,110,117,112,118,114,121,120,115]) == 62
    assert heaviestBox([113,116,110,117,112,118,114,121,120,115]) == 62
    assert heaviestBox([143, 158, 123, 115, 108, 171, 151, 143, 136, 128]) == 93
    assert heaviestBox([156, 147, 119, 135, 180, 152, 123, 168, 140, 164]) ==  96
