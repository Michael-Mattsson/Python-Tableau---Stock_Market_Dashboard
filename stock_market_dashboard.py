 import pandas as pd

apple = pd.read_csv("AAPL.csv")
microsoft = pd.read_csv("MSFT.csv")
google = pd.read_csv("GOOGL.csv")
amazon = pd.read_csv("AMZN.csv")
nvidia = pd.read_csv("NVDA.csv")
tesla = pd.read_csv("TSLA.csv")
facebook = pd.read_csv("FB.csv")
broadcom = pd.read_csv("AVGO.csv")
asml = pd.read_csv("ASML.csv")
adobe = pd.read_csv("ADBE.csv")
pepsico = pd.read_csv("PEP.csv")
costco = pd.read_csv("COST.csv")
cisco = pd.read_csv("CSCO.csv")
netflix = pd.read_csv("NFLX.csv")
amd = pd.read_csv("AMD.csv")
pdd = pd.read_csv("PDD.csv")
starbucks = pd.read_csv("SBUX.csv")
mondelez = pd.read_csv("MDLZ.csv")
mercadolibre = pd.read_csv("MELI.csv")
monster = pd.read_csv("MNST.csv")
lululemon = pd.read_csv("LULU.csv")

dfs = [apple, microsoft, google, amazon, nvidia, tesla, facebook, broadcom, asml, adobe, pepsico, costco, cisco, netflix, amd, pdd, starbucks, mondelez, mercadolibre, monster, lululemon]

for df in dfs:
  df["MA50"] = df.Close.rolling(50).mean()
  df["MA200"] = df.Close.rolling(200).mean()

#####Check with apple.head(200) to see values for both 50 and 200
#####Check with apple.head() in between to see change

for df in dfs:
  df["Previous day close price"] = df.Close.shift(1)

for df in dfs:
  df["Change in price"] = df["Close"] - df["Previous day close price"]

for df in dfs:
  df["Percent change in price"] = df.Close.pct_change()

for df in dfs:
  df["Previous day volume"] = df.Volume.shift(1)

for df in dfs:
  df["Change in volume"] = df["Volume"] - df["Previous day volume"]

for df in dfs:
  df["Percent change in volume"] = df.Volume.pct_change()

##### Industry groupings

industry_mapping = {
    'apple.csv': 'Electronic Technology',
    'microsoft.csv': 'Technology Services',
    'google.csv': 'Technology Services',
    'amazon.csv': 'Retail',
    'nvidia.csv': 'Electronic Technology',
    'tesla.csv': 'Consumer Goods',
    'facebook.csv': 'Technology Services',
    'broadcom.csv': 'Electronic Technology',
    'asml.csv': 'Electronic Technology',
    'adobe.csv': 'Technology Services',
    'pepsico.csv': 'Consumer Goods',
    'costco.csv': 'Retail',
    'cisco.csv': 'Technology Services',
    'netflix.csv': 'Technology Services',
    'amd.csv': 'Electronic Technology',
    'pdd.csv': 'Retail',
    'starbucks.csv': 'Consumer Goods',
    'mondelez.csv': 'Consumer Goods',
    'mercadolibre.csv': 'Retail',
    'monster.csv': 'Consumer Goods',
    'lululemon.csv': 'Retail'
}

for df, filename in zip(dfs, ["apple.csv", "microsoft.csv", "google.csv", "amazon.csv", "nvidia.csv", 
                              "tesla.csv", "facebook.csv", "broadcom.csv", "asml.csv", "adobe.csv", 
                              "pepsico.csv", "costco.csv", "cisco.csv", "netflix.csv", "amd.csv", 
                              "pdd.csv", "starbucks.csv", "mondelez.csv", "mercadolibre.csv", 
                              "monster.csv", "lululemon.csv"]):
    df["Industry"] = industry_mapping[filename]

##### Check with apple.head()










