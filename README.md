# cheap_flight_search
Program that searchs for cheap flights to different locations and sends an email with the flights detail.

I've built this project for a Python course that I am doing and i'm very proud as it is one of my first projects done all by myself, that is why I am uploading it to GitHub.
In it I reviewed many concepts that i've been learning like Classes, HTTP requests, SMPT library, API's enpoints calling and a few more.

The idea of the project is to retrieve data from a Google Sheet (using Sheety API), that is: City name, city IATA Code and average price from "FROM_CITY" (in ths case is London but you can modify it so yu search from flights from your city) to that city, and then search for flights (Tequila API) to each destination in the next six months that are cheaper than the lowest price, if there is any.
If it found some cheaper flights, it sends you an email with the flights detail (price, departure time and arrival time) using the Twillio API.

As i said you can customize the departure city, the destination cities and the lowest price so you can make it even more functional. I've could done it myself but I currently have a cast in my right hand and i'm right handed so you can imagine how much i struggled to do this :).

Hope you like it, and if you have some better ideas (that you'll for sure have), just let me know.
Nacho
