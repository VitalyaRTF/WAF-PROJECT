import requests
import random as rd

burp0_url = "http://myhost123.test:80/wp-login.php"
burp0_cookies = {"wordpress_test_cookie": "WP%20Cookie%20check", "wp_lang": "en_US"}
burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)

burp1_url = "http://myhost123.test:80/wp-login.php"
burp1_cookies = {"wordpress_test_cookie": "WP%20Cookie%20check", "wp_lang": "en_US"}
burp1_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "http://myhost123.test/wp-login.php", "Content-Type": "application/x-www-form-urlencoded", "Origin": "http://myhost123.test", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
burp1_data = {"log": "testusr", "pwd": "Cpp123321#", "wp-submit": "Log In", "redirect_to": "http://myhost123.test/wp-admin/", "testcookie": "1"}
requests.post(burp1_url, headers=burp1_headers, cookies=burp1_cookies, data=burp1_data)

burp2_url = "http://myhost123.test:80/wp-admin/"
burp2_cookies = {"wordpress_b2b6058102d675715ef9b7689e66fcd1": "testusr%7C1679560730%7CLM6RL4rWoXIlcQVMN4pHJU8IYZyWICR5q6acLhWdoL6%7Cbcbc991a64921df49fc024c463c1f50503c7b45d24aa6b12f9a9152884b8840c", "wordpress_test_cookie": "WP%20Cookie%20check", "wp_lang": "en_US", "wordpress_logged_in_b2b6058102d675715ef9b7689e66fcd1": "testusr%7C1679560730%7CLM6RL4rWoXIlcQVMN4pHJU8IYZyWICR5q6acLhWdoL6%7C01fe0da361f8e5be259ba049f023bf2b1da34c8fe512b8955ea25d6fc7dead32"}
burp2_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "http://myhost123.test/wp-login.php", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
requests.get(burp2_url, headers=burp2_headers, cookies=burp2_cookies)

burp0_url = "http://myhost123.test:80/wp-admin/user-new.php"
burp0_cookies = {"wordpress_b2b6058102d675715ef9b7689e66fcd1": "testusr%7C1679562426%7Cjc7kc3pVMEBn1PoQsCCKtQf7TQDq2QhIL2JwI5lKVd8%7C9d56acd8d8b1727726c16ef5802300e5cb4554bbd06d3568bf7c4762cba501c4", "wordpress_test_cookie": "WP%20Cookie%20check", "wp_lang": "en_US", "wordpress_logged_in_b2b6058102d675715ef9b7689e66fcd1": "testusr%7C1679562426%7Cjc7kc3pVMEBn1PoQsCCKtQf7TQDq2QhIL2JwI5lKVd8%7C359bf5c247d8d32fde7e8831d323cb6667cf7d5e07f5804394a10b46fa812a97", "wp-settings-1": "mfold%3Df", "wp-settings-time-1": "1679387930"}
burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "http://myhost123.test/wp-admin/", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)

burp1_url = "http://myhost123.test:80/wp-admin/user-new.php"
burp1_cookies = {"wordpress_b2b6058102d675715ef9b7689e66fcd1": "testusr%7C1679562426%7Cjc7kc3pVMEBn1PoQsCCKtQf7TQDq2QhIL2JwI5lKVd8%7C9d56acd8d8b1727726c16ef5802300e5cb4554bbd06d3568bf7c4762cba501c4", "wordpress_test_cookie": "WP%20Cookie%20check", "wp_lang": "en_US", "wordpress_logged_in_b2b6058102d675715ef9b7689e66fcd1": "testusr%7C1679562426%7Cjc7kc3pVMEBn1PoQsCCKtQf7TQDq2QhIL2JwI5lKVd8%7C359bf5c247d8d32fde7e8831d323cb6667cf7d5e07f5804394a10b46fa812a97", "wp-settings-1": "mfold%3Df", "wp-settings-time-1": "1679387930"}
burp1_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "http://myhost123.test/wp-admin/user-new.php", "Content-Type": "application/x-www-form-urlencoded", "Origin": "http://myhost123.test", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
user_tag = str(rd.randint(0,1000))
burp1_data = {"action": "createuser", "_wpnonce_create-user": "6ddbbae078", "_wp_http_referer": "/wp-admin/user-new.php", "user_login": user_tag, "email": user_tag+"@mail.ru", "first_name": '', "last_name": '', "url": '', "pass1": "123", "pass2": "123", "pw_weak": "on", "send_user_notification": "1", "role": "subscriber", "createuser": "Add New User"}
requests.post(burp1_url, headers=burp1_headers, cookies=burp1_cookies, data=burp1_data)

burp2_url = "http://myhost123.test:80/wp-admin/users.php?update=add&id=4"
burp2_cookies = {"wordpress_b2b6058102d675715ef9b7689e66fcd1": "testusr%7C1679562426%7Cjc7kc3pVMEBn1PoQsCCKtQf7TQDq2QhIL2JwI5lKVd8%7C9d56acd8d8b1727726c16ef5802300e5cb4554bbd06d3568bf7c4762cba501c4", "wordpress_test_cookie": "WP%20Cookie%20check", "wp_lang": "en_US", "wordpress_logged_in_b2b6058102d675715ef9b7689e66fcd1": "testusr%7C1679562426%7Cjc7kc3pVMEBn1PoQsCCKtQf7TQDq2QhIL2JwI5lKVd8%7C359bf5c247d8d32fde7e8831d323cb6667cf7d5e07f5804394a10b46fa812a97", "wp-settings-1": "mfold%3Df", "wp-settings-time-1": "1679387930"}
burp2_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "http://myhost123.test/wp-admin/user-new.php", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
requests.get(burp2_url, headers=burp2_headers, cookies=burp2_cookies)
