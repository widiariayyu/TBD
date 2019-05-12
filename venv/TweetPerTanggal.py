class TweetPerTanggal(object):
    def __init__(self, created_at):
        self.created_at = created_at
        self.total_tweet = 0
        self.total_retweet = 0
        self.total_fav = 0