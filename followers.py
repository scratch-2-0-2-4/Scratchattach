import scratchattach as sa
import time

cloud = sa.get_tw_cloud(1325289772)

while True:
    user = sa.get_user("Scratch_2_0_2_4")
    followers = int(user.follower_count())

    cloud.set_var("followers", followers)
    time.sleep(10)
