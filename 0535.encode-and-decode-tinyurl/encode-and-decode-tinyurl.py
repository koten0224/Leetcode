class Codec:

    def __init__(self):
        self.subway = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.body = {}
    def encode(self,url):
        tiny = "http://tinyurl.com/"+''.join(self.subway[random.randint(0,61)] for _ in range(6))
        self.body[tiny] = url
        return tiny
    def decode(self,url):
        return self.body[url]