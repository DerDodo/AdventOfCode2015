import random
from enum import Enum
from typing import List, Tuple

from file_util import read_input_file


class Spell(Enum):
    MagicMissile = 53
    Drain = 73
    Shield = 113
    Poison = 173
    Recharge = 229


class Boss:
    hp: int
    damage: int

    def __init__(self, lines: List[str]):
        self.hp = int(lines[0].split(" ")[-1])
        self.damage = int(lines[1].split(" ")[-1])


class Wizard:
    hp: int
    mana: int
    mana_used: int
    hard_mode: bool

    poison_rounds_left: int
    shield_rounds_left: int
    recharge_rounds_left: int

    def __init__(self, hp: int, mana: int, strategy, hard_mode: bool):
        self.hp = hp
        self.mana = mana
        self.strategy = strategy
        self.hard_mode = hard_mode
        self.mana_used = 0

        self.poison_rounds_left = 0
        self.shield_rounds_left = 0
        self.recharge_rounds_left = 0

    def battle(self, boss: Boss) -> bool:
        for _ in range(1000):
            result = self.take_turn(boss)
            if result is not None:
                return result

            result = self.boss_turn(boss)
            if result is not None:
                return result

        return False

    def take_turn(self, boss) -> bool | None:
        if self.hard_mode:
            self.hp -= 1
            if self.hp <= 0:
                return False

        self.apply_lasting_effects(boss)
        if self.mana < 53:
            return False

        spell = self.strategy(self, boss)
        if not self.can_use(spell):
            raise ValueError(f"Cannot use spell {spell}")

        self.cast(spell, boss)

        if boss.hp <= 0:
            return True

    def boss_turn(self, boss: Boss):
        self.apply_lasting_effects(boss)

        if boss.hp <= 0:
            return True

        shield = 7 if self.shield_rounds_left > 0 else 0
        damage = max(1, boss.damage - shield)
        self.hp -= damage

        if self.hp <= 0:
            return False

    def apply_lasting_effects(self, boss: Boss):
        if self.poison_rounds_left > 0:
            self.poison_rounds_left -= 1
            boss.hp -= 3

        if self.recharge_rounds_left > 0:
            self.recharge_rounds_left -= 1
            self.mana += 101

        if self.shield_rounds_left > 0:
            self.shield_rounds_left -= 1

    def can_use(self, spell: Spell) -> bool:
        if spell == Spell.Poison and self.poison_rounds_left > 0:
            return False

        if spell == Spell.Shield and self.shield_rounds_left > 0:
            return False

        if spell == Spell.Recharge and self.recharge_rounds_left > 0:
            return False

        if self.mana < spell.value:
            return False

        return True

    def cast(self, spell: Spell, boss: Boss):
        self.mana -= spell.value
        self.mana_used += spell.value
        if spell == Spell.MagicMissile:
            self.cast_magic_missile(boss)
        elif spell == Spell.Drain:
            self.cast_drain(boss)
        elif spell == Spell.Poison:
            self.cast_poison()
        elif spell == Spell.Shield:
            self.cast_shield()
        elif spell == Spell.Recharge:
            self.cast_recharge()

    @staticmethod
    def cast_magic_missile(boss):
        boss.hp -= 4

    def cast_drain(self, boss):
        self.hp += 2
        boss.hp -= 2

    def cast_poison(self):
        self.poison_rounds_left = 6

    def cast_shield(self):
        self.shield_rounds_left = 6

    def cast_recharge(self):
        self.recharge_rounds_left = 5

    def get_available_spells(self) -> List[Spell]:
        available_spells = []

        for spell in list(Spell):
            can_poison = spell != Spell.Poison or self.poison_rounds_left == 0
            can_shield = spell != Spell.Shield or self.shield_rounds_left == 0
            can_recharge = spell != Spell.Recharge or self.recharge_rounds_left == 0
            if self.mana >= spell.value and can_poison and can_shield and can_recharge:
                available_spells.append(spell)

        if len(available_spells) == 0:
            raise ValueError(f"Cannot cast any spell!, mana: {self.mana}")
        return available_spells


def strategy_1_random(wizard: Wizard, _: Boss) -> Spell:
    available_spells = wizard.get_available_spells()
    return random.choice(available_spells)


def strategy_by_priority(wizard: Wizard, strategy: List[Spell]) -> Spell:
    available_spells = wizard.get_available_spells()
    for spell in strategy:
        if spell in available_spells:
            return spell
    return random.choice(available_spells)


def strategy_2_psr(wizard: Wizard, _: Boss) -> Spell:
    return strategy_by_priority(wizard, [Spell.Poison, Spell.Shield, Spell.Recharge])


def strategy_2_prs(wizard: Wizard, _: Boss) -> Spell:
    return strategy_by_priority(wizard, [Spell.Poison, Spell.Recharge, Spell.Shield])


def strategy_2_spr(wizard: Wizard, _: Boss) -> Spell:
    return strategy_by_priority(wizard, [Spell.Shield, Spell.Poison, Spell.Recharge])


def strategy_2_srp(wizard: Wizard, _: Boss) -> Spell:
    return strategy_by_priority(wizard, [Spell.Shield, Spell.Recharge, Spell.Poison])


def strategy_2_rps(wizard: Wizard, _: Boss) -> Spell:
    return strategy_by_priority(wizard, [Spell.Recharge, Spell.Poison, Spell.Shield])


def strategy_2_rsp(wizard: Wizard, _: Boss) -> Spell:
    return strategy_by_priority(wizard, [Spell.Recharge, Spell.Shield, Spell.Poison])


def strategy_2_rs(wizard: Wizard, _: Boss) -> Spell:
    return strategy_by_priority(wizard, [Spell.Recharge, Spell.Shield])


def strategy_2_sr(wizard: Wizard, _: Boss) -> Spell:
    return strategy_by_priority(wizard, [Spell.Shield, Spell.Recharge])


def strategy_2_ps(wizard: Wizard, _: Boss) -> Spell:
    return strategy_by_priority(wizard, [Spell.Poison, Spell.Shield])


def strategy_2_sp(wizard: Wizard, _: Boss) -> Spell:
    return strategy_by_priority(wizard, [Spell.Shield, Spell.Poison])


def strategy_2_pr(wizard: Wizard, _: Boss) -> Spell:
    return strategy_by_priority(wizard, [Spell.Poison, Spell.Recharge])


def strategy_2_rp(wizard: Wizard, _: Boss) -> Spell:
    return strategy_by_priority(wizard, [Spell.Recharge, Spell.Poison])


def strategy_2_s(wizard: Wizard, _: Boss) -> Spell:
    return strategy_by_priority(wizard, [Spell.Shield])


def strategy_2_p(wizard: Wizard, _: Boss) -> Spell:
    return strategy_by_priority(wizard, [Spell.Poison])


def strategy_2_r(wizard: Wizard, _: Boss) -> Spell:
    return strategy_by_priority(wizard, [Spell.Recharge])


def strategy_3_magic_missile(wizard: Wizard, _: Boss) -> Spell:
    return strategy_by_priority(wizard, [Spell.Shield, Spell.MagicMissile])


def strategy_3_drain(wizard: Wizard, _: Boss) -> Spell:
    return strategy_by_priority(wizard, [Spell.Shield, Spell.Drain, Spell.MagicMissile])


def strategy_4_srp(wizard: Wizard, boss: Boss) -> Spell:
    if boss.hp < 30:
        return strategy_1_random(wizard, boss)
    else:
        return strategy_by_priority(wizard, [Spell.Shield, Spell.Recharge, Spell.Poison, Spell.Drain])


def parse_input_file() -> Boss:
    lines = read_input_file(22)
    return Boss(lines)


def level22_try_x_times(
    min_mana: int, min_boss_hp: int, times: int, player_hp: int, player_mana: int, strategy, hard_mode: bool
) -> Tuple[int, int]:
    for _ in range(times):
        boss = parse_input_file()
        wizard = Wizard(player_hp, player_mana, strategy, hard_mode)
        player_won = wizard.battle(boss)
        if player_won:
            min_mana = min(min_mana, wizard.mana_used)

        if boss.hp < min_boss_hp:
            min_boss_hp = boss.hp
        if boss.hp == min_boss_hp:
            min_boss_hp = boss.hp

    return min_mana, min_boss_hp


def level22(player_hp: int, player_mana: int, simulation_scale: int, hard_mode: bool) -> int:
    num_simulations_often = 10 * simulation_scale
    num_simulations_seldom = 1 * simulation_scale
    strategies = {
        strategy_1_random: num_simulations_seldom,
        strategy_2_psr: num_simulations_seldom,
        strategy_2_prs: num_simulations_seldom,
        strategy_2_spr: num_simulations_often,
        strategy_2_srp: num_simulations_often,
        strategy_2_rsp: num_simulations_seldom,
        strategy_2_rps: num_simulations_seldom,
        strategy_2_rp: num_simulations_seldom,
        strategy_2_pr: num_simulations_seldom,
        strategy_2_ps: num_simulations_often,
        strategy_2_sp: num_simulations_often,
        strategy_2_sr: num_simulations_often,
        strategy_2_rs: num_simulations_often,
        strategy_2_r: num_simulations_seldom,
        strategy_2_s: num_simulations_seldom,
        strategy_2_p: num_simulations_often,
        strategy_3_magic_missile: 1,
        strategy_3_drain: 1,
        strategy_4_srp: num_simulations_often,
    }

    min_mana = 10000000
    min_boss_hp = 10000000

    level22_try_x_times(min_mana, min_boss_hp, 1, player_hp, player_mana, strategy_4_srp, hard_mode)

    for strategy in strategies:
        new_min_mana, new_min_boss_hp = level22_try_x_times(
            min_mana, min_boss_hp, strategies[strategy], player_hp, player_mana, strategy, hard_mode
        )
        min_mana = min(min_mana, new_min_mana)
        min_boss_hp = min(min_boss_hp, new_min_boss_hp)

    return min_mana


if __name__ == "__main__":
    _min_mana_to_win_easy = level22(50, 500, 500, False)
    print(f"Min mana to win (easy): {_min_mana_to_win_easy}", flush=True)
    _min_mana_to_win_hard = level22(50, 500, 20, True)
    print(f"Min mana to win (hard): {_min_mana_to_win_hard}", flush=True)
