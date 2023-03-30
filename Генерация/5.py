import requests

burp0_url = "http://192.168.1.3:80/wp-login.php"
burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
requests.get(burp0_url, headers=burp0_headers)

burp1_url = "http://myhost123.test:80/wp-login.php"
burp1_cookies = {"wordpress_test_cookie": "WP%20Cookie%20check", "wordpress_logged_in_b2b6058102d675715ef9b7689e66fcd1": "testusr%7C1679566439%7CxGslj9xNmy8C5ahFwb6qBFdSSQ7sJ469NW1YxZlayNY%7C3dca5c6b890947e4c3ce1ed1cf4862979bcc033cab82e2c2921dec7904811d33"}
burp1_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "http://myhost123.test/wp-login.php", "Content-Type": "application/x-www-form-urlencoded", "Origin": "http://myhost123.test", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
burp1_data = {"log": "testusr", "pwd": "Cpp123321#", "wp-submit": "Log In", "redirect_to": "http://myhost123.test/wp-admin/", "testcookie": "1"}
requests.post(burp1_url, headers=burp1_headers, cookies=burp1_cookies, data=burp1_data)

burp2_url = "http://myhost123.test:80/wp-admin/"
burp2_cookies = {"wordpress_b2b6058102d675715ef9b7689e66fcd1": "testusr%7C1679566442%7C9CaNFIXKdUvYk9zGzADQRkN7nHcdRRLCr6egKHUobtC%7Cfc2fa3ac562c44fb63892d7b8d416e8fc4f2d9dc3f4616189dc197029e1c790c", "wordpress_test_cookie": "WP%20Cookie%20check", "wordpress_logged_in_b2b6058102d675715ef9b7689e66fcd1": "testusr%7C1679566442%7C9CaNFIXKdUvYk9zGzADQRkN7nHcdRRLCr6egKHUobtC%7C976b57934448320447f6b368986e83b759b03fbe822fa6088af8411a1922822a"}
burp2_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "http://myhost123.test/wp-login.php", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
requests.get(burp2_url, headers=burp2_headers, cookies=burp2_cookies)

burp3_url = "http://myhost123.test:80/wp-login.php?action=logout&_wpnonce=af7169c224"
burp3_cookies = {"wordpress_test_cookie": "WP%20Cookie%20check", "wordpress_logged_in_b2b6058102d675715ef9b7689e66fcd1": "testusr%7C1679566442%7C9CaNFIXKdUvYk9zGzADQRkN7nHcdRRLCr6egKHUobtC%7C976b57934448320447f6b368986e83b759b03fbe822fa6088af8411a1922822a", "wp-settings-1": "mfold%3Df", "wp-settings-time-1": "1679393642"}
burp3_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "http://myhost123.test/wp-admin/", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
requests.get(burp3_url, headers=burp3_headers, cookies=burp3_cookies)

burp4_url = "http://myhost123.test:80/wp-login.php?loggedout=true&wp_lang=en_US"
burp4_cookies = {"wordpress_test_cookie": "WP%20Cookie%20check"}
burp4_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "http://myhost123.test/wp-admin/", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
requests.get(burp4_url, headers=burp4_headers, cookies=burp4_cookies)
