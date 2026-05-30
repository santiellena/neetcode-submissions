class TimeMap:
    hm = {}
    timestamps = {int}
    def __init__(self):
        self.hm = {}
        self.timestamps = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hm[key + str(timestamp)] = value
        old_timestamps = self.timestamps.get(key, [])
        old_timestamps.append(timestamp)
        self.timestamps[key] = old_timestamps

    def get(self, key: str, timestamp: int) -> str:
        timestamps = self.timestamps.get(key, [])

        if len(timestamps) == 0:
            return ""
        
        if self.hm.get(key + str(timestamp), -1) != -1:
            return self.hm[key + str(timestamp)]

        closest_timestamp = 0

        l, r = 0, len(timestamps) - 1

        while l <= r:
            m = (l + r) // 2

            if timestamps[m] > timestamp:
                r = m - 1
            else:
                if abs(closest_timestamp - timestamp) > abs(timestamps[m] - timestamp):
                    closest_timestamp = timestamps[m]
                l = m + 1
                

        if closest_timestamp == 0:
            return ""
        else:
            return self.hm[key + str(closest_timestamp)]        
        
        
