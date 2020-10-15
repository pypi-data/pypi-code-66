from thinc.api import fix_random_seed
from spacy.lang.en import English
from spacy.tokens import Span
from spacy import displacy
from spacy.pipeline import merge_entities


def test_issue5551():
    """Test that after fixing the random seed, the results of the pipeline are truly identical"""
    component = "textcat"
    pipe_cfg = {
        "model": {
            "@architectures": "spacy.TextCatBOW.v1",
            "exclusive_classes": True,
            "ngram_size": 2,
            "no_output_layer": False,
        }
    }
    results = []
    for i in range(3):
        fix_random_seed(0)
        nlp = English()
        example = (
            "Once hot, form ping-pong-ball-sized balls of the mixture, each weighing roughly 25 g.",
            {"cats": {"Labe1": 1.0, "Label2": 0.0, "Label3": 0.0}},
        )
        pipe = nlp.add_pipe(component, config=pipe_cfg, last=True)
        for label in set(example[1]["cats"]):
            pipe.add_label(label)
        nlp.initialize()
        # Store the result of each iteration
        result = pipe.model.predict([nlp.make_doc(example[0])])
        results.append(list(result[0]))
    # All results should be the same because of the fixed seed
    assert len(results) == 3
    assert results[0] == results[1]
    assert results[0] == results[2]


def test_issue5838():
    # Displacy's EntityRenderer break line
    # not working after last entity
    sample_text = "First line\nSecond line, with ent\nThird line\nFourth line\n"
    nlp = English()
    doc = nlp(sample_text)
    doc.ents = [Span(doc, 7, 8, label="test")]
    html = displacy.render(doc, style="ent")
    found = html.count("</br>")
    assert found == 4


def test_issue5918():
    # Test edge case when merging entities.
    nlp = English()
    ruler = nlp.add_pipe("entity_ruler")
    patterns = [
        {"label": "ORG", "pattern": "Digicon Inc"},
        {"label": "ORG", "pattern": "Rotan Mosle Inc's"},
        {"label": "ORG", "pattern": "Rotan Mosle Technology Partners Ltd"},
    ]
    ruler.add_patterns(patterns)

    text = """
        Digicon Inc said it has completed the previously-announced disposition
        of its computer systems division to an investment group led by
        Rotan Mosle Inc's Rotan Mosle Technology Partners Ltd affiliate.
        """
    doc = nlp(text)
    assert len(doc.ents) == 3
    # make it so that the third span's head is within the entity (ent_iob=I)
    # bug #5918 would wrongly transfer that I to the full entity, resulting in 2 instead of 3 final ents.
    # TODO: test for logging here
    # with pytest.warns(UserWarning):
    #     doc[29].head = doc[33]
    doc = merge_entities(doc)
    assert len(doc.ents) == 3
