import csv

from gridref2latlng import gridref2latlng

CSV_IN = '../NO2_Edinburgh_2008-2012_simplified.csv'
CSV_OUT = '../NO2_Edinburgh_2008-2012.csv'




def main():
    
    
    with open(CSV_IN) as csvfile:
        
        reader = csv.reader(csvfile)
        next(reader)
        
        csv_out = []
        
        
        for line in reader:
            (easting, northing, aqma, to_kerb, year, NO2) = line               
            lat, lng = gridref2latlng(float(easting), float(northing), verbose=False)
            csv_out.append([lat, lng, year, NO2])
            
    with open(CSV_OUT, 'w') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['latitude', 'longitude', 'year', 'NO2'])
        writer.writerows(csv_out) 
        print('Writing text to %s' % CSV_OUT)
        
            

if __name__ == "__main__":
    main() 

