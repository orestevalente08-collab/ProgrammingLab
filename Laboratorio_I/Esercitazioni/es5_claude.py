class ExamException(Exception):
    pass

class CSVDataFile:
    def __init__(self, name):
        if not isinstance(name, str):
            raise ExamException("The value is not a string\n")
        else:
            self.name  = name
    
    def get_data(self):
        try:
            with open(self.name, 'r') as f:
                next(f)
                lines = []
                counter = 0
                for line in f:
                    line = line.strip()
                    line = line.split(',')
                    lines.append(line)
                    if len(line)>2:
                        raise ExamException("The current line don't have 2 items\n")
                for line in lines:
                    for idx, item in enumerate(line):
                        if item == '':
                            line[idx] = 0
                            continue
                        try:
                            counter +=1
                            line[idx] = float(item)
                        except ValueError:
                            print("Found a not-numerical data\n")
                            continue
                    if counter<2:
                        raise ExamException("There are not such numerical datas\n")
                return lines
        except FileNotFoundError:
            raise ExamException("File not found\n")


class LinearRegression:
    def __init__(self, data):
        self.data =  data
        self.cov_xy = 0
        self.var_x = 0
        self.var_y = 0
        self.m = None
        self.q = None

    def get_r_squared(self):
        try:
            r = self.cov_xy/(self.var_x**(1/2)*self.var_y**(1/2))
            return r**2
        except ZeroDivisionError:
            return "Variation of y is zero\n"

    def fit(self):
        sum_x = 0
        sum_y = 0
        sum_xy = 0
        length = 0
        print(self.data)
        for items in self.data:
            try:
                sum_x += items[0]
                sum_y += items[1]
                sum_xy += items[0]*items[1]
                length += 1
            except TypeError:
                continue
        mean_x = sum_x/length
        mean_y = sum_y/length
        mean_xy = sum_xy/length
        for items in self.data:
            try:
                self.var_x = self.var_x + (items[0]-mean_x)**2
                self.var_y = self.var_y + (items[1] - mean_y)**2
            except TypeError:
                continue
        self.cov_xy = mean_xy-mean_x*mean_y
        self.m = self.cov_xy/self.var_x
        self.q = mean_y - self.m*mean_x

    def predict(self, x):
        if not isinstance(x, float or int):
            raise ExamException("The value is not numeric\n")
        if self.m == None:
            raise ExamException("You must to call fit() first\n")
        else:
            return self.m*x+self.q

data_file = CSVDataFile(name='data_5.csv')
data = data_file.get_data()
model = LinearRegression(data)
model.fit()
print(model.predict(5.0)) # es. 23.7
print(model.get_r_squared()) # es. 0.94
