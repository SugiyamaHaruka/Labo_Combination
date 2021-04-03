import numpy.random
from sys import argv


def main():
    """
    Args: (from command line)
        member_expected 　対面参加人数
        member_total    　参加総人数
        max_times       　ゼミ総回数
    Return: none
    """

    member_expected, member_total, max_times = argv[1:]

    # [前回の参加者1,前回の参加者2]
    before = [0] * int(member_expected)

    # {メンバーの名前:回数}
    member_dictionary = {str(i): 0 for i in range(1, int(member_total) + 1)}

    count = 0
    while count < int(max_times):
        # current[今回のメンバー1,今回のメンバー1]
        # 一様分布で乱数生成
        current = numpy.random.randint(1, 6, 2)

        if all(x not in current for x in before) and len(set(current)) == 2:
            # 前回のメンバーと重複しない時
            # 乱数に重複がない時

            before = current.copy()
            for i in current:
                member_dictionary[str(i)] += 1
            print("参加者一 : " + str(current[0]) + " 参加者二 : " + str(current[1]))

            count += 1

    print(member_dictionary)


if __name__ == '__main__':
    main()

