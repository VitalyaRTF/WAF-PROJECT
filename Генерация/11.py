import requests

burp0_url = "http://192.168.1.3:80/"
burp0_cookies = {"wordpress_test_cookie": "WP%20Cookie%20check"}
burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)

burp1_url = "http://myhost123.test:80/wp-login.php?action=login"
burp1_cookies = {"wordpress_test_cookie": "WP%20Cookie%20check", "wp_lang": "en_US", "wp-settings-1": "mfold%3Do", "wp-settings-time-1": "1679554361", "wordpress_logged_in_b2b6058102d675715ef9b7689e66fcd1": "testusr%7C1680080602%7CzPNgDlNzK28mjNsR7eQ1ec2grrju3rZx3k8ZpBZijk5%7C989d8a6034c593f2f2ba44c86c319675eb916c340867feb81385f9a7a7a40b14"}
burp1_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "DNT": "1", "Connection": "close", "Referer": "http://192.168.1.3/", "Upgrade-Insecure-Requests": "1"}
requests.get(burp1_url, headers=burp1_headers, cookies=burp1_cookies)

burp2_url = "http://myhost123.test:80/wp-login.php"
burp2_cookies = {"wordpress_test_cookie": "WP%20Cookie%20check", "wp_lang": "en_US", "wp-settings-1": "mfold%3Do", "wp-settings-time-1": "1679554361", "wordpress_logged_in_b2b6058102d675715ef9b7689e66fcd1": "testusr%7C1680080602%7CzPNgDlNzK28mjNsR7eQ1ec2grrju3rZx3k8ZpBZijk5%7C989d8a6034c593f2f2ba44c86c319675eb916c340867feb81385f9a7a7a40b14"}
burp2_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "http://myhost123.test/wp-login.php?action=login", "Content-Type": "application/x-www-form-urlencoded", "Origin": "http://myhost123.test", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
burp2_data = {"log": "testusr", "pwd": "Cpp123321#", "wp-submit": "Log In", "redirect_to": "http://myhost123.test/wp-admin/", "testcookie": "1"}
requests.post(burp2_url, headers=burp2_headers, cookies=burp2_cookies, data=burp2_data)

burp3_url = "http://myhost123.test:80/wp-admin/"
burp3_cookies = {"wordpress_b2b6058102d675715ef9b7689e66fcd1": "testusr%7C1680080718%7CQqm35PUpJQl2bY8ddXglJxOBxgn41Hi2tafuIg2X8qO%7C467f917cb78a76358080ef8b41126d6ebeebe08b4ec23816bd31d2c946bac268", "wordpress_test_cookie": "WP%20Cookie%20check", "wp_lang": "en_US", "wp-settings-1": "mfold%3Do", "wp-settings-time-1": "1679554361", "wordpress_logged_in_b2b6058102d675715ef9b7689e66fcd1": "testusr%7C1680080718%7CQqm35PUpJQl2bY8ddXglJxOBxgn41Hi2tafuIg2X8qO%7C60b7aa8da58ff8fe35c0ab7f3707fa7a884cc2b31bb33fca82cbc959980ddda0"}
burp3_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "http://myhost123.test/wp-login.php?action=login", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
requests.get(burp3_url, headers=burp3_headers, cookies=burp3_cookies)

burp4_url = "http://myhost123.test:80/wp-admin/plugins.php"
burp4_cookies = {"wordpress_b2b6058102d675715ef9b7689e66fcd1": "testusr%7C1680080718%7CQqm35PUpJQl2bY8ddXglJxOBxgn41Hi2tafuIg2X8qO%7C467f917cb78a76358080ef8b41126d6ebeebe08b4ec23816bd31d2c946bac268", "wordpress_test_cookie": "WP%20Cookie%20check", "wp_lang": "en_US", "wp-settings-1": "mfold%3Do", "wp-settings-time-1": "1679554361", "wordpress_logged_in_b2b6058102d675715ef9b7689e66fcd1": "testusr%7C1680080718%7CQqm35PUpJQl2bY8ddXglJxOBxgn41Hi2tafuIg2X8qO%7C60b7aa8da58ff8fe35c0ab7f3707fa7a884cc2b31bb33fca82cbc959980ddda0"}
burp4_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "http://myhost123.test/wp-admin/", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
requests.get(burp4_url, headers=burp4_headers, cookies=burp4_cookies)

burp5_url = "http://myhost123.test:80/wp-admin/plugins.php?action=activate&plugin=akismet%2Fakismet.php&plugin_status=all&paged=1&s&_wpnonce=6547228d70"
burp5_cookies = {"wordpress_b2b6058102d675715ef9b7689e66fcd1": "testusr%7C1680080718%7CQqm35PUpJQl2bY8ddXglJxOBxgn41Hi2tafuIg2X8qO%7C467f917cb78a76358080ef8b41126d6ebeebe08b4ec23816bd31d2c946bac268", "wordpress_test_cookie": "WP%20Cookie%20check", "wp_lang": "en_US", "wp-settings-1": "mfold%3Do", "wp-settings-time-1": "1679554361", "wordpress_logged_in_b2b6058102d675715ef9b7689e66fcd1": "testusr%7C1680080718%7CQqm35PUpJQl2bY8ddXglJxOBxgn41Hi2tafuIg2X8qO%7C60b7aa8da58ff8fe35c0ab7f3707fa7a884cc2b31bb33fca82cbc959980ddda0"}
burp5_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "http://myhost123.test/wp-admin/plugins.php", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
requests.get(burp5_url, headers=burp5_headers, cookies=burp5_cookies)

burp6_url = "http://myhost123.test:80/wp-admin/plugins.php?activate=true&plugin_status=all&paged=1&s="
burp6_cookies = {"wordpress_b2b6058102d675715ef9b7689e66fcd1": "testusr%7C1680080718%7CQqm35PUpJQl2bY8ddXglJxOBxgn41Hi2tafuIg2X8qO%7C467f917cb78a76358080ef8b41126d6ebeebe08b4ec23816bd31d2c946bac268", "wordpress_test_cookie": "WP%20Cookie%20check", "wp_lang": "en_US", "wp-settings-1": "mfold%3Do", "wp-settings-time-1": "1679554361", "wordpress_logged_in_b2b6058102d675715ef9b7689e66fcd1": "testusr%7C1680080718%7CQqm35PUpJQl2bY8ddXglJxOBxgn41Hi2tafuIg2X8qO%7C60b7aa8da58ff8fe35c0ab7f3707fa7a884cc2b31bb33fca82cbc959980ddda0"}
burp6_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "http://myhost123.test/wp-admin/plugins.php", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
requests.get(burp6_url, headers=burp6_headers, cookies=burp6_cookies)

burp7_url = "http://myhost123.test:80/wp-admin/options-general.php?page=akismet-key-config&view=start"
burp7_cookies = {"wordpress_b2b6058102d675715ef9b7689e66fcd1": "testusr%7C1680080718%7CQqm35PUpJQl2bY8ddXglJxOBxgn41Hi2tafuIg2X8qO%7C467f917cb78a76358080ef8b41126d6ebeebe08b4ec23816bd31d2c946bac268", "wordpress_test_cookie": "WP%20Cookie%20check", "wp_lang": "en_US", "wp-settings-1": "mfold%3Do", "wp-settings-time-1": "1679554361", "wordpress_logged_in_b2b6058102d675715ef9b7689e66fcd1": "testusr%7C1680080718%7CQqm35PUpJQl2bY8ddXglJxOBxgn41Hi2tafuIg2X8qO%7C60b7aa8da58ff8fe35c0ab7f3707fa7a884cc2b31bb33fca82cbc959980ddda0"}
burp7_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "http://myhost123.test/wp-admin/plugins.php", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
requests.get(burp7_url, headers=burp7_headers, cookies=burp7_cookies)

burp8_url = "http://myhost123.test:80/wp-admin/plugins.php"
burp8_cookies = {"wordpress_b2b6058102d675715ef9b7689e66fcd1": "testusr%7C1680080718%7CQqm35PUpJQl2bY8ddXglJxOBxgn41Hi2tafuIg2X8qO%7C467f917cb78a76358080ef8b41126d6ebeebe08b4ec23816bd31d2c946bac268", "wordpress_test_cookie": "WP%20Cookie%20check", "wp_lang": "en_US", "wp-settings-1": "mfold%3Do", "wp-settings-time-1": "1679554361", "wordpress_logged_in_b2b6058102d675715ef9b7689e66fcd1": "testusr%7C1680080718%7CQqm35PUpJQl2bY8ddXglJxOBxgn41Hi2tafuIg2X8qO%7C60b7aa8da58ff8fe35c0ab7f3707fa7a884cc2b31bb33fca82cbc959980ddda0"}
burp8_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
requests.get(burp8_url, headers=burp8_headers, cookies=burp8_cookies)

burp9_url = "http://myhost123.test:80/wp-admin/plugins.php?action=deactivate&plugin=akismet%2Fakismet.php&plugin_status=all&paged=1&s&_wpnonce=886fb2095e"
burp9_cookies = {"wordpress_b2b6058102d675715ef9b7689e66fcd1": "testusr%7C1680080718%7CQqm35PUpJQl2bY8ddXglJxOBxgn41Hi2tafuIg2X8qO%7C467f917cb78a76358080ef8b41126d6ebeebe08b4ec23816bd31d2c946bac268", "wordpress_test_cookie": "WP%20Cookie%20check", "wp_lang": "en_US", "wp-settings-1": "mfold%3Do", "wp-settings-time-1": "1679554361", "wordpress_logged_in_b2b6058102d675715ef9b7689e66fcd1": "testusr%7C1680080718%7CQqm35PUpJQl2bY8ddXglJxOBxgn41Hi2tafuIg2X8qO%7C60b7aa8da58ff8fe35c0ab7f3707fa7a884cc2b31bb33fca82cbc959980ddda0"}
burp9_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "http://myhost123.test/wp-admin/plugins.php", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
requests.get(burp9_url, headers=burp9_headers, cookies=burp9_cookies)

burp10_url = "http://myhost123.test:80/wp-admin/plugins.php?deactivate=true&plugin_status=all&paged=1&s="
burp10_cookies = {"wordpress_b2b6058102d675715ef9b7689e66fcd1": "testusr%7C1680080718%7CQqm35PUpJQl2bY8ddXglJxOBxgn41Hi2tafuIg2X8qO%7C467f917cb78a76358080ef8b41126d6ebeebe08b4ec23816bd31d2c946bac268", "wordpress_test_cookie": "WP%20Cookie%20check", "wp_lang": "en_US", "wp-settings-1": "mfold%3Do", "wp-settings-time-1": "1679554361", "wordpress_logged_in_b2b6058102d675715ef9b7689e66fcd1": "testusr%7C1680080718%7CQqm35PUpJQl2bY8ddXglJxOBxgn41Hi2tafuIg2X8qO%7C60b7aa8da58ff8fe35c0ab7f3707fa7a884cc2b31bb33fca82cbc959980ddda0"}
burp10_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "http://myhost123.test/wp-admin/plugins.php", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
requests.get(burp10_url, headers=burp10_headers, cookies=burp10_cookies)
