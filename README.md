# Candy Rush

## Team Members

- Kira Baker
- Elias Ghiz
- Christopher Snook
- Rishi Burt-Iyer

## Problem Statment

Our group is investigating whether candy sold in a country (with parameters like sugar, ingredients, additives, processing level) is correlated or associated with the country’s happiness rate. True purchased candy data is proprietary, so we plan to use the countries where each candy product is being sold as a stand in for availability, and we acknowledge this as a limitation.

## Data Sources with URL and Description

### Open Food Facts

- **URL:** https://world.openfoodfacts.org/data
- **Size:** 15 GB
- **Description:** Crowd-sourced global food products, which we will filter to only candy in our project. Has 88 columns with information such as url, creator, quantities, origins, cities, etc, and then an additional 100 columns of additives and ingredients columns.

### World Happiness Report

- **URL:** https://worldhappiness.report/data
- **Description:** Has 13 columns with features like Year, Rank, Country Name, and explanatory reasoning columns.

### Open Food Facts

| Column | Data Type |
|---|---|
| `code` | String |
| `product_name` | String |
| `categories_tags` | String |
| `countries_tags` | String |
| `ingredients_tags` | String |
| `sugars_100g` | Double |
| `additives_n` | Integer |
| `additives_tags` | String |
| `nova_group` | Integer |

### World Happiness Report

| Column | Data Type |
|---|---|
| `Year` | Integer |
| `Rank` | Integer |
| `Country name` | String |
| `Life evaluation (3-year average)` | Double |
| `Log GDP per capita` | Double |
| `Social support` | Double |
| `Healthy life expectancy` | Double |
| `Freedom to make life choices` | Double |
| `Generosity` | Double |
| `Perceptions of corruption` | Double |

### Repo Structure

```text
├── README.md
├── requirements.txt
├── data/
│   ├── open_food_facts.csv
│   └── world_happiness.xlsx
└── notebooks/
```
