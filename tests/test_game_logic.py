from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_hint_messages_are_not_swapped():
    # Regression test: when guess is too high, message must say LOWER (not HIGHER)
    # and when guess is too low, message must say HIGHER (not LOWER)
    _, high_msg = check_guess(60, 50)
    assert "LOWER" in high_msg, f"Expected 'LOWER' when guess is too high, got: {high_msg}"

    _, low_msg = check_guess(40, 50)
    assert "HIGHER" in low_msg, f"Expected 'HIGHER' when guess is too low, got: {low_msg}"

def test_guess_one_above_secret():
    # Guess is just 1 above secret — should still say Too High / Go LOWER
    outcome, msg = check_guess(51, 50)
    assert outcome == "Too High"
    assert "LOWER" in msg

def test_guess_one_below_secret():
    # Guess is just 1 below secret — should still say Too Low / Go HIGHER
    outcome, msg = check_guess(49, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in msg

def test_secret_at_minimum():
    # Secret is 1 (lowest possible), any higher guess should say Too High
    outcome, msg = check_guess(2, 1)
    assert outcome == "Too High"
    assert "LOWER" in msg

def test_secret_at_maximum():
    # Secret is 100 (highest possible), any lower guess should say Too Low
    outcome, msg = check_guess(99, 100)
    assert outcome == "Too Low"
    assert "HIGHER" in msg

def test_guess_far_below_secret():
    # Guess is 1, secret is 100 — extreme low
    outcome, msg = check_guess(1, 100)
    assert outcome == "Too Low"
    assert "HIGHER" in msg

def test_guess_far_above_secret():
    # Guess is 100, secret is 1 — extreme high
    outcome, msg = check_guess(100, 1)
    assert outcome == "Too High"
    assert "LOWER" in msg
