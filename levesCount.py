import pandas as pd
import numpy
import pandas
import matplotlib.pyplot as plt

class AccionLogAnalyser:
    
    def __init__(self):
        self.levels = ['INFO', 'DEBUG', 'SEVERE', 'ERROR']
        self.file_location = "Desktop/python/data.csv"
        self.schema = ['timestamp', 'host', 'level', 'message']
        self.df = pd.read_csv(self.file_location, names=self.schema)

    def createDF(self):
        return self.df
        
    def level_count(self, df):
        counts = []
        for lev in self.levels:
            out = df[df.level == lev].count()
            counts.append(out['level'])
            
        return self.levels, counts
    
    def timestamp_level_count(self, df):
        df = df[df.level == 'ERROR']
        out = df.groupby('timestamp')
        out1 = out.count()
        keys = list(out.groups.keys())
        out2 = out1['level']
        values = list(out2)
    
        return keys, values
        
def main():
    log_obj = AccionLogAnalyser()
    df = log_obj.createDF()
    levels, counts = log_obj.level_count(df)
    print(levels, counts)
    plt.bar(levels, counts, color="gbmr") 
    plt.show()
    
        
if __name__ == '__main__':
    main()
    
    
    
    
    
------------------------------------------------------------------------------------------
    
log_obj = AccionLogAnalyser()
df = log_obj.createDF()
timestamp, counts = log_obj.timestamp_level_count(df)
plt.plot(timestamp, counts) 
plt.show()