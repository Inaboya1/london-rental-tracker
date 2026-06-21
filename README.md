Investigating rental affordability across London boroughs.
# London Rental Affordability Tracker
An interactive dashboard exploring how rent compares to local wages
across London boroughs, using real property listing data and
ONS wage estimates.
## Live Demo
https://london-rental-tracker-6peoepudfbgl232fkbz9fm.streamlit.app/
If you work in London and earn the median local wage, what percentageof your salary would go toward rent in each borough, and where in London is rent genuinely unaffordable relative to local pay?
# Datasets
Kaggle: London House Price Data (property listings, rent and sale estimates, January 2025)
ONS: Annual Survey of Hours and Earnings, borough-level median pay(2023 estimates)
# Key findings
Wandsworth has the highest rent-to-income ratio at 72%
Tower Hamlets is the most affordable at 59.1%
98.8% of London properties exceed the 30% affordability stress threshold
The median London property requires 14.3 years of median local salary to purchase
# Methodology
Properties were matched to boroughs via outcode using a custom lookup table. Affordability ratio = (median monthly rent / median monthly wage) x 100. Only properties with HIGH confidence sale estimates and complete rent/wage data were included. Boroughs with fewer than 50 matched properties were excluded to avoid unreliable small-sample averages.
# Limitations
Wage data is from 2023; property data is from January 2025 which has 1-2 year gap existing between the two sources
The dataset over-represents outer London outcodes relative to prime central areas
Outcode-to-borough mapping covers 98.0% of properties; the remainder were excluded from borough-level analysis