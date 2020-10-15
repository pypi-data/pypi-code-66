import pytest


def test_el_tokenizer_handles_long_text(el_tokenizer):
    text = """Η Ελλάδα (παλαιότερα Ελλάς), επίσημα γνωστή ως Ελληνική Δημοκρατία,\
    είναι χώρα της νοτιοανατολικής Ευρώπης στο νοτιότερο άκρο της Βαλκανικής χερσονήσου.\
    Συνορεύει στα βορειοδυτικά με την Αλβανία, στα βόρεια με την πρώην\
    Γιουγκοσλαβική Δημοκρατία της Μακεδονίας και τη Βουλγαρία και στα βορειοανατολικά με την Τουρκία."""
    tokens = el_tokenizer(text)
    assert len(tokens) == 54


@pytest.mark.parametrize(
    "text,length",
    [
        ("Διοικητικά η Ελλάδα διαιρείται σε 13 Περιφέρειες.", 8),
        ("Η εκπαίδευση στην Ελλάδα χωρίζεται κυρίως σε τρία επίπεδα.", 10),
        (
            "Η Ελλάδα είναι μία από τις χώρες της Ευρωπαϊκής Ένωσης (ΕΕ) που διαθέτει σηµαντικό ορυκτό πλούτο.",
            19,
        ),
        (
            "Η ναυτιλία αποτέλεσε ένα σημαντικό στοιχείο της Ελληνικής οικονομικής δραστηριότητας από τα αρχαία χρόνια.",
            15,
        ),
        ("Η Ελλάδα είναι μέλος σε αρκετούς διεθνείς οργανισμούς.", 9),
    ],
)
def test_el_tokenizer_handles_cnts(el_tokenizer, text, length):
    tokens = el_tokenizer(text)
    assert len(tokens) == length
