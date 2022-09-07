# **1- Understanding the Problem and the Data:**
  Marketing is crucial for the growth and sustainability of retail business. By understanding the customer, marketers can launch a targeted marketing campaign that is tailored for specific needs. In this project, I tried to create an ad marketing campaign by dividing the customers of a company is Seattle, U.S into at least 3 distinctive groups.

The company has extensive data on their customers for the duration of 2.5 years and it has these different features:

- ORDERNUMBER: Identification of order placed
- QUANTITYORDERED: Number of items ordered
- PRICEEACH: Price of each item
- ORDERDATE: Date in which order is placed
- STATUS: Status of the order
- QTR_ID: Quarter in which order is placed
- Month_ID: Month in which order is placed
- Year_ID: Year in which order is placed
- PRODUCTLINE: Product Category
- CUSTOMMERNAME: Name of the customer
- PHONE: Phone number
- ADDRESSLINE1: Address to be shipped to
- ADDRESSLINE2: Address to be shipped to
- CITY: State in which customer resides
- POSTALCODE: Postal code in which culstomer resides
- COUNTRY: Country in whih customer resides
- TERRITORY: Territory in which customer resides
- DEALSIZE: Size of the order
- CONTACTFRISTNAME: Contact person's first name
- CONTACTLASTNAME: Contact person's last name

As we can see here, there's a lot of features that we can get rid of since they are not useful and they can for sure lower our model's performance. These features are:
- ['ADDRESSLINE1','ADDRESSLINE2','POSTALCODE','CITY','TERRITORY','PHONE','STATE','CONTACTFIRSTNAME','CONTACTLASTNAME','CUSTOMERNAME','ORDERNUMBER','ORDERDATE']

At the end of this step, we ended up with this Dataset:

![1](https://user-images.githubusercontent.com/103439643/188916330-a59a104c-a6b8-4202-a8d6-d6a6ae44019f.PNG)

# **2- Perform exploratory data analysis:**

In order to solve our problem which is trying to divide the customers of the company, we first need to try and understand our data very well. For that analysing and visualizing data is a necessity. So i used Tableau to create different Dashboards that can help me figure out what we need to do later on.

![Total_sales_Per_Country](https://user-images.githubusercontent.com/103439643/188928108-3bd29ec7-1bd6-4326-9f31-308fea84fe44.png)

Well here we can see that USA has the most sales among all countries, we can also see that Europe plays a huge role when it comes to sales.


![Status](https://user-images.githubusercontent.com/103439643/188928843-b828ad7e-b491-4a66-b8d6-7e0a5fea76c1.png)

Here we can see that our data is super unbalanced and it will have a huge impact later on that can lower the performance of our model. In this case we can't get more data and we also can't delete some rows of the data so the better option here is to drop this column.

![ProductLine](https://user-images.githubusercontent.com/103439643/188929489-3780b2dd-f580-422c-8a62-71828e53b243.png)

Here we can tell that cars are the most selled products, rather than that, everything seems cool and fine when it comes to this column so no major changes needed.

![Month_Sales](https://user-images.githubusercontent.com/103439643/188930206-e7ff8ffc-d1e1-4b8e-853d-3d88380a78f2.png)

Here we can tell that November has the highest sales each year, this might be a huge information since campaigns can be set around this month.

![1](https://user-images.githubusercontent.com/103439643/188930994-18ad83ee-a7b7-442c-8dca-cf55b1c472f8.PNG)

Here I used the correlation matrix to see if there's any other information i can collect and i find out that the QTR_ID and MONTH_ID features are collerated so i can drop definetly drop the QTR_ID column.

# **3- Creating the Model:**
## **A- K-Means Clustering Algorithm:**
K-means is an unsupervised laerning algorithm that works by grouping some data points together in an unsupervised fashion. The algorithm groups observations with similar attribute values together by measuring the Euclidian distance between points.

![0_ipBIcsy9jjvqEpbK](https://user-images.githubusercontent.com/103439643/188952482-7e63e3e1-d4dc-4547-90fc-96d05e5df2ae.png)

The steps of this algorithm are:
- K-Clusters(Centers) points are created at random locations
- Assign each data point to the nearest center
- The center points are moved to their means of their respective clusters
- step 2 and 3 are repeated until no observation changes.
