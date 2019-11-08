""" e-Judge """
def main():
    """ Checkmate """
    # y ก่อน x
    k_mine = input()
    q_mine = input()
    k_him = input()
    other = int(input())
    lst_other = []
    for _ in range(other):
        other_him = input()
        lst_other.append(other_him)
    if (abs(int(k_mine[0])-int(k_him[0])) <= 1)\
         and (abs(int(k_mine[1])-int(k_him[1])) <= 1): # Check King
        print('Checkmate')
    else:
        choice = k_pos(q_mine.split(), k_him.split())
        if choice == '4':
            print('Defeat')
        else:
            lst_other.append(k_mine)
            chk = chkordef(choice, lst_other, q_mine, k_him)
            if 'D' in chk:
                print('Defeat')
            else:
                print('Checkmate')
 
def k_pos(start, stop):
    """ King Position """
    if (abs(int(start[0][0])-int(stop[0][0])))\
         == (abs(int(start[0][1])-int(stop[0][1]))): # อยู่ทางเฉียง
        return '1'
    elif int(start[0][0]) == int(stop[0][0]): # อยู่ซ้าย-ขวา
        return '2'
    elif int(start[0][1]) == int(stop[0][1]): # อยู่บน-ล่าง
        return '3'
    else:
        return '4'
 
def chkordef(choice, opponent, queen, king):
    """ Checkmate or Defeat """
    lst_chk = []
    if choice == '1':
        for i in range(len(opponent)):
            case_1 = (int(king[0]) < int(opponent[i][0])) and (int(opponent[i][0]) < int(queen[0]))
            case_2 = (int(king[0]) > int(opponent[i][0])) and (int(opponent[i][0]) > int(queen[0]))
            case_3 = (int(king[1]) < int(opponent[i][1])) and (int(opponent[i][1]) < int(queen[1]))
            case_4 = (int(king[1]) > int(opponent[i][1])) and (int(opponent[i][1]) > int(queen[1]))
            if (abs(int(opponent[i][0])-int(queen[0])) == abs(int(opponent[i][1])-int(queen[1])))\
             and (case_1 or case_2) and (case_3 or case_4):
                lst_chk.append('D')
            else:
                lst_chk.append('C')
    elif choice == '2':
        for i in range(len(opponent)):
            case_1 = (int(king[1]) < int(opponent[i][1])) and (int(opponent[i][1]) < int(queen[1]))
            case_2 = (int(king[1]) > int(opponent[i][1])) and (int(opponent[i][1]) > int(queen[1]))
            if (int(opponent[i][0]) == int(queen[0]))\
                 and (case_1 or case_2):
                lst_chk.append('D')
            else:
                lst_chk.append('C')
    elif choice == '3':
        for i in range(len(opponent)):
            case_1 = (int(king[0]) < int(opponent[i][0])) and (int(opponent[i][0]) < int(queen[0]))
            case_2 = (int(king[0]) > int(opponent[i][0])) and (int(opponent[i][0]) > int(queen[0]))
            if (int(opponent[i][1]) == int(queen[1]))\
                 and (case_1 or case_2):
                lst_chk.append('D')
            else:
                lst_chk.append('C')
    return lst_chk
main()