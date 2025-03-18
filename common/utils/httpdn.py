import requests

class Request:

    def httpget(self,url,body,header):
        """
        :param url:
        :param body:
        :param header:
        :return: 状态码，响应，时间，
        """
        res = requests.get(url=url,params=body,headers=header)
        return res.status_code,res,res.elapsed.total_seconds()

    def httppost(self,url,body,header):
        """
        :param url:
        :param body:
        :param header:
        :return: 状态码，响应，时间，
        """
        print(url)
        print(body)
        print(header)
        if isinstance(body,dict):
            res = requests.post(url=url, json=body, headers=header)
            return res.status_code, res.json(), res.elapsed.total_seconds()
        else:
            res = requests.post(url=url, data=body, headers=header)
            return res.status_code, res.json(), res.elapsed.total_seconds()

    def httpput(self,url,body,header):
        """
        :param url:
        :param body:
        :param header:
        :return:
        """
        res = requests.put(url=url, json=body, headers=header)
        return res.status_code, res.json(), res.elapsed.total_seconds()

    def httpdel(self,url,body,header):
        """
        :param url:
        :param body:
        :param header:
        :return:
        """
        res = requests.delete(url=url, json=body, headers=header)
        return res.status_code, res.json(), res.elapsed.total_seconds()

    #请求方式也作为参数
    def http(self,method,url,body,header):
        if method == "get":
            return self.httpget(url,body,header)
        #复制的时候注意self
        elif method == "post":
            return self.httppost(url,body,header)
        elif method =="put":
            return self.httpput(url, body, header)
        elif method == "delete":
            return self.httpdel(url, body, header)

if __name__ == '__main__':
    http = Request()
    #测试get请求
    # para = {"city": "shanghai", "type": 1}
    # # res = http.httpget("http://127.0.0.1:8000/city",para,"")
    # # res = http.http("get","http://127.0.0.1:8000/city/222",para,"")
    # print(res)
    #测试post请求
    body = {
        "pro_no": "2199",
        "pro_name": "大牛测试测试2199"
    }
    #
    url ="http://localhost:8000/aiplat/pro/167"
    # res = http.httppost(url,body,"")
    # res = http.http("post", url, body, "")
    # print(res)
    #测试put请求
    # res = http.httpput(url, body, "")
    # res = http.http("put", url, body, "")
    # print(res)
    #测试delete请求
    # res = http.httpdel(url,"","")
    # res = http.http("delete",url, "", "")
    #
    # print(res)

    # res = requests.request()
    # res.json()
    body.get("pro_no")
    print(body.get("pro_no"))
