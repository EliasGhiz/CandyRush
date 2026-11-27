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

## Schema
### Open Food Facts

- **Number of Columns:** 211
- As a group, we decided the 9 columns listed below will be the most useful to make our statement. These nine columns have the most important data to make a good comparison between goods sold in different countries and their correlation to the happiness scale.

### Open Food Facts

| Column | Data Type | Description |
|---|---|---|
| `code` | String | Product id |
| `product_name` | String | Name of product |
| `categories_tags` | String | Category of product |
| `countries_tags` | String | Countries where the product is sold |
| `ingredients_tags` | String | Ingredients in the product |
| `sugars_100g` | Double | Grams of sugar per 100 grams |
| `additives_n` | Integer | Number of additives in the product |
| `additives_tags` | String | Types of additives in the product |
| `nova_group` | Integer | Level of food processing 1-4 scale |

### World Happiness Report

| Column | Data Type | Description |
|---|---|---|
| `Year` | Integer | Year of observation |
| `Rank` | Integer | National happiness ranking |
| `Country name` | String | Name country |
| `Life evaluation (3-year average)` | Double | Average national happiness over three years |
| `Lower whisker` | Double | Lower confidence interval bound |
| `Upper whisker` | Double | Upper confidence interval bound |
| `Log GDP per capita` | Double | Contribution of GDP per capita to happiness |
| `Social support` | Double | Contribution of social support to happiness |
| `Healthy life expectancy` | Double | Healthy life expectancy |
| `Freedom to make life choices` | Double | Personal freedom |
| `Generosity` | Double | Generosity |
| `Perceptions of corruption` | Double | Perceived corruption |
| `Dystopia + residual` | Double | Baseline happiness plus unexplained variation |

### Repo Structure

```text
├── README.md
├── requirements.txt
├── data/
│   ├── open_food_facts.csv
│   └── world_happiness.xlsx
└── notebooks/
│   └── 01_create_write_candy_happiness_rdds.ipynb
```
