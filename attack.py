from element_table import ElementalTable


def attack(
        damage,
        atk_elem: ElementalTable,
        def_elem: ElementalTable,
):
    return damage * def_elem[atk_elem.attack] / 100
