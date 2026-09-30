import requests
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0',
    'Cookie':'webanlytics2020pageinfo=%7B%22isFirstTime%22%3Afalse%7D; isGuide=-1; UM_distinctid=197cb5840e018d-0a32c2cf01e69a8-4c657b58-168000-197cb5840e1dca; _gprp_c=""; Qnick=; _4399stats_vid=17515378395423534; webanlytics2020userinfo=%7B%22distinct_id%22%3A%22af781a6028996487904c8b911ba53edf%22%2C%22vid%22%3A%22af781a6028996487904c8b911ba53edf%22%2C%22uid%22%3A%22%22%2C%22createTime%22%3A1751539943225%7D; _4399tongji_vid=175153994364634; zone_guide_limit=-1; zone_guide=-1; Hm_lvt_e54c3322799bd1eb83f9003a22de4e66=1759066413; webanlytics2020userinfo_4399_com=%7B%22distinct_id%22%3A%22784d12ea72e8818014c0d8e294caf547%22%2C%22vid%22%3A%22784d12ea72e8818014c0d8e294caf547%22%2C%22uid%22%3A3037139735%2C%22createTime%22%3A1759585070421%7D; gdc_webRecordId=31bb4d3d-5ccc07-c185c9; gdc_newStatCid=3001; gdc_newStatOid1=19479; webRecordIdP=31bb4d3d-5ccc07-c185c9; gdc_userMark=J31qR17yB45TF-39Hc85om88Hc5-9gX70FX57Fw51-es80Xy21om17L; global_hs=4399.com%7C%7C%7C4399%u4E09%u56FD%u6740%7C%7Chttps%3A//my.4399.com/yxsgs/%7C%7C1; zone_guide_date=1763049600; zone_guide_time=1; home4399=yes; Hm_lvt_334aca66d28b3b338a76075366b2b9e8=1761963547,1764499224; HMACCOUNT=3CCB6468957AAF08; USESSIONID=cfd04846-63be-420e-9f71-50d164c70726; phlogact=l138434; Uauth=4399|1|20251130|dev4399.|1764499245550|e731d160d693ed6881416b6ac39cb202; Pauth=1448849939|790791484|t3ce7n27085480c867e4e2ca8e72ca2b|1764499245|10002|7125d4c8d1d18e9d385990a4561abc60|2; ck_accname=790791484; Puser=790791484; Xauth=aef44e6ffc382c2c9ec68be2f126094c; ptusertype=dev4399.4399_login; Pnick=165135535b; Hm_lpvt_334aca66d28b3b338a76075366b2b9e8=1764499376; ol=1; Hm_lvt_5c9e5e1fa99c3821422bf61e662d4ea5=1762167927,1762994809,1763002191,1764499385; _4399tongji_st=1764499384; Hm_lvt_e5a07b5994f78634294b9c347a5be7d2=1762167927,1762994809,1763002191,1764499385; Pmtime=dc495dd05a53d180910b%7C1764499565; Hm_lpvt_5c9e5e1fa99c3821422bf61e662d4ea5=1764499573; Hm_lpvt_e5a07b5994f78634294b9c347a5be7d2=1764499573',
    'Referer':'https://my.4399.com/forums/mtag-82186?page=2'
}
n=1
for i in range(1,8):
    # 1.明确目标
    url = f'https://my.4399.com/forums/mtag-82186?page={i}'
    # 2.发起请求，接受响应

    res = requests.get(url, headers=headers)
    res.encoding = 'utf-8'
    #print(res.text)
    # 3.数据解析（提取）

    # 4.数据存储
    with open(f'./造梦西游论坛./{n}.html','w',encoding='utf-8') as f:
        f.write(res.text)
    n+=1
