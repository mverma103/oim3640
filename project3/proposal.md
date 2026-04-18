## My Project Proposal

**What I'm building:** 

I am building a Flask web app that allows a user to enter a place name/address and find the nearest MBTA stop using the Mapbox Geocoding API and the MBTA API

**Why I chose this:** 

This project will help me with being able to build web apps using flask, and being able to leverage many API's to access real live data, something we haven't combined together. It's really practical and combining these learnings with web development into one project makes it more interesting than writing a script into terminal. I also like that this project could solve a real problem by helping someone quickly find the nearest T stop from a location

**Core features:** 

- A hoempage where the user can enter a place name/address
- Use the Mapbox API to convert the place into latitude and longitude
- Use the MBTA API to find the nearest station based on those coordinates
- Display to the user the nearest stop name
- Display to the user whether its wheelchair accessible
- Make sure that it can bypass keyerror from invalid location/addresses or no stops nearby

**What I don't know yet:**

- How the MBTA API response is structured and how to find the correct stop data
- How to display a Mapbox map inside an HTML page
- how to structure the project with Flask routes.