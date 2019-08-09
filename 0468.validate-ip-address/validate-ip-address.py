class Solution:
    def validIPAddress(self, IP: str) -> str:
        ipv4 = r'((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])'
        ipv6 = r'([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}'
        def check(rule):
            result = re.search(rule,IP)
            return result and result.group()==IP
        if check(ipv4) :return "IPv4"
        elif check(ipv6):return "IPv6"
        else:return "Neither"