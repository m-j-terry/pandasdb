# Who are we?
 My name is Michael. I am a (former) educator, software developer, writer, and social activist. 

 My partner Magdalena and I began a journey in November of 2019. We had been dumpster diving around Brooklyn and Manhattan since 2018 when we decided to create an instagram account to document the quantity (and quality) of all the things we were finding in the trash. Toothpaste. Candy bars. Razors. Feminine hygeine products. Crackers and other dry goods. Holiday goods. And so much more!

 When we made our instagram, I also started a [spreadsheet](https://docs.google.com/spreadsheets/d/e/2PACX-1vQGM2bcNxW9mAuIU95k3llQI_n396jS7gEC-2j7huUvP8ctfU_OlkSygpK2A3uA2kjIphcQX8L_oJ6p/pubhtml) to document the total value of everything we were pulling from the trash—six nights a week, 52 weeks a year!

 While we have not posted on our instagram in quite sometime nor have we updated our spreadsheet, the 'data' we collected was monumental. Just the two of us checking a couple of stores' dumpsters each night were able to document over $150,000 of wasted goods in the year and a half we collected data, which was more than our combined income at the time! We didn't sell any of it. We 'redistributed' it out to friends and across our community at work and to our community through neighborhood fridges/pantries and directly off our stoop. 

 But if this is the trend for small cornerstore CVS' and Walgreens in the little sliver of New York that we covered each night, imagine this trend magnified across the city, the country, the entire global market. 

 Adam Smith, the father of classical economics, theorized that the entire market was guided by an invisible hand that (through aggregating supply to meet demand) could collect all of the bits of local knowledge about demand that are dispersed throughout the economy and transmute them into material prosperity and create the most effecient economic system in human history. 
 
 So what is happening to all of those bits of local knowledge? Are they actually able to transform themselves into the products and goods that people need? Not really. Instead, they wind up in the landfill while people wonder where their next meal will come from or else have to decide between having food and making rent. Of course, credit card companies make it possible to afford rent and groceries; though they only help resolve this issue by tightening the vice around your neck.

 The scope of this project is to expose the waste inherent in capitalism and its consequences and to start to conceive of the new way forward.

# What is this?
 This repository contains the server file for populating the TrashPandas SQL database from the excel sheet documenting the waste we found in dumpsters from November 2019 through (roughly) June 2021.

 It is part of a larger project I am undertaking to make our 'data' more interactive, accessible, and presentable. It is also an excuse to experiment with new langauges and services in my programming!

## How it works
### workbook.py 
- Workbook organizes the data from the spreadsheet into Class objects (Item and Corporation). Item has the properties of date, name, defects, units, price, and total (which is units * price). The Corporation object has a name and a list. 
- Workbook goes through each sheet in the master spreadsheet and creates an instance of the Corporation Class for the corporation and then iterates through the sheet, creating an instace of the Item Class for each item in the sheet and appending it to the Corporation Class's list each time. 
- Once all of the Items are stored in their corresponding Corporation, all of the Corporations are packaged into an array and returned to be manipulated by the server.py file, where they will be integrated into the SQL server. 

### server.py
- The list of Corporation objects (which contain lists of Item objects) are then destructured and queried into a table whose title is the corporation.name and whose contents are the contents are the same as that of the Item Class. 
- After all the Corporation tables have been populated from the Class objects, the total value of wasted goods from each corporation is calculated and stored in the Grand_Totals table. 
- Lastly, the totals from each of the Corporations are themselves summed and added to the Grand_Totals table as Grand_Total. 

Stay tuned for the TrashPandas website!
To learn more in the meantime, check us out on Instagram!
![https://www.instagram.com/trash.pandas_ofnyc/?hl=en](https://lh3.googleusercontent.com/proxy/oNTjoYoASVVlr1vNFTgSzwT2EQFTuUJCYnosh07q1rQbeIihL4kfL1_Z23HMD6t4trzV7kL0giLscs3Yehs9HDxj_QJQGE2eRMasjTErFxxn_dHDAaxGWTZWkVropxPm0v9d5ngpPcDfS9BQPMJKiaU0pzKI_nCIOJSDLKB4Oa9K4uLrDIvR)