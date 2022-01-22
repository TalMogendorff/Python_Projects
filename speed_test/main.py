import speedtest

test = speedtest.Speedtest()

print("Loading Server list...")
test.get_servers()
print("Choosing best Server...")
best = test.get_best_server()

print(f"Found: {best['host']} located in {best['country']}")

print("Checking for your download test...")
download_result = test.download()
print("Checking for your upload test")
upload_result = test.upload()
ping_result = test.results.ping

print('\nThe result are : \n')
print(f"Donwload Speed: {download_result / 1024 / 1024 :.2f} Mbit/s")
print(f"Upload Speed: {upload_result / 1024 / 1024 :.2f} Mbit/s")
print(f"Ping: {ping_result:.2f}ms")

