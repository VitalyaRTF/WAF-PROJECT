import requests
import random as rd

burp0_url = "http://192.168.1.3:80/"
burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
requests.get(burp0_url, headers=burp0_headers)

burp1_url = "http://myhost123.test:80/wp-login.php?action=login"
burp1_cookies = {"wordpress_test_cookie": "WP%20Cookie%20check", "wordpress_logged_in_b2b6058102d675715ef9b7689e66fcd1": "testusr%7C1680519782%7CM4bLZAbKNxjObaNJEDwGCukqvPYjY0Thhmn2QuQxTVC%7Cb67d630bf271afe9115f51e1e414511cdffd578e3f82d0885c52bbf058a9016e", "wp-settings-1": "mfold%3Do", "wp-settings-time-1": "1679909100"}
burp1_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "DNT": "1", "Connection": "close", "Referer": "http://192.168.1.3/", "Upgrade-Insecure-Requests": "1"}
requests.get(burp1_url, headers=burp1_headers, cookies=burp1_cookies)

burp2_url = "http://myhost123.test:80/wp-login.php"
burp2_cookies = {"wordpress_test_cookie": "WP%20Cookie%20check", "wordpress_logged_in_b2b6058102d675715ef9b7689e66fcd1": "testusr%7C1680519782%7CM4bLZAbKNxjObaNJEDwGCukqvPYjY0Thhmn2QuQxTVC%7Cb67d630bf271afe9115f51e1e414511cdffd578e3f82d0885c52bbf058a9016e", "wp-settings-1": "mfold%3Do", "wp-settings-time-1": "1679909100"}
burp2_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "http://myhost123.test/wp-login.php?action=login", "Content-Type": "application/x-www-form-urlencoded", "Origin": "http://myhost123.test", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
burp2_data = {"log": "testusr", "pwd": "Cpp123321#", "wp-submit": "Log In", "redirect_to": "http://myhost123.test/wp-admin/", "testcookie": "1"}
requests.post(burp2_url, headers=burp2_headers, cookies=burp2_cookies, data=burp2_data)

burp3_url = "http://myhost123.test:80/wp-admin/"
burp3_cookies = {"wordpress_b2b6058102d675715ef9b7689e66fcd1": "testusr%7C1680520365%7CjLSpN6oicRG4JezyfggqXD7j09S1JKnKNEDVVJz7PBt%7C8e87b96f92b57660594e5f61500adfdaaad60b821946d1fea9ec4ae84ddd8582", "wordpress_test_cookie": "WP%20Cookie%20check", "wordpress_logged_in_b2b6058102d675715ef9b7689e66fcd1": "testusr%7C1680520365%7CjLSpN6oicRG4JezyfggqXD7j09S1JKnKNEDVVJz7PBt%7Cfd58db2b7c2bc8bbb50b2e5ea89979d4c46e3a29d360c5947978ccfaeebdea68", "wp-settings-1": "mfold%3Do", "wp-settings-time-1": "1679909100"}
burp3_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "http://myhost123.test/wp-login.php?action=login", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
requests.get(burp3_url, headers=burp3_headers, cookies=burp3_cookies)

burp4_url = "http://myhost123.test:80/wp-admin/options-general.php"
burp4_cookies = {"wordpress_b2b6058102d675715ef9b7689e66fcd1": "testusr%7C1680520365%7CjLSpN6oicRG4JezyfggqXD7j09S1JKnKNEDVVJz7PBt%7C8e87b96f92b57660594e5f61500adfdaaad60b821946d1fea9ec4ae84ddd8582", "wordpress_test_cookie": "WP%20Cookie%20check", "wordpress_logged_in_b2b6058102d675715ef9b7689e66fcd1": "testusr%7C1680520365%7CjLSpN6oicRG4JezyfggqXD7j09S1JKnKNEDVVJz7PBt%7Cfd58db2b7c2bc8bbb50b2e5ea89979d4c46e3a29d360c5947978ccfaeebdea68", "wp-settings-1": "mfold%3Do", "wp-settings-time-1": "1679909100"}
burp4_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "http://myhost123.test/wp-admin/", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
requests.get(burp4_url, headers=burp4_headers, cookies=burp4_cookies)

burp5_url = "http://myhost123.test:80/wp-admin/options.php"
burp5_cookies = {"wordpress_b2b6058102d675715ef9b7689e66fcd1": "testusr%7C1680520365%7CjLSpN6oicRG4JezyfggqXD7j09S1JKnKNEDVVJz7PBt%7C8e87b96f92b57660594e5f61500adfdaaad60b821946d1fea9ec4ae84ddd8582", "wordpress_test_cookie": "WP%20Cookie%20check", "wordpress_logged_in_b2b6058102d675715ef9b7689e66fcd1": "testusr%7C1680520365%7CjLSpN6oicRG4JezyfggqXD7j09S1JKnKNEDVVJz7PBt%7Cfd58db2b7c2bc8bbb50b2e5ea89979d4c46e3a29d360c5947978ccfaeebdea68", "wp-settings-1": "mfold%3Do", "wp-settings-time-1": "1679909100"}
burp5_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "http://myhost123.test/wp-admin/options-general.php", "Content-Type": "application/x-www-form-urlencoded", "Origin": "http://myhost123.test", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
burp5_data = {"option_page": "general", "action": "update", "_wpnonce": "6a2b93e805", "_wp_http_referer": "/wp-admin/options-general.php", "blogname": "test site"+str(rd.randint(1,1000)), "blogdescription": '', "siteurl": "http://myhost123.test", "home": "http://myhost123.test", "new_admin_email": "testusr@gmail.com", "users_can_register": "1", "default_role": "subscriber", "timezone_string": "UTC+5", "date_format": "F j, Y", "date_format_custom": "F j, Y", "time_format": "g:i a", "time_format_custom": "g:i a", "start_of_week": "1", "submit": "Save Changes"}
requests.post(burp5_url, headers=burp5_headers, cookies=burp5_cookies, data=burp5_data)

burp6_url = "http://myhost123.test:80/wp-admin/options-general.php?settings-updated=true"
burp6_cookies = {"wordpress_b2b6058102d675715ef9b7689e66fcd1": "testusr%7C1680520365%7CjLSpN6oicRG4JezyfggqXD7j09S1JKnKNEDVVJz7PBt%7C8e87b96f92b57660594e5f61500adfdaaad60b821946d1fea9ec4ae84ddd8582", "wordpress_test_cookie": "WP%20Cookie%20check", "wordpress_logged_in_b2b6058102d675715ef9b7689e66fcd1": "testusr%7C1680520365%7CjLSpN6oicRG4JezyfggqXD7j09S1JKnKNEDVVJz7PBt%7Cfd58db2b7c2bc8bbb50b2e5ea89979d4c46e3a29d360c5947978ccfaeebdea68", "wp-settings-1": "mfold%3Do", "wp-settings-time-1": "1679909100"}
burp6_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "http://myhost123.test/wp-admin/options-general.php", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
requests.get(burp6_url, headers=burp6_headers, cookies=burp6_cookies)
