class Solution(object):
    def validIPAddress(self, IP):
        if ':' in IP and '.' not in IP:
            items = IP.split(':')
            if len(items) != 8 or '' in items:
                return 'Neither'
            for item in items:
                if len(item) > 4:
                    return 'Neither'
                for each in item:
                    if each.lower() not in string.hexdigits:
                        return 'Neither'
            return 'IPv6'
            
            
        elif '.' in IP and ':' not in IP: 
            items = IP.split('.')
            if len(items) != 4:
                return 'Neither'
            else:
                for item in items:
                    try:
                        item_num = int(item)
                    except ValueError:
                        return 'Neither'
                    if item_num > 255 or item_num < 0:
                        return 'Neither'
                    item_string = str(item_num)
                    if item_string != item:
                        return 'Neither'
                return 'IPv4'
        else:
            return 'Neither'