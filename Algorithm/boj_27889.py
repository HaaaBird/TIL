# boj_27889.py
# 특별한 학교 이름

schools = {
    "NLCS": "North London Collegiate School",
    "BHA": "Branksome Hall Asia",
    "KIS": "Korea International School",
    "SJA": "St. Johnsbury Academy",
}

in_str = input()

print(schools.get(in_str))