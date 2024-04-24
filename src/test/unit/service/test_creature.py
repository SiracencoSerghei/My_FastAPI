from src.fake.creature import _creatures


from src.model.creature import Creature
from src.service import creature as code

# sample = [creature for creature in _creatures if creature.name == "Yeti"]
sample = Creature(name="Yeti",
        country="CN",
        area="Himalayas",
        description="Hirsute Himalayan",
        aka="Abominable Snowman",
        )

def test_create():
    resp = code.create(sample)
    assert resp == sample


def test_get_exists():
    resp = code.get_one("Yeti")
    # assert resp == sample[0]
    assert resp == sample

def test_get_missing():
    resp = code.get_one("boxturtle")
    assert resp is None
