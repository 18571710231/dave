import requests


class TestDemo:
    def test_get(self):
        r = requests.get("http://httpbin.testing-studio.com/get")
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code == 200

    def test_query(self):
        payload = {
            "level": 1,
            "name": "seveniruby",
            "age": "33"
        }
        r = requests.get("http://httpbin.testing-studio.com/get", params=payload)
        print(r.text)
        assert r.status_code == 200

    def test_post_form(self):
        body = {
            "level": 1,
            "name": "seveniruby",
            "age": "33"
        }
        r = requests.post("http://httpbin.testing-studio.com/post", data=body)
        print(r.text)
        assert r.status_code == 200

    def test_header(self):
        r = requests.get("http://httpbin.testing-studio.com/get", headers={"h": "python"})
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code == 200
        assert r.json()["headers"]["H"] == "python"

    def test_json(self):
        json = {
            "level": 1,
            "name": "seveniruby",
            "age": "33"
        }
        r = requests.post("http://httpbin.testing-studio.com/post", json=json)
        print(r.text)
        assert r.status_code == 200
        assert r.json()["json"]["level"] == 1

    def test_assert_json(self):
        from jsonpath import jsonpath
        r = requests.get("https://home.testing-studio.com/categories.json")
        print(r.text)
        assert r.status_code == 200
        print(jsonpath(r.json(), '$..name'))
        assert jsonpath(r.json(), '$..name')[0] == "提问区"

    def test_hamcrest(self):
        from jsonpath import jsonpath
        r = requests.get("https://home.testing-studio.com/categories.json")
        print(r.text)
        assert r.status_code == 200
        print(jsonpath(r.json(), '$..name'))
        assert jsonpath(r.json(), '$..name')[0] == "提问区"

    def test_cookie(self):
        url = "https://home.testing-studio.com/cookies"
        cookie_data = {
            "user":"dave",
            "pssword":"123456"
        }
        r = requests.get(url=url,cookies=cookie_data)
        print(r.request.headers)

    def test_oauth(self):
        from requests.auth import HTTPBasicAuth
        r = requests.get(url="http://httpbin.testing-studio.com/basic-auth/banana/123", auth=HTTPBasicAuth("banana", "123"))
        print(r.text)
