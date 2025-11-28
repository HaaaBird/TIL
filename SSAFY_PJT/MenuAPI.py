import requests
import uuid
import pprint

DEVICE_ID = str(uuid.uuid4()) # 전역으로 고정. 항상 동일한 DEVICE_ID 값을 보장해야 함.
def get_authorization():
    LOGIN_URL = "https://welplus.welstory.com/login"
    
    headers = {
        "User-Agent": "Welplus",
        "X-Device-Id": DEVICE_ID,
        "Content-Type": "application/x-www-form-urlencoded",
        "X-Autologin": "N",
    }
    
    data = {
        "username": "thinkingong1",
        "password": "Tkvl1234@",
        "remember-me": "false",
    }
    
    response = requests.post(LOGIN_URL, headers=headers, data=data)
    print("Login Status:", response.status_code)
    return response.headers.get("Authorization")


def get_menu_from_welstory_api(date, meal_time, restaurant_code, token):
    BASE_URL = "https://welplus.welstory.com"
    ENDPOINT = "/api/meal"
    params = {
        "menuDt": date,
        "menuMealType": str(meal_time),
        "restaurantCode": restaurant_code,
    }
    
    headers = {
        "User-Agent": "Welplus",
        "X-Device-Id": DEVICE_ID,
        "Authorization": token,
        "Cookie": f"cafeteriaActiveId={restaurant_code}", # 가짜쿠키
    }
    
    response = requests.get(BASE_URL + ENDPOINT, headers=headers, params=params)
    
    print("Menu Status:", response.status_code)
    
    try:
        pprint.pprint(response.json())
    except:
        print(response.text)


if __name__ == "__main__":
    # 로그인 -> 토큰 발급
    """
    서울멀티캠: REST000133
    삼성전기 부산(부울경캠): REST000595
    구미1캠: REST000017
    구미2캠-1: REST000018
    구미2캠-2: REST000019
    """
    token = get_authorization()
    restaurant_code = 'REST000595'
    get_menu_from_welstory_api(
        date="20251121",
        meal_time=2,
        restaurant_code=restaurant_code,
        token=token
    )
