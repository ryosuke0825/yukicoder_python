def main():
    N = int(input())
    if N == 1:
        return 1
    first_num = 1
    # 次にチェックする階層の値を格納する配列
    next_check = [first_num]
    # チェック済みの値を格納するコレクション
    checked = {first_num}
    step = 1
    # 次にチェックする値がなくなる＝一番深い階層までチェックが終わるまでループ
    while next_check:
        new_next_check = []
        step += 1
        # 次にチェックする配列のすべての値をチェック
        for val in next_check:
            bit_num = bin(val).count('1')
            # 進める場所または戻る場所にNがあれば終了
            if val + bit_num == N or val - bit_num == N:
                return step
            # Nがない場合は進めるマス、戻れるマスが未チェック且つ取り得る範囲内なら配列に追加
            val_plus = val + bit_num
            val_minus = val - bit_num
            if val_plus not in checked and val_plus < N:
                new_next_check.append(val_plus)
                checked.add(val_plus)
            if val_minus not in checked and val_minus < N:
                new_next_check.append(val_minus)
                checked.add(val_minus)
        next_check = new_next_check
    return -1


if __name__ == "__main__":
    print(main())
