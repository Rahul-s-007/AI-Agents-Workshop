from ping3 import ping

def get_response_time(url):
    response_time = ping(url)
    if response_time is None:
        return -1
    else:
        return response_time * 1000  # Convert to milliseconds

if __name__ == "__main__":
    url = "google.com"
    response_time = get_response_time(url)
    if response_time == -1:
        print(f"Failed to ping {url}")
    print(f"Average response time for {url}: {response_time:.2f} ms")

# def get_response_time(url):
#     if url == "google.com":
#         return 0.3
#     if url == "openai.com":
#         return 0.4
#     if url == "youtube.com":
#         return 0.5
#     else:
#         return 1.0