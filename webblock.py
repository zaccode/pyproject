import datetime as dt
import time as tm
end_time = dt.datetime(2022,8,31)

site_block = ["www.instagram.com","themoviezflix.net"]
host_path = "C:/Windows/System32/drivers/etc/hosts"
redirect = "127.0.0.1"

while True:
    if dt.datetime.now() < end_time:
        print("Start Blocking")
        with open(host_path,"r+")  as host_file:
            content = host_file.read()
            for site in site_block:
                if site not in content:
                    host_file.write(redirect + " " + site)
                
                else:
                    pass
    else:
         with open(host_path,"r+")  as host_file:
            content = host_file.readlines()
            host_file.seek(0)
            for lines in content:
                if not any(site in lines for site in site_block):
                    host_file.write(lines)
            host_file.truncate()

         tm.sleep(5)

