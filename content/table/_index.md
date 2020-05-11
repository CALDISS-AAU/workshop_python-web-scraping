---
title: "Table"
weight: 20
---

```python
#Indlæs data
import pandas as pd
ess = pd.read_csv('https://github.com/CALDISS-AAU/workshop_python-table-data/raw/master/data/ESS2014DK_subset.csv')
```


```python
#Inspicer første 5 rækker af pandas dataframe
ess.head()
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>idno</th>
      <th>ppltrst</th>
      <th>happy</th>
      <th>health</th>
      <th>cgtsday</th>
      <th>alcfreq</th>
      <th>height</th>
      <th>weight</th>
      <th>gndr</th>
      <th>yrbrn</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>921018</td>
      <td>6</td>
      <td>9</td>
      <td>Very good</td>
      <td>10.0</td>
      <td>2-3 times a month</td>
      <td>178.0</td>
      <td>64.0</td>
      <td>Male</td>
      <td>1990</td>
    </tr>
    <tr>
      <td>1</td>
      <td>921026</td>
      <td>8</td>
      <td>8</td>
      <td>Very good</td>
      <td>NaN</td>
      <td>Several times a week</td>
      <td>172.0</td>
      <td>64.0</td>
      <td>Female</td>
      <td>1948</td>
    </tr>
    <tr>
      <td>2</td>
      <td>921034</td>
      <td>8</td>
      <td>8</td>
      <td>Good</td>
      <td>NaN</td>
      <td>Every day</td>
      <td>176.0</td>
      <td>87.0</td>
      <td>Male</td>
      <td>1957</td>
    </tr>
    <tr>
      <td>3</td>
      <td>921076</td>
      <td>8</td>
      <td>8</td>
      <td>Good</td>
      <td>NaN</td>
      <td>Several times a week</td>
      <td>162.0</td>
      <td>70.0</td>
      <td>Female</td>
      <td>1958</td>
    </tr>
    <tr>
      <td>4</td>
      <td>921084</td>
      <td>5</td>
      <td>8</td>
      <td>Very good</td>
      <td>NaN</td>
      <td>Every day</td>
      <td>175.0</td>
      <td>80.0</td>
      <td>Male</td>
      <td>1936</td>
    </tr>
  </tbody>
</table>