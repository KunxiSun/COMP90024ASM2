##### CouchDB variables
couchdb_username = "admin"
couchdb_password = "admin"
couchdb_ip = "172.26.130.11"
couchdb_port = "5984"
couchdb_url = "http://%s:%s@%s:%s"%(couchdb_username,couchdb_password,couchdb_ip,couchdb_port) # don't change this variable
couchdb_name = "whole_au" 

##### Tweeter API keys
consumer_key = "2KYzayBTxaykRUmDrDgYWeW2D"
consumer_secret = "cKOLznQWR94ET3JcFGotUbvKJnckBVdwZazY9jhnp1eSNXSLTE" 
access_token = "1254697631600660480-12cqVeP49fcoL5RfmaDoeW0DjlRjvf" 
access_token_secret = "N0gfaDsqvwPlLVlRjGT0OSfWiJnMI9BRC9sSf6XfpBo8R" 
bearer_token = "AAAAAAAAAAAAAAAAAAAAAJa9PAEAAAAAfXT1jiOVkwBjum1E1H5q7T%2F5nIE%3DpLoB8Be1X1EhUG1sZQrrRZ5tOsd1CDXPkFAi7vuXJc4b0fPMNc"

##### Streaming API harvester variable
keywords = [""] 

##### Search API harvester variable
search_query = ""
search_since = "2016-01-01"
search_until = "2020-05-16"

#####  Australia Coodinates
#box_au = "112.5,-37.5,154.1,-12.8" 
box_melb = "143.947,-38.468,145.066,-36.882"
#box_syd = "150.6,-33.8,151.4,-33.3"
#https://www.mapdevelopers.com/draw-circle-tool.php
australia = '-29.1425,133.1389,2081km'
melbourne = '-37.7867,144.9082,100km'
sydney = '-33.8813,151.2128,100km'
brisbane = '-27.5394,153.1024,100km'
adelaide = '-34.9328,138.6444,100km'
perth = '-32.0379,115.8808,100km'

states = ['melbourne', 'sydney', 'brisbane', 'adelaide', 'perth']
states_geocodes = [melbourne, sydney, brisbane, adelaide, perth]


melbourne_city = "-37.8136,144.9631,4km"
City_of_Maroondah = '-37.8097,145.2591,3.9km'
City_of_Whitehorse = '-37.8286,145.1486,4km'
Yarra_Ranges_Shire = '-37.7451,145.7134,24.7km'
City_of_Bayside = '-37.9333,145.0163,3km'
Shire_of_Cardinia = '-38.1135,145.5802,17.9km'
City_of_Casey = '-38.1105,145.2922,10.08km'
City_of_Greater_Dandenong = '-38.0061,145.2038,5.7km'
City_of_Frankston= '-38.1404,145.1597,5.7km'
City_of_Glen_Eira = '-37.9035,145.0383,3.1km'
City_of_Kingston = '-37.9819,145.1045,4.77km'
City_of_Monash = "-37.9016,145.1155,4.5km"
Shire_of_Mornington_Peninsula = '-38.2854,145.0934,13.44km'
Towns_adjacent_to_Westernport = '-38.3563,145.2480,13.03km'
City_of_Stonnington = '-37.8596,145.0328,2.53km'
City_of_Brimbank = '-37.7595,144.8071,5.55km'
City_of_Hobsons_Bay = '-37.8361,144.8401,4km'
City_of_Maribyrnong = "-37.7951,144.8841,2.79km"
City_of_Melton = "-37.6882,144.6534,11.49km"
City_of_Moonee_Valley = "-37.7465,144.9061,3.28km"
City_of_Wyndham = '-37.9119,144.6534,11.64km'
City_of_Port_Phillip = '-37.8465,144.9667,2.27km'
City_of_Yarra = '-37.7979,144.9887,2.2km'
City_of_Banyule = '-37.7314,145.0824,3.96km'
City_of_Darebin = '-37.7278,145.0163,3.67km'
City_of_Hume = "-37.5987,144.8291,11.21km"
City_of_Moreland = "-37.7241,144.9502,3.57km"
Shire_of_Nillumbik = '-37.5977,145.2701,10.39km'
City_of_Whittlesea = "-37.5383,145.0934,11.06km"
City_of_Boroondara = '-37.8119,145.0714,3.87km'
City_of_Knox = '-37.8715,145.2480,5.34km'
City_of_Manningham = '-37.7669,145.1597,5.31km'

city_provinces = ['melbounre_city',
             'City_of_Maroondah',
            'City_of_Whitehorse',
            'Yarra_Ranges_Shire',
            'City_of_Bayside',
            'Shire_of_Cardinia',
            'City_of_Casey',
            'City_of_Greater_Dandenong',
            'City_of_Frankston',
            'City_of_Glen_Eira',
            'City_of_Kingston',
            'City_of_Monash',
            'Shire_of_Mornington_Peninsula',
            'Towns_adjacent_to_Westernport',
            'City_of_Stonnington',
            'City_of_Brimbank',
            'City_of_Hobsons_Bay',
            'City_of_Melton',
            'City_of_Moonee_Valley',
            'City_of_Wyndham',
            'City_of_Port_Phillip',
            'City_of_Yarra',
            'City_of_Banyule',
            'City_of_Darebin',
            'City_of_Hume',
            'City_of_Moreland',
            'Shire_of_Nillumbik',
            'City_of_Whittlesea',
            'City_of_Boroondara',
            'City_of_Knox',
            'City_of_Manningham']

geocodes = [melbourne_city,City_of_Maroondah,
            City_of_Whitehorse,Yarra_Ranges_Shire,City_of_Bayside,Shire_of_Cardinia,City_of_Casey,City_of_Greater_Dandenong,
            City_of_Frankston,City_of_Glen_Eira,City_of_Kingston,City_of_Monash,Shire_of_Mornington_Peninsula,Towns_adjacent_to_Westernport,
            City_of_Stonnington,City_of_Brimbank,City_of_Hobsons_Bay,City_of_Melton,City_of_Moonee_Valley,
            City_of_Wyndham,City_of_Port_Phillip,City_of_Yarra,City_of_Banyule,City_of_Darebin,City_of_Hume,City_of_Moreland,
            Shire_of_Nillumbik,City_of_Whittlesea,City_of_Boroondara,City_of_Knox,City_of_Manningham]

