from es2 import CSVTimeSeriesFile



class ExamException(Exception):

    pass



class SequenceFinder:

    def __init__(self, data):

        if (not isinstance(data, list)) or data == []:

            raise ExamException('The datas are not of the right type\n')
        
        if len(data) < 2:

            raise ExamException("There are not enough info\n")

        self.data = data



    def find_longest_streak(self, direction):

        if direction == "up":

            dsf

        elif direction == "down":

            dsf

        else:

            raise ExamException("The inserted value is invalid\n")



    def find_threshold_crossing(self, threshold):

        dsf





tsf = CSVTimeSeriesFile(name='data.csv')

ts = tsf.get_data()

sf = SequenceFinder(ts)

streak = sf.find_longest_streak("up")
# {"start": "1949-06", "end": "1949-10",
# "length": 5, "values": [135, 148, 152, 160, 172]}

crossings = sf.find_threshold_crossings(200)
# [{"date": "1951-05", "direction": "up", "value": 204},
# {"date": "1952-01", "direction": "down", "value": 193}, ...]