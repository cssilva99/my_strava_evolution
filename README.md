# my_strava_evolution
As a developer I want to "webscrap" Strava data from my own endpoint, so that I can analyse the evolution of my pace, avg and max heart rate ❤️

Backend (server.py):

Add Strava API credentials to .env
Create token storage/refresh endpoints
Create activities sync endpoint
Create analytics endpoints for pace/HR evolution

Frontend:

Update index.css with design system (dark theme, fonts)
Create landing page with Strava connect
Create dashboard with charts (Recharts)
Create activity list component
Add date range filters

Files to create:

Backend: server.py (rewrite)
Frontend: App.js, App.css, index.css + components

Features Implemented:

Pace Evolution Chart: Interactive line chart showing pace (min/km) trends over time with average reference line
Heart Rate Charts: Dual-line chart tracking both Max HR and Average HR evolution

Activity Dashboard:

Summary cards (total activities, distance, avg pace, avg HR), filterable activity list with sport type badges

Filters: Date range picker (calendar), sport type dropdown (Run, Ride, Swim, Walk)
Strava Integration: OAuth token management with auto-refresh

