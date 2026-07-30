from behavior import current_behavior


def test_behavior_stays_safe():
    assert current_behavior() == "safe"
