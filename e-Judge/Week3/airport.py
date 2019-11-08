""" e-Judge """
def main():
    """ Airport """
    destination = input()
    time_fly = input()
    hour_fly = int(time_fly[0:2])
    min_fly = int(time_fly[3:5])
    # แปลงเป็น 24 ชั่วโมง ก่อน
    if hour_fly == 12 and ("am" in time_fly): # ถ้า time_fly เป็น am
        hour_fly = 0
    elif 1 <= hour_fly <= 11 and ("pm" in time_fly): # ถ้า time_fly เป็น pm
        hour_fly += 12
    min_fly += hour_fly*60
    time_travel = 0
    if destination == "A":
        time_travel += (25+15+5+70+45)
    elif destination == "B":
        time_travel += (15+10+70+45)
    elif destination == "C":
        time_travel += (5+65+45)
    min_fly -= time_travel
    hour_fly = min_fly // 60
    min_time = min_fly - (hour_fly*60)
    hour_fly = hour_fly % 24 # ดักข้ามวัน
    if hour_fly == 0: # แปลงกลับเป็น 12 (am)
        print("12:%02dam" % min_time)
    elif hour_fly == 12: # แปลง am เป็น pm
        print("12:%02dpm" % min_time)
    elif 12 < hour_fly <= 23: # แปลง am เป็น pm
        hour_fly -= 12
        print("%02d:%02dpm" % (hour_fly, min_time))
    else: # am อยู่แล่ว
        print("%02d:%02dam" % (hour_fly, min_time))
main()