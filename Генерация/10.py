import requests

burp0_url = "http://192.168.1.3:80/"
burp0_cookies = {"wordpress_test_cookie": "WP%20Cookie%20check"}
burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)

burp1_url = "http://myhost123.test:80/wp-login.php?action=login"
burp1_cookies = {"wordpress_test_cookie": "WP%20Cookie%20check", "wp_lang": "en_US", "wp-settings-1": "mfold%3Do", "wp-settings-time-1": "1679554361"}
burp1_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "DNT": "1", "Connection": "close", "Referer": "http://192.168.1.3/", "Upgrade-Insecure-Requests": "1"}
requests.get(burp1_url, headers=burp1_headers, cookies=burp1_cookies)

burp2_url = "http://myhost123.test:80/wp-login.php"
burp2_cookies = {"wordpress_test_cookie": "WP%20Cookie%20check", "wp_lang": "en_US", "wp-settings-1": "mfold%3Do", "wp-settings-time-1": "1679554361"}
burp2_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "http://myhost123.test/wp-login.php?action=login", "Content-Type": "application/x-www-form-urlencoded", "Origin": "http://myhost123.test", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
burp2_data = {"log": "792", "pwd": "792", "wp-submit": "Log In", "redirect_to": "http://myhost123.test/wp-admin/", "testcookie": "1"}
requests.post(burp2_url, headers=burp2_headers, cookies=burp2_cookies, data=burp2_data)

burp3_url = "http://myhost123.test:80/wp-admin/profile.php"
burp3_cookies = {"wordpress_b2b6058102d675715ef9b7689e66fcd1": "792%7C1680080457%7C43wbm4OPRdYFY5VwyLK5Bnhxl1321jM47F14qMvhh1T%7C76e3d5f7ccd824c62a961e486905a92fa6cce27e110ab732e78a8a6b029878aa", "wordpress_test_cookie": "WP%20Cookie%20check", "wp_lang": "en_US", "wp-settings-1": "mfold%3Do", "wp-settings-time-1": "1679554361", "wordpress_logged_in_b2b6058102d675715ef9b7689e66fcd1": "792%7C1680080457%7C43wbm4OPRdYFY5VwyLK5Bnhxl1321jM47F14qMvhh1T%7Cef8081dd8a07539e109e9a1ab83d22a122852490252c26a60f219efeda680d74"}
burp3_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "http://myhost123.test/wp-login.php?action=login", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
requests.get(burp3_url, headers=burp3_headers, cookies=burp3_cookies)

burp4_url = "http://myhost123.test:80/wp-login.php?action=logout&_wpnonce=1834e0600a"
burp4_cookies = {"wordpress_test_cookie": "WP%20Cookie%20check", "wp_lang": "en_US", "wp-settings-1": "mfold%3Do", "wp-settings-time-1": "1679554361", "wordpress_logged_in_b2b6058102d675715ef9b7689e66fcd1": "792%7C1680080457%7C43wbm4OPRdYFY5VwyLK5Bnhxl1321jM47F14qMvhh1T%7Cef8081dd8a07539e109e9a1ab83d22a122852490252c26a60f219efeda680d74", "wp-settings-time-16": "1679907657"}
burp4_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "http://myhost123.test/wp-admin/profile.php", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
requests.get(burp4_url, headers=burp4_headers, cookies=burp4_cookies)

burp5_url = "http://myhost123.test:80/wp-login.php?loggedout=true&wp_lang=en_US"
burp5_cookies = {"wordpress_test_cookie": "WP%20Cookie%20check", "wp_lang": "en_US", "wp-settings-1": "mfold%3Do", "wp-settings-time-1": "1679554361"}
burp5_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "http://myhost123.test/wp-admin/profile.php", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
requests.get(burp5_url, headers=burp5_headers, cookies=burp5_cookies)
