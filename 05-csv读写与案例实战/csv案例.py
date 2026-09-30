import csv
import requests
import jsonpath
import json
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "origin": "https://xueqiu.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://xueqiu.com/",
    "sec-ch-ua": "\"Not;A=Brand\";v=\"8\", \"Chromium\";v=\"150\", \"Google Chrome\";v=\"150\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36"
}
cookies = {
    "xq_a_token": "7285291d27f8ae5f9b71c440942dc17a334c918c",
    "xqat": "7285291d27f8ae5f9b71c440942dc17a334c918c",
    "xq_r_token": "3d0342e6e6675a4f4f9d65702ecd1f78e50b939c",
    "xq_id_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTc4NjIzODYzOCwiY3RtIjoxNzg0MTc5NDYyMTkzLCJjaWQiOiJkOWQwbjRBWnVwIn0.QGSiDWxqtOu27hbR-tJmA4y3KClluX_vls60iy2SzGfW9t7k_DbJiekdfaT0Aer6nzRv10MbLEqUXxtiuPnXH3uuK2yEpN31nxyy1CGxjDAdtF-O84d43wcdHmDwbpR-ye6mC61IGq8lciMNonabsg9bi14TGEY7HpYilMf8IdJ6MBSAQZQaS_f-Q5OFoyrvr78YK6oMsAf1tDuLi1CtciaV4KNsLizWE8ctGsuK5TYlYEb2drmrQL8Z1hpRsnUInqqrH8ZtBx43GKcTZk2APmRXNZYsJPRK1ccPsPZ55aS-XtdgaJWphAURpKEGafx996HQjhpfIfRScfzxBAjYeg",
    "cookiesu": "811784179476177",
    "u": "811784179476177",
    "device_id": "25db0ecca2f3b9f8518f5ddab8da3e96",
    "Hm_lvt_1db88642e346389874251b5a1eded6e3": "1784179477",
    "HMACCOUNT": "B18D00D97F7300E2",
    "Hm_lpvt_1db88642e346389874251b5a1eded6e3": "1784179483",
    "ssxmod_itna": "1-Yq0x9DcD2Q0Q0=YD=G0WGCDIOUIhnDGQqDXDUqAQD2DIde7=GFKDCEhFhYmWghifyPoe8BAWU5lD0v4emDA5Dn_x7YDtr39iD00u0w6dF0C0wd3BhAhxp199FAbu3W//1uKe8MhE89v5AtpQGi8C8DbDB3DbqDy3_5oYxGGj4GwDGoD34DiDDPDbfrDAqPD7qDFBWnb=cTDm4GWBCbDmqG2leDfDAEOaAh6npTdxD3DfSTPQ0bDe8FNy4Dl9fS6zDD_F7FjHjFWU1nK0FxPBeDM7xGXiiZ6BeDBFXZ6WPM2dNFpjeGyB5GuQP3FawUP=/eLtajY25WR5YrH3DoiDT8iteRFFwm80Plx5HGx8DNz0D94h3EeUDNYrbiTHBPN9483rHUGeM5DPYx=YoYiNO_4zTGATHG0DQi7QDxQTQZON/rtmOeD_Yr0PSGeYo4iWiOA3O7GGi7bgc3qTIB3LOFCoePD",
    "ssxmod_itna2": "1-Yq0x9DcD2Q0Q0=YD=G0WGCDIOUIhnDGQqDXDUqAQD2DIde7=GFKDCEhFhYmWghifyPoe8BAWU5mDneooq_ifYxDLBL2WePXDGXxTv=6B971/z=rw63I4DIEQiAFRHehanZ2HPuk0zLmgI2G0lMhDpAUKUwDf_xhdYCLdCdKijkd4GQIKAfX233N5Mk3iWGwUCbNX8Yx9i0DgRq4XK7Gd/oU3Eb4yln2cWQR=5CDGZdIxvTxY9R6c0i_Isw=9FMWybQUxOYR_zTFVK6vYyM=/Uk6eNzUt57QLXCuy4d67FqM5KdNG1XRggCQ3dQZdNZfzdTN4uxS27wgoShN5Lx88h/4xzOKDMtkS39TwXdiHrQLhwug_2OClo=wkiz_kfWt7hz1OamTGwlzqCdqfHyhbEu11WmULtRMWmndddsP73ibx7013BvSmE2DCkhasrFyoa9LH/rxP=N57dhbmyxwWODNRh6oQH7EnOtz7w1b7M3Q0R=tMW=bmExw=eQZ8xbuzSQvqG=rc6HGAIhWLQhNxFqGqU6F=GOtk3KY8/u8rMOTkbAaN=GNyfzK7iH9_z2D_W_Hr4H1Tur4vZTRFh1b0bZ=iRHqbB5dEL38kTviRG74R34L=fpygRmEk1QNvRrNsw84B/_kFHQ5Fzb==WbF2xZqmeX44l0GL25Ed9gMET2xugx/YQN7p7Mazw03MR65B4FEng5eiFk8R4c0=tDpxqCqGY5GpMd4P0og=8DeGeYx9DePrE_DBxsDYYGfo4D_Kieq2FQeOqxD"
}
for x in range(1,11):
    url = "https://stock.xueqiu.com/v5/stock/screener/quote/list.json"
    params = {
        "page": f"{x}",
        "size": "30",
        "order": "desc",
        "order_by": "percent",
        "market": "CN",
        "type": "sh_sz"
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)

    # print(response.json())
    data = response.json()
    symbol = jsonpath.jsonpath(data, '$..symbol')
    name = jsonpath.jsonpath(data, '$..name')
    current = jsonpath.jsonpath(data, '$..current')
    chg = jsonpath.jsonpath(data, '$..chg')
    # print(symbol)
    # print(name)
    # print(current)
    # print(chg)
    head = [
        'symbol', 'name', 'current', 'chg'
    ]
    sum__list = []
    for i in zip(symbol, name, current, chg):
        list = []
        for j in i:
            if j is None:
                a = '-'
                list.append(a)
            else:
                list.append(j)
        sum__list.append(list)
        # print(list)
    with open('csv案例.csv', 'a', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(head)
        writer.writerows(sum__list)
#print(response)
