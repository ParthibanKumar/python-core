# Getting started¶
# To use pandas, you'll typically start with the following line of code.

# Creating data
# There are two core objects in pandas: the DataFrame and the Series.

# DataFrame
# A DataFrame is a table. It contains an array of individual entries, each of which has a certain value. Each entry corresponds to a row (or record) and a column.

# For example, consider the following simple DataFrame:

import pandas as pd

df = pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})

df = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})

df = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']}, 
                  index=["User A", "User B"])


# Series¶
# A Series, by contrast, is a sequence of data values. If a DataFrame is a table, a Series is a list. And in fact you can create one with nothing more than a list:

df = pd.Series([1,2,3,4])

df = pd.Series([30, 35, 40], 
               index=['2015 Sales', '2016 Sales', '2017 Sales'], 
               name='Product A')


# Reading data files¶
# Being able to create a DataFrame or Series by hand is handy. But, most of the time, we won't actually be creating our own data by hand. Instead, we'll be working with data that already exists.


# wine_reviews = pd.read_csv("data\input\csv\winemag-data-130k-v2.csv", 
#                            delimiter=",",
#                             usecols=["country", "points", "price", "variety", "winery"] )

# wine_reviews = pd.read_csv("data\input\csv\winemag-data-130k-v2.csv", nrows=0 )

wine_reviews = pd.read_csv("data\input\csv\winemag-data-130k-v2.csv")

# print(wine_reviews.shape)

# subset_wine_review = wine_reviews[["country"]]

# print(list(wine_reviews.columns))
# print(wine_reviews.shape)
# print(subset_wine_review.head())

# print(wine_reviews['country'][::-1])

# print(wine_reviews.loc[0:1])

# print(wine_reviews.iloc[0:5,[1,2,5]])

# print(wine_reviews.loc[0:5, "country"])

# print(wine_reviews.loc[0:10, [ "country", "points", "price" ]])

# print(wine_reviews[wine_reviews["price"] > 100])

# print(wine_reviews.[[-5]]iloc["price"])
# wine_reviews = wine_reviews.drop(columns="province")
# print(wine_reviews.columns)

# print(wine_reviews["country"] == "Italy")
# print(wine_reviews.country == "Italy")
# print(wine_reviews.loc[(wine_reviews.country == "Italy") | (wine_reviews.points >= 90)])

# print(wine_reviews.loc[wine_reviews.country.isin(["Italy", "France"])])

# print(wine_reviews.country.isin(["Italy", "France"]))

# print(wine_reviews.price.notnull())
# print(wine_reviews["description"])
# print(wine_reviews.loc[[0, 1, 10, 100], ["country", "province", "region_1", "region_2"]])

# print(wine_reviews[wine_reviews.points >= 95 & wine_reviews.country.isin(["Australia", "New Zealand"])])

# print(wine_reviews.points.mean())

# double = lambda x: x *2
# print(double(22))

# words = ["banana", "fig", "apple"]
# print(sorted(words, key=lambda w: len(w)))

def to_stars(point):
    return point / 20

wine_reviews["stars"]  = wine_reviews.points.map(lambda p: p / 2)
# wine_reviews["country_upper"] = wine_reviews.country.map(lambda c: c.upper())
# print(wine_reviews.head(5))

# print(wine_reviews.country.isna().head())

# wine_reviews["country_upper"] = wine_reviews.country.fillna("UNKNOWN").map(lambda c: c.upper())

# print(wine_reviews.country.isna().isna().sum())

# wine_reviews["ratio"] = wine_reviews.points / wine_reviews.price

# print(wine_reviews.ratio)

# print(wine_reviews[["title", "points", "price", "ratio"]].head())

# best_row = wine_reviews.ratio.idxmax()

# print(wine_reviews.loc[best_row, "title"])

# n_topical = wine_reviews.description.str.contains("tropical").sum()
# n_fruity = wine_reviews.description.str.contains("fruity").sum()
# print(n_fruity, n_topical)
# descriptor_counts = pd.Series({
#     "tropical":n_topical, "fruity":n_fruity
# })

# descriptor_counts = pd.Series({
#     word: wine_reviews.description.str.contains(word).sum()
#     for word in ["tropical", "fruity"]
# })

# print(descriptor_counts)


def stars(row):
    if row.country == "Canada":
        return 3
    elif row.points >= 95:
        return 3
    elif row.points >=85:
        return 2
    else:
        return 1

star_rating = wine_reviews.apply(stars, axis=1)
# print(star_rating)


# print(wine_reviews.groupby("country").price.median())

# print(wine_reviews.groupby("taster_twitter_handle").taster_twitter_handle.count().max())

# print(wine_reviews.groupby("price")["points"].max().sort_index())

# price_extreme = wine_reviews.groupby("variety")["price"].agg(['min', 'max'])

# print(price_extreme.sort_values(by=["min", "max"],ascending=False))

# print(wine_reviews.groupby("taster_name")["points"].mean())

# print(wine_reviews.groupby(["country", "variety"]).size())

# wine_reviews["points"]=wine_reviews["points"].astype('float64')

# wine_reviews["points"]=wine_reviews.points.astype('float64')
# print(wine_reviews[["points"]])

# print(wine_reviews[pd.isnull(wine_reviews["country"])])
# print(pd.isnull(wine_reviews["country"]).size)
# print(wine_reviews.region_2.fillna("Unknown"))

# print(wine_reviews.points.to_string())

wine_reviews["region_1"] = wine_reviews["region_1"].fillna("Wnknown")
# print(wine_reviews["region_1"])
# print(wine_reviews.groupby("region_1")["region_1"].count())

wine_reviews = wine_reviews.rename(columns={"points":"score"})

print(wine_reviews.columns)