from sys import argv
from itertools import combinations
from copy import deepcopy
import random


# 初めの組み合わせを生成する関数
def generate_comb(member_expected, member_total, member_dictionary):
    """
    Args: (from command line)
        member_expected 　対面参加人数
        member_total    　参加総人数
        max_times       　ゼミ総回数
    Return:
        list[ (tuple), (tuple),...]
    """
    while True:
        # All combinations
        current_comb = list(combinations([i for i in range(1, member_total + 1)], member_expected))
        """
        test_list = []
        for i in range(i, member_total + 1):
            test_list.append(i)
        current_comb = list(combinations(test_list,member_expected))
        """
        # 一度順番をランダムにする
        random.shuffle(current_comb)

        # 前後でかぶっている部分がないかどうかを確かめる。かぶっていない場合には Trueが返される
        condition = check_condition(current_comb, member_dictionary)

        if condition:
            return current_comb
        else:
            # 前後でかぶっている部分があった場合、新たな組み合わせを生成するために、計算に使われた辞書をリセット
            member_dictionary = member_dictionary.fromkeys(member_dictionary, 0)


# 組み合わせの並べ方で、前後でかぶっているものがないかどうかを確認するための関数
def check_condition(current_comb, member_dictionary):
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
        """
        test_flag = True
        for i in check_list:
            if check_list.count(i) > 1:
                test_flag = False
                break
        """
        if any(check_list.count(i) > 1 for i in check_list):
            return False
        else:
            # 前回のメンバーと被っていない場合
            before = deepcopy(current)
            for i in list(current):
                member_dictionary[str(i)] += 1
    return True


# 組合せを生成するのが2度目以降(max_timesが11以上のとき)の時に利用する関数
def re_comb(member_expected, member_total, member_dictionary, current_comb, times, added):
    while times:
        next_comb = generate_comb(member_expected, member_total, member_dictionary)
        check_list = list(current_comb[-1]) + list(next_comb[0])
        """
        current_comb = (1,2)
        next_comb = (3,4)
        check_list = [1,2,3,4]
        """
        if not any(check_list.count(i) > 1 for i in check_list):
            current_comb += next_comb
            times -= 1

    return current_comb


# 全ての組合せを表示する回数
def print_members(current_comb, max_times):
    name_dict = {
        1:"18T4006",
        2:"18T4015",
        3:"18T4025",
        4:"18T4029",
        5:"18T4043"
    }
    filename = "result" + str(max_times) + ".txt"
    for i,v in enumerate(current_comb[:max_times]):
        """
        f' format済み
        <  左寄り並び
    　　 <7 左寄り7byte
        """
        result_print = f'{str("No." + str(i + 1) +":"):<7} {name_dict[list(v)[0]]:<12} {name_dict[list(v)[1]]:<12}'
        with open(filename, "a") as fs:
            fs.write(result_print + "\n")
            print(result_print)


def main():
    """
    Args: (from command line)
        member_expected 　対面参加人数
        member_total    　参加総人数
        max_times       　ゼミ総回数
    Return: none
    """

    member_expected, member_total, max_times = [int(i) for i in argv[1:]]
    """
    arg_list = []
    for i in argv:
        arg_list.append(i)
    member_expected, member_total, max_times = arg_list
    # arg_list: ["?","?","?"]
    """
    # 組み合わせの理論数
    theory_num = len(list(combinations([i for i in range(1, member_total + 1)], member_expected)))
    
    # {メンバーの名前:回数}
    member_dictionary = {str(i): 0 for i in range(1, member_total + 1)}
    """
    member_dictionary = {}
    for i in range(1,member_total + 1):
        member_dictionary[str(i)] = 0
    """
    times = max_times // theory_num  # 42 // 10 = 4
    added = max_times % theory_num  # 42 % 10 = 2

    # Combinationを生成する。
    current_comb = generate_comb(member_expected, member_total, member_dictionary)
    all_comb = re_comb(member_expected, member_total, member_dictionary, current_comb, times, added)
    print_members(all_comb, max_times)


if __name__ == '__main__':
    main()

