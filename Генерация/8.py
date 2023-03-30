import requests
import random as rd

burp0_url = "http://myhost123.test:80/index.php/2023/02/21/hello-world/"
burp0_cookies = {"wordpress_test_cookie": "WP%20Cookie%20check", "wp_lang": "en_US", "wordpress_logged_in_b2b6058102d675715ef9b7689e66fcd1": "testusr%7C1680079101%7CAdu39aLdsX9wgzqDdWzYMtg2QGtdlumdweSw0BKZzjl%7C2354b81b8e4d9abc2e94594e1309f712727b498e5c8946e0c1246a883ce03ceb", "wp-settings-1": "mfold%3Do", "wp-settings-time-1": "1679554361"}
burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "DNT": "1", "Connection": "close", "Referer": "http://192.168.1.3/", "Upgrade-Insecure-Requests": "1"}
requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)

burp1_url = "http://myhost123.test:80/wp-comments-post.php"
burp1_cookies = {"wordpress_test_cookie": "WP%20Cookie%20check", "wp_lang": "en_US", "wordpress_logged_in_b2b6058102d675715ef9b7689e66fcd1": "testusr%7C1680079101%7CAdu39aLdsX9wgzqDdWzYMtg2QGtdlumdweSw0BKZzjl%7C2354b81b8e4d9abc2e94594e1309f712727b498e5c8946e0c1246a883ce03ceb", "wp-settings-1": "mfold%3Do", "wp-settings-time-1": "1679554361"}
burp1_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded", "Origin": "http://myhost123.test", "DNT": "1", "Connection": "close", "Referer": "http://myhost123.test/index.php/2023/02/21/hello-world/", "Upgrade-Insecure-Requests": "1"}
burp1_data = {"comment": str(rd.randint(0,1000)), "submit": "Post Comment", "comment_post_ID": "1", "comment_parent": "0", "_wp_unfiltered_html_comment": "0c4acd98af"}
requests.post(burp1_url, headers=burp1_headers, cookies=burp1_cookies, data=burp1_data)

burp2_url = "http://myhost123.test:80/index.php/2023/02/21/hello-world/"
burp2_cookies = {"wordpress_test_cookie": "WP%20Cookie%20check", "wp_lang": "en_US", "wordpress_logged_in_b2b6058102d675715ef9b7689e66fcd1": "testusr%7C1680079101%7CAdu39aLdsX9wgzqDdWzYMtg2QGtdlumdweSw0BKZzjl%7C2354b81b8e4d9abc2e94594e1309f712727b498e5c8946e0c1246a883ce03ceb", "wp-settings-1": "mfold%3Do", "wp-settings-time-1": "1679554361"}
burp2_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "http://myhost123.test/index.php/2023/02/21/hello-world/", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
requests.get(burp2_url, headers=burp2_headers, cookies=burp2_cookies)
