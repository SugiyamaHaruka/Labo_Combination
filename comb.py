import numpy as np
from sys import argv
from itertools import combinations
from copy import deepcopy
import random


def generate_comb(member_expected, member_total, max_times):
    """
    Args: (from command line)
        member_expected 　対面参加人数
        member_total    　参加総人数
        max_times       　ゼミ総回数
    Return:
        list[ (tuple), (tuple),...]
    """

    # All combinations
    current_comb = list(combinations([i for i in range(1, member_total + 1)], member_expected))

    # 一回順番をランダムにする
    random.shuffle(current_comb)

    # 最大生成数が理論組み合わせ数より小さい場合、そのまま返す
    if max_times < len(current_comb):
        return current_comb
    else:
        # 大きい場合、理論組み合わせ数の倍数かどうかを判断
        if max_times % len(current_comb):
            # 倍数ではない場合、余りの部分を乱数で生成し、現リストに追加
            # 例えば
            # 現リスト [ (3,5), (2,4) ....(1,2) ]
            # 12回生成の場合、余りの2回を乱数で生成する [ 0, 1 ]
            # 現リストに[ 0, 1 ]番を後ろに追加する
            # [ (3,5), (2,4) ....(1,2), (3,5), (2,4) ]
            # そしてもう一回順番をランダムにする

            add_list = random.sample(range(member_total), max_times % len(current_comb))
            current_comb += [current_comb[i] for i in add_list]
            random.shuffle(current_comb)
        else:
            # 倍数の場合、倍数ごとにリストを追加する
            times = int(max_times / len(current_comb))
            for i in range(times-1):
                current_comb += current_comb
            random.shuffle(current_comb)
    return current_comb


def check_condition_a(current_comb, member_dictionary):
    """
    Args: (from command line)
        current_comb 　   生成されたリスト
        member_dictionary {番号:回数}の辞書
    Return:
        Boolean
    """

    before = current_comb[0]
    for i in list(before):
        member_dictionary[str(i)] += 1

    for index in range(1, len(current_comb)):

        current = current_comb[index]
        check_list = list(before) + list(current)
        if any(check_list.count(i) > 1 for i in check_list):
            return False
        else:
            # 前回のメンバーと重複しない時
            before = deepcopy(current)
            for i in list(current):
                member_dictionary[str(i)] += 1
    return True


def check_condition_b(member_dictionary):
    """
    Args: (from command line)
        member_dictionary {番号:回数}の辞書
    Return:
        Boolean
    """

    # 参加回数に0が存在する場合は不正解
    if 0 in member_dictionary.values():
        return False
    else:
        # 理論組み合わせ数が回数の場合、分散が0の場合が最適解
        values = np.fromiter(member_dictionary.values(), dtype=float)
        if np.var(values) != 0.0:
            return False
        else:
            return True


def main():
    """
    Args: (from command line)
        member_expected 　対面参加人数
        member_total    　参加総人数
        max_times       　ゼミ総回数
    Return: none
    """

    member_expected, member_total, max_times = [int(i) for i in argv[1:]]
    # 組み合わせの理論数
    theory_num = len(list(combinations([i for i in range(1, member_total + 1)], member_expected)))
    # {メンバーの名前:回数}
    member_dictionary = {str(i): 0 for i in range(1, member_total + 1)}

    while True:

        # Combinationを生成する
        current_comb = generate_comb(member_expected, member_total, max_times)

        # 状況Aに合うか
        condition_a = check_condition_a(current_comb, member_dictionary)

        # ちょうど組み合わせ理論数の場合だけ 状況Bを判断する
        if max_times == theory_num:
            condition_b = check_condition_b(member_dictionary)
        else:
            condition_b = True

        # 全て合致の場合、出力
        if condition_a and condition_b:
            for i in current_comb[:max_times]:
                print(i)
            break
        else:
            # なければ、計算に使われた辞書をリセット
            member_dictionary = member_dictionary.fromkeys(member_dictionary, 0)


if __name__ == '__main__':
    main()

