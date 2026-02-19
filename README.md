# Source Code & Language

The two Python scripts have been tested using and each of them has been transformed into a Python standard (.py) in the present repository.

The library Matplotlib has been used to output the Linear Regressions by each of the 3 sports : 
- swimming 🏊‍♂️
- running 🏃‍♀️
- riding 🚴‍♀️ 

(Thriathlon)

## Script 1 :
- Absolute Values
  (Raw from Strava)
  
## Script 2 :
- Heart Rate vs Pace
  (Efficiency)
  
  It's a Linear Regression

# To be implemented

1. Read the comments of a given Strava activity from the endpoint :
  
- GET /activities/{id}/comments

4. Use emojis parser
   - Emojis are Unicode
   - I would like to use Python to parse them as well

5. If I find a free LLM, the 3rd feature I'd like to implement is a Humor Heatmap

In which days am I happier?

Note to self : Should I do a PCA Analysis to separate variables (I am happier because it's Friday , I'm happy for something else)

4. Github Actions for automation

I would like GitHub Actions to execute these 2 Python scripts, and "ingress" the linear regression chart as a .png or .html to the GCP Artifact Registry -> 0,5 GB 
(500 MB) of Free Storage
