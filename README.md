
### Import WTO_Chrono


```python
from WTO_Chrono import Chrono
```

### Make an Instance using Chrono( )


```python
chrono = Chrono()
```

### Run .chrono_pandas(  ) in created instance


```python
chrono.chrono_pandas() #take a while, around 3min
```

# Done : check your result using .df


```python
chrono.df
```
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>complainant</th>
      <th>consultation_requested</th>
      <th>curr_stat</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>DS1</th>
      <td>Malaysia — Prohibition of Imports of Polyethyl...</td>
      <td>SINGAPORE</td>
      <td>10 JANUARY 1995</td>
      <td>SETTLED OR TERMINATED (WITHDRAWN, MUTUALLY AGR...</td>
    </tr>
    <tr>
      <th>DS2</th>
      <td>United States — Standards for Reformulated and...</td>
      <td>VENEZUELA, BOLIVARIAN REPUBLIC OF</td>
      <td>24 JANUARY 1995</td>
      <td>IMPLEMENTATION NOTIFIED BY RESPONDENT</td>
    </tr>
    <tr>
      <th>DS3</th>
      <td>Korea, Republic of — Measures Concerning the T...</td>
      <td>UNITED STATES</td>
      <td>4 APRIL 1995</td>
      <td>IN CONSULTATIONS</td>
    </tr>
    <tr>
      <th>DS4</th>
      <td>United States — Standards for Reformulated and...</td>
      <td>BRAZIL</td>
      <td>10 APRIL 1995</td>
      <td>IMPLEMENTATION NOTIFIED BY RESPONDENT</td>
    </tr>
    <tr>
      <th>DS5</th>
      <td>Korea, Republic of — Measures Concerning the S...</td>
      <td>UNITED STATES</td>
      <td>3 MAY 1995</td>
      <td>SETTLED OR TERMINATED (WITHDRAWN, MUTUALLY AGR...</td>
    </tr>
    <tr>
      <th>DS6</th>
      <td>United States — Imposition of Import Duties on...</td>
      <td>JAPAN</td>
      <td>17 MAY 1995</td>
      <td>SETTLED OR TERMINATED (WITHDRAWN, MUTUALLY AGR...</td>
    </tr>
    <tr>
      <th>DS7</th>
      <td>European Communities — Trade Description of Sc...</td>
      <td>CANADA</td>
      <td>19 MAY 1995</td>
      <td>SETTLED OR TERMINATED (WITHDRAWN, MUTUALLY AGR...</td>
    </tr>
    <tr>
      <th>DS8</th>
      <td>Japan — Taxes on Alcoholic Beverages</td>
      <td>EUROPEAN COMMUNITIES</td>
      <td>21 JUNE 1995</td>
      <td>MUTUALLY ACCEPTABLE SOLUTION ON IMPLEMENTATION...</td>
    </tr>
    <tr>
      <th>DS9</th>
      <td>European Communities — Duties on Imports of Ce...</td>
      <td>CANADA</td>
      <td>30 JUNE 1995</td>
      <td>PANEL ESTABLISHED, BUT NOT YET COMPOSED</td>
    </tr>
    <tr>
      <th>DS10</th>
      <td>Japan — Taxes on Alcoholic Beverages</td>
      <td>CANADA</td>
      <td>7 JULY 1995</td>
      <td>MUTUALLY ACCEPTABLE SOLUTION ON IMPLEMENTATION...</td>
    </tr>
    <tr>
      <th>DS11</th>
      <td>Japan — Taxes on Alcoholic Beverages</td>
      <td>UNITED STATES</td>
      <td>7 JULY 1995</td>
      <td>MUTUALLY ACCEPTABLE SOLUTION ON IMPLEMENTATION...</td>
    </tr>
    <tr>
      <th>DS12</th>
      <td>European Communities — Trade Description of Sc...</td>
      <td>PERU</td>
      <td>18 JULY 1995</td>
      <td>SETTLED OR TERMINATED (WITHDRAWN, MUTUALLY AGR...</td>
    </tr>
    <tr>
      <th>DS13</th>
      <td>European Communities — Duties on Imports of Gr...</td>
      <td>UNITED STATES</td>
      <td>19 JULY 1995</td>
      <td>SETTLED OR TERMINATED (WITHDRAWN, MUTUALLY AGR...</td>
    </tr>
    <tr>
      <th>DS14</th>
      <td>European Communities — Trade Description of Sc...</td>
      <td>CHILE</td>
      <td>24 JULY 1995</td>
      <td>SETTLED OR TERMINATED (WITHDRAWN, MUTUALLY AGR...</td>
    </tr>
    <tr>
      <th>DS15</th>
      <td>Japan — Measures Affecting the Purchase of Tel...</td>
      <td>EUROPEAN COMMUNITIES</td>
      <td>18 AUGUST 1995</td>
      <td>IN CONSULTATIONS</td>
    </tr>
    <tr>
      <th>DS16</th>
      <td>European Communities — Regime for the Importat...</td>
      <td>GUATEMALA; HONDURAS; MEXICO; UNITED STATES</td>
      <td>28 SEPTEMBER 1995</td>
      <td>SETTLED OR TERMINATED (WITHDRAWN, MUTUALLY AGR...</td>
    </tr>
    <tr>
      <th>DS17</th>
      <td>European Communities — Duties on Imports of Rice</td>
      <td>THAILAND</td>
      <td>5 OCTOBER 1995</td>
      <td>IN CONSULTATIONS</td>
    </tr>
    <tr>
      <th>DS18</th>
      <td>Australia — Measures Affecting Importation of ...</td>
      <td>CANADA</td>
      <td>5 OCTOBER 1995</td>
      <td>MUTUALLY ACCEPTABLE SOLUTION ON IMPLEMENTATION...</td>
    </tr>
    <tr>
      <th>DS19</th>
      <td>Poland — Import Regime for Automobiles</td>
      <td>INDIA</td>
      <td>28 SEPTEMBER 1995</td>
      <td>SETTLED OR TERMINATED (WITHDRAWN, MUTUALLY AGR...</td>
    </tr>
    <tr>
      <th>DS20</th>
      <td>Korea, Republic of — Measures concerning Bottl...</td>
      <td>CANADA</td>
      <td>8 NOVEMBER 1995</td>
      <td>SETTLED OR TERMINATED (WITHDRAWN, MUTUALLY AGR...</td>
    </tr>
    <tr>
      <th>DS21</th>
      <td>Australia — Measures Affecting the Importation...</td>
      <td>UNITED STATES</td>
      <td>20 NOVEMBER 1995</td>
      <td>SETTLED OR TERMINATED (WITHDRAWN, MUTUALLY AGR...</td>
    </tr>
    <tr>
      <th>DS22</th>
      <td>Brazil — Measures Affecting Desiccated Coconut</td>
      <td>PHILIPPINES</td>
      <td>30 NOVEMBER 1995</td>
      <td>REPORT(S) ADOPTED, NO FURTHER ACTION REQUIRED</td>
    </tr>
    <tr>
      <th>DS23</th>
      <td>Venezuela, Bolivarian Republic of — Anti-Dumpi...</td>
      <td>MEXICO</td>
      <td>5 DECEMBER 1995</td>
      <td>SETTLED OR TERMINATED (WITHDRAWN, MUTUALLY AGR...</td>
    </tr>
    <tr>
      <th>DS24</th>
      <td>United States — Restrictions on Imports of Cot...</td>
      <td>COSTA RICA</td>
      <td>22 DECEMBER 1995</td>
      <td>IMPLEMENTATION NOTIFIED BY RESPONDENT</td>
    </tr>
    <tr>
      <th>DS25</th>
      <td>European Communities — Implementation of the U...</td>
      <td>URUGUAY</td>
      <td>14 DECEMBER 1995</td>
      <td>IN CONSULTATIONS</td>
    </tr>
    <tr>
      <th>DS26</th>
      <td>European Communities — Measures Concerning Mea...</td>
      <td>UNITED STATES</td>
      <td>26 JANUARY 1996</td>
      <td>MUTUALLY ACCEPTABLE SOLUTION ON IMPLEMENTATION...</td>
    </tr>
    <tr>
      <th>DS27</th>
      <td>European Communities — Regime for the Importat...</td>
      <td>ECUADOR; GUATEMALA; HONDURAS; MEXICO; UNITED S...</td>
      <td>5 FEBRUARY 1996</td>
      <td>SETTLED OR TERMINATED (WITHDRAWN, MUTUALLY AGR...</td>
    </tr>
    <tr>
      <th>DS28</th>
      <td>Japan — Measures Concerning Sound Recordings</td>
      <td>UNITED STATES</td>
      <td>9 FEBRUARY 1996</td>
      <td>SETTLED OR TERMINATED (WITHDRAWN, MUTUALLY AGR...</td>
    </tr>
    <tr>
      <th>DS29</th>
      <td>Turkey — Restrictions on Imports of Textile an...</td>
      <td>HONG KONG, CHINA</td>
      <td>12 FEBRUARY 1996</td>
      <td>IN CONSULTATIONS</td>
    </tr>
    <tr>
      <th>DS30</th>
      <td>Brazil — Countervailing Duties on Imports of D...</td>
      <td>SRI LANKA</td>
      <td>23 FEBRUARY 1996</td>
      <td>IN CONSULTATIONS</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>DS509</th>
      <td>China — Duties and other Measures concerning t...</td>
      <td>EUROPEAN UNION</td>
      <td>19 JULY 2016</td>
      <td>PANEL ESTABLISHED, BUT NOT YET COMPOSED</td>
    </tr>
    <tr>
      <th>DS510</th>
      <td>United States — Certain Measures Relating to t...</td>
      <td>INDIA</td>
      <td>9 SEPTEMBER 2016</td>
      <td>PANEL ESTABLISHED, BUT NOT YET COMPOSED</td>
    </tr>
    <tr>
      <th>DS511</th>
      <td>China — Domestic Support for Agricultural Prod...</td>
      <td>UNITED STATES</td>
      <td>13 SEPTEMBER 2016</td>
      <td>PANEL COMPOSED</td>
    </tr>
    <tr>
      <th>DS512</th>
      <td>Russian Federation — Measures Concerning Traff...</td>
      <td>UKRAINE</td>
      <td>14 SEPTEMBER 2016</td>
      <td>PANEL COMPOSED</td>
    </tr>
    <tr>
      <th>DS513</th>
      <td>Morocco — Anti-Dumping Measures on Certain Hot...</td>
      <td>TURKEY</td>
      <td>3 OCTOBER 2016</td>
      <td>PANEL COMPOSED</td>
    </tr>
    <tr>
      <th>DS514</th>
      <td>United States — Countervailing Measures on Col...</td>
      <td>BRAZIL</td>
      <td>11 NOVEMBER 2016</td>
      <td>IN CONSULTATIONS</td>
    </tr>
    <tr>
      <th>DS515</th>
      <td>United States — Measures Related to Price Comp...</td>
      <td>CHINA</td>
      <td>12 DECEMBER 2016</td>
      <td>IN CONSULTATIONS</td>
    </tr>
    <tr>
      <th>DS516</th>
      <td>European Union — Measures Related to Price Com...</td>
      <td>CHINA</td>
      <td>12 DECEMBER 2016</td>
      <td>PANEL COMPOSED</td>
    </tr>
    <tr>
      <th>DS517</th>
      <td>China — Tariff Rate Quotas for Certain Agricul...</td>
      <td>UNITED STATES</td>
      <td>15 DECEMBER 2016</td>
      <td>PANEL ESTABLISHED, BUT NOT YET COMPOSED</td>
    </tr>
    <tr>
      <th>DS518</th>
      <td>India — Certain Measures on Imports of Iron an...</td>
      <td>JAPAN</td>
      <td>20 DECEMBER 2016</td>
      <td>PANEL COMPOSED</td>
    </tr>
    <tr>
      <th>DS519</th>
      <td>China — Subsidies to Producers of Primary Alum...</td>
      <td>UNITED STATES</td>
      <td>12 JANUARY 2017</td>
      <td>IN CONSULTATIONS</td>
    </tr>
    <tr>
      <th>DS520</th>
      <td>Canada — Measures Governing the Sale of Wine i...</td>
      <td>UNITED STATES</td>
      <td>18 JANUARY 2017</td>
      <td>IN CONSULTATIONS</td>
    </tr>
    <tr>
      <th>DS521</th>
      <td>European Union — Anti-Dumping Measures on Cert...</td>
      <td>RUSSIAN FEDERATION</td>
      <td>27 JANUARY 2017</td>
      <td>IN CONSULTATIONS</td>
    </tr>
    <tr>
      <th>DS522</th>
      <td>Canada — Measures Concerning Trade in Commerci...</td>
      <td>BRAZIL</td>
      <td>8 FEBRUARY 2017</td>
      <td>PANEL ESTABLISHED, BUT NOT YET COMPOSED</td>
    </tr>
    <tr>
      <th>DS523</th>
      <td>United States — Countervailing Measures on Cer...</td>
      <td>TURKEY</td>
      <td>8 MARCH 2017</td>
      <td>PANEL COMPOSED</td>
    </tr>
    <tr>
      <th>DS524</th>
      <td>Costa Rica — Measures Concerning the Importati...</td>
      <td>MEXICO</td>
      <td>8 MARCH 2017</td>
      <td>IN CONSULTATIONS</td>
    </tr>
    <tr>
      <th>DS525</th>
      <td>Ukraine — Measures relating to Trade in Goods ...</td>
      <td>RUSSIAN FEDERATION</td>
      <td>19 MAY 2017</td>
      <td>IN CONSULTATIONS</td>
    </tr>
    <tr>
      <th>DS526</th>
      <td>United Arab Emirates — Measures Relating to Tr...</td>
      <td>QATAR</td>
      <td>31 JULY 2017</td>
      <td>PANEL ESTABLISHED, BUT NOT YET COMPOSED</td>
    </tr>
    <tr>
      <th>DS527</th>
      <td>Bahrain, Kingdom of — Measures Relating to Tra...</td>
      <td>QATAR</td>
      <td>31 JULY 2017</td>
      <td>IN CONSULTATIONS</td>
    </tr>
    <tr>
      <th>DS528</th>
      <td>Saudi Arabia, Kingdom of — Measures Relating t...</td>
      <td>QATAR</td>
      <td>31 JULY 2017</td>
      <td>IN CONSULTATIONS</td>
    </tr>
    <tr>
      <th>DS529</th>
      <td>Australia — Anti-Dumping Measures on A4 Copy P...</td>
      <td>INDONESIA</td>
      <td>1 SEPTEMBER 2017</td>
      <td>IN CONSULTATIONS</td>
    </tr>
    <tr>
      <th>DS530</th>
      <td>Kazakhstan — Anti-dumping Measures on Steel Pipes</td>
      <td>UKRAINE</td>
      <td>19 SEPTEMBER 2017</td>
      <td>IN CONSULTATIONS</td>
    </tr>
    <tr>
      <th>DS531</th>
      <td>Canada — Measures Governing the Sale of Wine i...</td>
      <td>UNITED STATES</td>
      <td>28 SEPTEMBER 2017</td>
      <td>IN CONSULTATIONS</td>
    </tr>
    <tr>
      <th>DS532</th>
      <td>Russian Federation — Measures Concerning the I...</td>
      <td>UKRAINE</td>
      <td>13 OCTOBER 2017</td>
      <td>IN CONSULTATIONS</td>
    </tr>
    <tr>
      <th>DS533</th>
      <td>United States — Countervailing Measures on Sof...</td>
      <td>CANADA</td>
      <td>28 NOVEMBER 2017</td>
      <td>IN CONSULTATIONS</td>
    </tr>
    <tr>
      <th>DS534</th>
      <td>United States — Anti-Dumping Measures Applying...</td>
      <td>CANADA</td>
      <td>28 NOVEMBER 2017</td>
      <td>IN CONSULTATIONS</td>
    </tr>
    <tr>
      <th>DS535</th>
      <td>United States — Certain Systemic Trade Remedie...</td>
      <td>CANADA</td>
      <td>20 DECEMBER 2017</td>
      <td>IN CONSULTATIONS</td>
    </tr>
    <tr>
      <th>DS536</th>
      <td>United States — Anti-Dumping Measures on Fish ...</td>
      <td>VIET NAM</td>
      <td>8 JANUARY 2018</td>
      <td>IN CONSULTATIONS</td>
    </tr>
    <tr>
      <th>DS537</th>
      <td>Canada — Measures Governing the Sale of Wine</td>
      <td>AUSTRALIA</td>
      <td>12 JANUARY 2018</td>
      <td>IN CONSULTATIONS</td>
    </tr>
    <tr>
      <th>DS538</th>
      <td>Pakistan — Anti-Dumping Measures on Biaxially ...</td>
      <td>UNITED ARAB EMIRATES</td>
      <td>24 JANUARY 2018</td>
      <td>IN CONSULTATIONS</td>
    </tr>
  </tbody>
</table>
<p>538 rows × 4 columns</p>
</div>



### Don't forget to Save It


```python
df.to_csv("~/wto.csv") #or the file is already on github
```
