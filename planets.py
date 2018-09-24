def weight_on_planets():
    message = "What do you weigh on earth? "
    earth_weight = int(input(message))
    mars_scalar = .38
    jupiter_scalar = 2.34
    mars_weight = earth_weight * mars_scalar
    jupiter_weight = earth_weight * jupiter_scalar
    fmt_stmt = "On {} you would weigh {} pounds."
    print("\n" + fmt_stmt.format("Mars", mars_weight) + "\n" + 
        (fmt_stmt.format("Jupiter", jupiter_weight)))   
   
   
if __name__ == '__main__':
   weight_on_planets()
