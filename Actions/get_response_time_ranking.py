def get_response_time_ranking(response_time):
    if response_time <= 7.5:
        return 1
    if response_time <= 15:
        return 2
    if response_time > 15:
        return 3

if __name__ == "__main__":
    response_time = 11
    print(f"Response time: {response_time} ms")
    print(f"Response time ranking: {get_response_time_ranking(response_time)}")

# def get_response_time_ranking(response_time):
#     if response_time == 0.1:
#         return 1
#     if response_time == 0.2:
#         return 2
#     if response_time == 0.3:
#         return 3
#     else:
#         return 4