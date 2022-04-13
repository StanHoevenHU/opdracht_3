Recommendation rules

In deze opdracht heb ik 2 functies gemaakt die een aanbeveling kunnen maken op basis van de relationele database van opdracht 2.

De functie om een aanbeving te maken op basis van een product, zal 4 producten returnen die in de zelfde subcategorie zitten. 
Deze producten zullen worden gefilterd eerst op basis van de populairiteit. 
De 20 best verkopende producten worden apart genomen.
Deze producten worden daarna opnieuw gesorteerd op basis van de prijs om zo de goedkoopste producten te krijgen.

De functie om een aanbeveling te maken op basis van een profiel kan worden gemaak door te kijken naar de producten die door dat profiel zijn bekeken.
We kijken naar producten van die al zijn bekeken door de klant.
hierbij zoeken we profielen die dezelfde producten hebben bekeken. 
En selecteren de andere producten die deze profielen hebben bekeken.
Van deze producten pakken we weer de producten die het meest voorkomen.

Op deze manier krijg je de 2 verschillende recommendations waarbij je de data uit de relationele database omzet naar een lijst van 4 producten die je kan aanbevelen.