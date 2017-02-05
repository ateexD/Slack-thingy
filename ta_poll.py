from slacker import Slacker
#slack=Slacker('xoxp-109406689664-110788867926-127737250370-d01039ce30fad5d82e8aaeb8ff4580f0')
slack=Slacker('xoxp-111399271671-111408077911-128780231495-a35ef316f291cea3401b6909a06438c0')
ch_id=slack.channels.get_channel_id("botbot")
print (ch_id)
slack.chat.command(channel=ch_id,command="/poll",text='"TA Availabilities" "Monday" "Tuesday" "Wednesday" "Thursday" "Friday" "Saturday" "Sunday"')#,asuser=True)
