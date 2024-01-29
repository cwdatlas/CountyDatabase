import pandas as pd


# Validate county id. Primarily making sure its a string and within the correct range
def valid_county_int(county):
    try:
        int(county)
        if county in range(1, 56):
            return True
    except ValueError:
        return False


class county_database:
    def __init__(self):
        # loading csv into panda dataframe
        self.counties = pd.read_csv("MontanaCounties.csv")
        # Set 'License Plate Prefix' as the index of the DataFrame
        self.counties.set_index('License Plate Prefix', inplace=True)

    def run(self):
        print("Welcome to the County Database, type in licence plate prefix. from 1 to 56")
        print("Then enter either 'county' or 'cs' which stands for county seat")
        print("lastly type 'quit' to quit")
        county_loop = True
        while county_loop:
            county = input("1-56 ->")
            if county == 'quit':
                break
                # Makes sure that county if a valid int from 1 to 56
            if valid_county_int(county) is False:
                print("Please enter a number from 1 to 56 or quit")
                # now that county is a valid int, we can convert it to an int
            elif int(county) in self.counties.index:
                # safely get county number
                selected_county = self.counties.loc[int(county)]
                print("pick what data you want, county or (cs) county seat")
                # Get specific county data, either county name or county seat
                ctype_loop = True
                while ctype_loop:
                    ctype = input("county, cs ->")
                    if ctype == 'quit': # Always need quit
                        ctype_loop = False
                    if ctype == "county":
                        print(f"County queried: {selected_county.iloc[0]}")
                        ctype_loop = False
                    elif ctype == "cs":
                        print(f"County seat queried: {selected_county.iloc[1]}")
                        ctype_loop = False
                    else:
                        print("Please enter either county or cs")
            else:
                print("We could not find that county number, please try again")
