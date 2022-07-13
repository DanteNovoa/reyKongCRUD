yt_api_key = "AIzaSyBFIyJ4s2bXbcKr_j2-c5-bk_e6VDhu28s"
channel_id = "UC0LrrCe2_jeRd3pepoLQ9Hw"
import pyyoutube

def get_channel_info():
    yt_client = pyyoutube.Api(api_key=yt_api_key)
    channel = yt_client.get_channel_info(channel_id=channel_id)
    channel_info = channel.items[0].to_dict()
    print(channel_info['statistics']['subscriberCount'])
    return channel_info['statistics']['subscriberCount']