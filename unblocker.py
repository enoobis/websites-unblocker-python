import time

# list of websites to block
websites_to_block = ["www.facebook.com", "www.youtube.com", "www.twitter.com"]

# host file location (for Windows it is C:\Windows\System32\drivers\etc\hosts)
hosts_file = "C:\Windows\System32\drivers\etc\hosts"

while True:
    with open(hosts_file, 'r+') as file:
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any(website in line for website in websites_to_block):
                file.write(line)
            file.truncate()
    print("All websites are now unblocked.")
    time.sleep(5)