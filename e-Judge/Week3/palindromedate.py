""" e-Judge """
def main():
    """ Palindrome Dates """
    day = input() # datemonthyear
    day = day.replace("-", "")
    date = day[0:2]
    month = day[2:4]
    year = day[4:]
    swap_dm = month + date # สลับวัน-เดือน
    dm_0 = str(int(date)) + str(int(month)) # ตัด 0 ตำแหน่งเดิม
    md_0 = str(int(month)) + str(int(date)) # ตัด 0 + สลับวัน-เดือน
    remove_year = year[2:]
    # จัดกลุ่ม
    day_01 = swap_dm + year # สลับวัน-เดือน + ปี 4 หลัก
    day_02 = swap_dm + remove_year # สลับวัน-เดือน + ปี 2 หลัก
    day_03 = dm_0 + year # ตัด 0 (ตำแหน่งเดิม) + ปี 4 หลัก
    day_04 = dm_0 + remove_year # ตัด 0 (ตำแหน่งเดิม) + ปี 2 หลัก
    day_05 = md_0 + year # ตัด 0 + สลับวัน-เดือน + ปี 4 หลัก
    day_06 = md_0 + remove_year # ตัด 0 + สลับวัน-เดือน + ปี 2 หลัก
    if day == day[::-1]:
        print("Yes!!")
    elif day_01 == day_01[::-1]:
        print("Yes!!")
    elif day_02 == day_02[::-1]:
        print("Yes!!")
    elif day_03 == day_03[::-1]:
        print("Yes!!")
    elif day_04 == day_04[::-1]:
        print("Yes!!")
    elif day_05 == day_05[::-1]:
        print("Yes!!")
    elif day_06 == day_06[::-1]:
        print("Yes!!")
    else:
        print("No!!")
main()