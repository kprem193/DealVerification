from __future__ import unicode_literals, print_function

import plac
import random
from pathlib import Path
import spacy

def find_str(s, char):
    index = 0

    if char in s:
        c = char[0]
        for ch in s:
            if ch == c:
                if s[index:index+len(char)] == char:
                    return index

            index += 1

    return -1
# new entity label
LABEL1 = 'fund'
LABEL2 = 'amount'
LABEL3 = 'account'
LABEL4 = 'type'
LABEL5 = 'saccountto'
LABEL6 = 'saccountfrom'
a=[]
TRAIN_DATA = [
("hi im sammy from fil how can i help you i am weasly i want to sell fifty percent in a fuming fund  okay it amounts to ten thousand pounds sounds good so may i confirm your details before you place the deal yes sure what is your full name weasly walnut what is the first line of your address and the pincode peter residency public pittensburg one one zero zero  what is the last ffour numbers of the card registered one two five nine of american express yes so i want to read the deal for you i confirm that i want to sell fifty percent of fuming fund which is worth ten thousand pounds from my account one two three four five fix seven yes perfect ",{
'entities':[(539,550,'fund'),(566,585,'amount'),(602,635,'account'),(517,521,'type')]
}),
("hi im jim from fidelity im smith i want to invest in fansy fund an amount of fifty thousand pounds okay so let me confirm that for you i confirm that i want to invest an of amount fifty thousand in the fansy fund in the account four five six seven agreed cool any further assistance no thank you ",{
'entities':[(210,215,'fund'),(180,202,'amount'),(236,255,'account'),(160,166,'type')]
}),

("im sandy from xyz limited I want to take out money which have invested in the fund golden children I want to remove seventy five percent of it the seventy five percent amounts to sixteen thousand pounds ok then before the deal is placed can you confirm your identity what is the id that has been assigned to you its four three four four okay do u have a bank account linked with your account no so the amount would be given by a cheque sound fine for me okay let me confirm the contents of your deal you want to take out seventy five percent of your share worth sixteen thousand pounds from account five nine five six three perfect okay any more assistance needed no",{
'entities':[(561,576,'fund'),(619,643,'amount'),(602,635,'account'),(512,520,'type')]
}),

("hi joe i want to place a switch deal from fund swiggy to fund zomato i want the whole amount in swiggy to be transferred okay let us first confirm your identity may i have your full name joseph jenny can i have the last four digits the registered bank account okay its three six six six its of charteted bank okay so you want to place a switch deal from swiggy fund to zomato fund worth fifty thousand pounds with account number six eight three two yes agreed so do you want any more details no",{
'entities':[(337,343,'type'),(387,408,'amount'),(369,375,'saccountto'),(354,360,'saccountfrom'),(429,448,'account')]
}),


("hey you are speaking to aman how can i assist you i am sen calling from tech corp limited i have to purchase a share in south north fund worth ten thousand pounds okay so you wish to have a deal reference yes the deal reference is one five nine six okay let me repeat this for u i hereby declare that i am placing a purchase deal  worth fifty thousand pounds  in the fund south north with account number one five nine six okay this deal will be placed within next twenty four hours",{
'entities':[(372,383,'fund'),(337,358,'amount'),(404,421,'account'),(316,324,'type')]
}),


("hey hai im tina how can i assist you can you make a sell deal worth fourty five percentage of my share in the fund development fund ok for this you need to confirm your identity first tell your complete name telly tina can i have your last four digits of your account number four seven nine zero two it belongs to citicorp bank yup so now we can proceed with the deal it amounts to sixty five thousand do you need any further assistance no fine i confirm that you want to sell forty percent from fund development which is worth sixty five thousand and the account number is one three five nine okay okay",{
'entities':[(501,512,'fund'),(528,547,'amount'),(574,593,'account'),(472,476,'type')]
}),


("you are speaking to rick how can i assist you i am smith from dell limited i want to withdraw my hundred percent funds from swer fund and invest fifty thousand pounds in swop fund we would like you to confirm your details before placing the deal may we have your company corp id one two three four six can we have your details  of the registered bank number just the last  four  digits seven six five eight nine fine its perfect we can proceed with deal so i will read back the details for you the i here by confirm that i want to invest fifty thousand pounds in swop fund with account number four five six seven and withdraw my hundred percent share from swer fund worth sixty six thousand pounds with account number nine nine eight eight yup its correct this deal will be placed in the next bidding hour okay thank you thankyou",{
'entities':[(563,567,'fund'),(538,559,'amount'),(593,612,'account'),(531,537,'type'),(656,660,'fund'),(672,697,'amount'),(718,739,'account'),(617,625,'type')]
}),


("hello you are speaking to jimmy how can i help you i am jennifer i want to move my hundred percent amount in fund intel to fund reliance that’s fine do you need any other details no so can i confirm your deal to transfer funds worth fourteen  thousand fifteen pounds with the associated account number five one one two from intel fund to reliance fund ",{
'entities':[(233,266,'amount'),(303,318,'account'),(212,220,'type'),(324,329,'saccountfrom'),(338,346,'saccountto')]
}),


("hi im calling from dredo corporation my name is smurf hey you are talking to david how can i help you i want to redeem my ninety percent from innovo fund ohk can you confirm your identity can you share details of your full name and your unique  id im smurf blue with associated id five eight eight eight nine fine lets proceed with the deal kindly provide the declaration i confirm that i want to redeem my ninety percent from innovo fund worth sum of five hundred one pounds where six eight nine two is account number fine its okay good bye",{
'entities':[(432,438,'fund'),(452,475,'amount'),(482,500,'account'),(397,403,'type')]
}),


("ron at this side how can i help you im simon i want to buy in graff fund worth ninety  thousand pounds ohk so any other details needed no all are fine kindly confirm your deal i declare that i want to buy in graff fund a sum of ninety thousand pounds and account number is one two three four five yes cool okay then lets proceed any other assistance needed guess yes when will this deal be placed deal will be confirmed in the next confirmation hours",{
'entities':[(208,213,'fund'),(228,250,'amount'),(273,296,'account'),(201,204,'type')]
}),


("hello this is george im here to assist you im kimmy i am looking to redeem my whole share in foundation fund let me assist you with that first confirm identity before tell me your first line of address its lane 717 chichago sounds fine may i know your account number just last four number eight seven three zero its perfect the whole share amounts to seventy three thousand pounds three cents sounds good okay the deal takes place in the next available session ok let me confirm the deal for you i hereby confirm that i want to redeem my hundred percent share in foundation fund worth seventy three thousand pounds three cents yup that’s it okay okay",{
'entities':[(563,573,'fund'),(585,626,'amount'),(634,652,'account'),(528,534,'type')]
}),

("you are speaking to tom rider from fidelity im kate from vlc limited i wish to make a few transactions okay let me first proceed with security check may i have your id vlc one two three five may i have last four digits of associated bank one eight eight eight okay lets proceed with the transactions can i have the details i want to move my fifty percent of funds in samsung funds to apple fund and i want to invest twenty thousand pounds and eleven cents in nokia fund okay the fifty percent of share in samsung is worth eleven thousand twelve pounds fifty cents so let me complete declaration i confirm that fifty percent funds in samsung worth eleven thousand twelve pounds fifty cents will be moved into apple funds and the account number associated is one nine eight nine and invest twenty thousand pounds and eleven cents into nokia fund with account number associated two three nine eight okay fine the deal takes place at the next hour of bidding anything more required no thank you bye",{
'entities':[(697,702,'type'),(647,682,'amount'),(708,713,'saccountto'),(633,640,'saccountfrom'),(757,776,'account'),(833,838,'fund'),(788,810,'amount'),(875,895,'account'),(781,787,'type')]
}),

("you are speaking to moore from fil how can i help you im harry from hogwarts limited okay lets proceed with normal checking your full name and the last four digits of your bank my full name is harry potter but l have no bank account associated with fil okay can you give ur pincode one six six eight okay lets proceed with deal i want to sell hundred percent of share in godrej fund its worth twenty thousand pounds okay let me repeat it i confirm to  sell  my hundred percent of share in fund godrej okay its worth twenty thousand pounds with account number eight nine three four okay i think its fine place the deal okay it will be placed with next dealing hour",{
'entities':[(494,500,'fund'),(516,538,'amount'),(559,580,'account'),(452,456,'type')]
}),

("hey im jones im jim how can i help you i want to put in twenty six thousand dollars into american express fund ohk fine let me read back the deal for you i confirm to put in twenty six thousand dollars into fund american express with five three two nine as account number okay bye bye",{
'entities':[(212,228,'fund'),(174,201,'amount'),(234,253,'account'),(167,173,'type')]
}),


("hey this is bobby from fildelity tell me how can i help you im raj from denim limited i want to switch my sixty six percent of fund in parry fund to volkswagon fund my i confirm your details your full name please raj rathore okay the last four digits of your bank account one two three four no i guess this is not registered account okay yup three three nine eight okay its worth ninety three pounds so let me reconfirm the deal for you sixty six percent of fund in parry fund will be moved into volkswagon fund with account number associated three three three nine its worth ninety three pounds zero cents okay okay it would be placed anything else needed no ok bye bye",{
'entities':[(496,506,'saccountto'),(576,606,'amount'),(543,565,'account'),(485,490,'type'),(467,471,'saccountfrom')]
}),

("hey this is hermoine im gracy from fidelity how do you need me assist you i want to take out thirty five percent of my share from hindustan funds okay let me confirm your identity before placing the deal may i have your full name please im gracy george may i know the last line of address sydney australia one zero zero zero six nine the thirty five percent fund is fifty three thousand dollars okay let me confirm the deal for you i confirm that i want to take out thirty five percent from hindustan fund worth fifty three thousand dollars  with associated account one nine eight six okay any more assistance needed no fine okay bye bye",{
'entities':[(491,500,'fund'),(512,540,'amount'),(566,584,'account'),(457,465,'type')]
}),

("good morning you are speaking to kelly from fidelity how can i help you i need to place certain deals from hp limited and by the way im kate can i have you id please one three two eight okay tell me the last four digits of bank account nine nine one two is it correct yes okay now you can place your deals now i want to place two withdraw seventy five percent from golden fund and thirty percent from diamond fund i want it in the form of cheque okay but it would take time for processing cheque okay its fine with me okay fine let me confirm the deal for you i declare that i want to sell seventy five percent worth ten thousand pounds from golden fund with account one one two three and also sell thirty percent from diamond fund worth nineteen thousand pounds and account associated is three nine two one okay thank you do you need deal reference no okay okay fine",{
'entities':[(642,648,'fund'),(617,636,'amount'),(667,684,'account'),(585,589,'type'),(694,698,'type'),(738,762,'amount'),(789,807,'account'),(719,726,'fund')]
}),

("hello jon welcome to fidelity may i help you this is tom i want to move all my shares in dell fund to lenovo fund okay i confirm to move all my share in dell fund to lenovo fund worth eighteen thousand pounds and five nine two three is the number okay it would be proceed within next dealing hours",{
'entities':[(166,172,'saccountto'),(184,208,'amount'),(213,232,'account'),(132,136,'type'),(153,157,'saccountfrom')]
}),

("hey im molly from cousera limited okay you are speaking with kolly how can i assist you i need to place some deals on behalf of my clients okay let me complete some security questions can i help your full name molly potter can i have your account number one two nine eight of citicorp bank okay lets proceed with deals i want to place switch deal to be placed from chetan fund into ajanta fund i want to shift only thirty nine percent fund its worth eleven thousand pounds fourteen cents okay i want to buy share in whitepool fund worth sixteen thousand dollars and twelve cents okay and any more deals no fine let me confirm the deal i confirm the to place a switch deal from fund chetan to fund ajanta worth  eleven thousand pounds fourteen cents account associated is three nine eight zero and place a buy deal in whitepool fund worth sixteen thousand dollars with account number one nine zero zero okay its fine with me okay bye",{
'entities':[(682,688,'saccountto'),(711,748,'amount'),(771,792,'account'),(660,666,'type'),(697,703,'saccountfrom'),(817,826,'fund'),(838,862,'amount'),(883,901,'account'),(805,808,'type')]
}),
("hello im michael from fidelity how can i help you im richard i want to redeem sixteen percent of my fund in equity asia okay let me confirm identity first okay can i know your full name richard christopher may i have your address please my address is one nine three plot sydney australia code one nine nine three okay now this is done can i please  proceed with my deal yes its worth eleven thousand pounds nineteen cents sure let me confirm your deal i confirm to redeem sixteen percent of equity asia amounting to  eleven thousand pounds nineteen cents with account number one two nine nine okay nice lets proceed then it would be done by the next bidding time thank you any further assistance needed no thank you",{
'entities':[(491,502,'fund'),(517,554,'amount'),(575,592,'account'),(465,471,'type')]
}),
("hey i m david am i calling to fidelity yes richard this side how can i help you i want to switch my nineteen percent fund in equity development fund to fund multi asset okay fine let me reconfirm your order i declare to switch nineteen percent fund in equity development fund to fund multi asset worth eleven thousand dollars thirteen cents account associated is one two zero one okay thank you thank you fine do you need any deal reference no thank you ",{
'entities':[(284,295,'saccountto'),(302,340,'amount'),(363,379,'account'),(220,226,'type'),(252,270,'saccountfrom')]
}),
("welcome robert this side how can i help you im robert i want to move eleven percent of my funds from bata to paragon okay this would amount to thirthy nine thousand dollars perfect okay lets proceed then let me read the deal for i confirm to move my eleven percent in bata fund to paragon fund worth forty thousand pounds twelve cents and one two zero one is the account number ok fine okay any deal reference to be included no thank you thank you",{
'entities':[(281,288,'saccountto'),(300,334,'amount'),(339,355,'account'),(242,246,'type'),(268,272,'saccountfrom')]
}),
("you are speaking to susan how can i assist you im steven from intex corporation okay let me confirm you details may i have you full name steven robert may i have last four digits of registered bank yes surely one zero nine eight okay now we are done with it we can proceed with the dealing i want to sell ten percent of my tata fund and invest thirty five thousand pounds in greenwich fund okay the ten percent worth of tata fund is thirty thousand pounds okay let confirm  the deal you want to invest thirty five thousand pounds in greenwich fund with associated number one nine nine two and sell ten percent of my tata fund worth thirty thousand pounds with account number one two three four okay fine i confirm itokay do you want any other assistance no thank you thank you",{
'entities':[(533,542,'fund'),(502,529,'amount'),(571,588,'account'),(495,501,'type'),(616,620,'fund'),(632,654,'amount'),(675,693,'account'),(593,597,'type')]
}),
("hi  im mark from oyo corporation hello im thomas how can i help you i want to invest eighty nine thousand pounds in spacy fund let complete a quick set of questions due to security issues may i have your full name mark twain okay may i know your last four digits of bank account one one zero zero okay fine so let me reconfirm your deal i declare to invest eighty nine thousand pounds in spacy fund with nine two three nine as the account number okay i confirm do you need any further assistance no thank you",{
'entities':[(388,393,'fund'),(357,384,'amount'),(404,423,'account'),(350,356,'type')]
}),
("you are speaking with donals from fil corp how can i help you im isabella from swiss corp i want to make a few transactions for the day okay let me proceed with a quick check you full name please isabella edison good pincode of the address one nine nine three six okay now you can proceed with transaction i want to place a switch deal of thirty seven percent in fund equity to fund sparkle okay this would worth eleven thousand three hundred pounds fine its good and i want to sell my fifteen percent share in condour corp okay it would worth seventy thousand pounds okay fine so here are  the deal details i confirm to place a switch deal of thirty seven percent in fund equity to fund sparkle worth eleven thousand three hundred pounds with account number associated one  nine two three and a sell fifty percent share in fund condour corp worth seventy thousand pounds with number seven one one two okay i confirm to place okay any more assistance okay no thank you bye bye",{
'entities':[(688,695,'saccountto'),(702,738,'amount'),(770,789,'account'),(629,635,'type'),(673,699,'saccountfrom'),(829,841,'fund'),(848,871,'amount'),(884,901,'account'),(796,800,'type')]
}),
("hello im smith you are speaking to joe from fil i need to place a switch deal of twenty nine percent from biba fund to fund development its worth nine hundred thirty thousand pounds sounds fine for me let me confirm the deal i declare to place a switch deal of twenty nine percent worth nine hundred thirty thousand pounds with one nine three six as the account number from fund equity okay do u need any further assistance no thank you good bye good bye",{
'entities':[(379,385,'fund'),(287,322,'amount'),(328,346,'account'),(246,252,'type')]
}),
("hey im sonia from fil im antony i want to move my full share in lenovo fund to dell fund thats worth ten million dollars okay its fine with me then let me reconfirm the deal for i declare to move my full share in lenovo fund worth ten million dollars to  fund dell account number being one six nine zero confirm okay any thing else needed  no fine bye bye",{
'entities':[(260,264,'saccountto'),(231,250,'amount'),(286,303,'account'),(191,195,'type'),(213,219,'saccountfrom')]
}),

("jones at your service im dusky how can i help you i need to switch my nineteen percent from saviour fund to equity fund ohk this amounts ninteen thousand three pounds ohk sounds fine with me let me place the deal i confirm to switch my ninteen percent in saviour fund to equity fund worth ninteen thousand three pounds   the account number is one two three eight ohk sounds great ohk then let me proceed with the dealing the final bidding will be made in couple of hours ohk bye bye",{
'entities':[(271,277,'saccountto'),(289,318,'amount'),(343,362,'account'),(226,232,'type'),(255,262,'saccountfrom')]
}),

("john bayre at your service abraham this side do you wish to place any deals yes i want to place a switch deal type where i move ten percent of my share in philips fund to orpat fund ohk this is amounting to ten thousand nine dollars six cents okay its fine let me place a confirmation i declare to place a switch deal from fund philips to orpat fund worth ten thousand nine dollars six cents with account number associated one three five seven ohk ohk any more assistance needed no thank you bye bye",{
'entities':[(339,344,'saccountto'),(356,391,'amount'),(423,443,'account'),(306,312,'type'),(339,344,'saccountfrom')]
}),
("hey im molly from cousera limited okay you are speaking with kolly how can i assist you i need to place some deals on behalf of my clients okay let me complete some security questions can i help your full name molly potter can i have your account number one two nine eight of citicorp bank okay lets proceed with deals i want to place switch deal to be placed from chetan fund into ajanta fund i want to shift only thirty nine percent fund its worth eleven thousand pounds fourteen cents okay i want to buy share in whitepool fund worth sixteen thousand dollars and twelve cents okay and any more deals no fine let me confirm the deal i confirm the to place a switch deal from fund chetan to fund ajanta worth  eleven thousand pounds fourteen cents account associated is three nine eight zero and place a buy deal in whitepool fund worth sixteen thousand dollars with account number one nine zero zero okay its fine with me okay bye",{
'entities':[(682,688,'saccountto'),(711,748,'amount'),(771,792,'account'),(660,666,'type'),(697,703,'saccountfrom'),(817,826,'fund'),(838,862,'amount'),(883,901,'account'),(805,808,'type')]
}),

("hi i am barry from fil how can i help you i am jonty and i want to sell my funds all funds invested in fidelity technology ok sir your shares are worth seventy three thousand euros do you confirm that you want to sell them yes can you please tell your pets name as security question yes it is tommy ok so i am gonna read the deal for you i confirm that i want to sell all my funds of fidelity technology whose worth is seventy three thousand from my account number four six three two nine nine ok ok",{
    'entities':[(384,405,'fund'),(419,448,'amount'),(472,500,'account'),(363,367,'type')]
}),
("hi i am sergey from fil how can i help you i am ronaldo and i want to redeem my funds twenty percent  funds invested in fidelity ok sir your shares are worth twenty five million pound do you confirm that you want to redeem them yes can you please tell your mother name as security question yes it is kristen ok so i am gonna read the deal for you i confirm that i want to redeem  my funds of fidelity technology whose worth is seventy three thousand from my number eight four three six two eight ok ok",{
    'entities':[(392,411,'fund'),(427,449,'amount'),(465,495,'account'),(372,378,'type')]
}),
("hi i am roger from fil my colleque has told me that you want to switch your stocks yes i want to switch my fifty percent stocks from yahoo to microsoft ok sir you want to switch your fifty percent stocks from yahoo to microsoft which are worth sixty seven thousand pounds yes can you please tell me your pin code yes it is seven three four four three two ok sir now i am going to read the deal for you i confirm that i want to switch my fifty percent funds from yahoo to microsoft which are worth sixty seven thousand in my account number nine one four six three eight yes that is right ok sir have a nice day bye",{
    'entities':[(471,480,'saccountto'),(462,467,'saccountfrom'),(539,568,'amount'),(497,517,'account'),(427,433,'type')]
}),
("hi i am billy from fil how may i help you i am pele and i am calling to do a deal ok sir can you tell me the details of your deal i want to invest sixty three thousand bucks in fidelity finance funds ok sir you want to invest sixty three thousand pounds in fidelity finance funds is that right yes sir please tell last four digits of your card number it is three six four two ok sir now i am going to read the deal for you i want to buy  funds worth sixty three thousand pounds of fidelity finance funds in my account number three two seven six nine five yes that’s correct ok sir is there anything else i can help you with no thank you thank you for calling in fidelity sir bye",{
    'entities':[(495,511,'fund'),(464,491,'amount'),(539,568,'account'),(448,451,'type')]
}),
("hi i am christopher from fil my colleague has given me information that you want to buy funds worth thirty nine million pounds  in fidelity finance funds yes thats correct ok so what i am going to do is real the deal again i confirm that i want to buy funds worth thirty nine million pounds in fidelity select retailing funds in my account number three two seven six nine four yes thats right ok sir goodbye",{
    'entities':[(294,319,'fund'),(264,290,'amount'),(347,376,'account'),(248,251,'type')]
}),
("hi i am harry from fidelity international how can i help you i am ronny i want to sell thirty percent of my fidelity select banking fund okay it amounts to twenty two thousand pounds sounds good so may i confirm your details before you place the deal yes sure what is your full name ronny watsun what is your pincode one one zero zero what is the last four numbers of the card registered five nine two four of visa yes so i want to read the deal for you i confirm that i want to sell thirty percent of my fidelity select banking funds which is worth twenty two thousand pounds from my account one two three four five fix seven yes perfect",{
    'entities':[(503,534,'fund'),(550,576,'amount'),(593,626,'account'),(479,483,'type')]
}),
("hi i am pele how can i help you i am ronaldo and i want to switch my 50 percent of the total funds invested from fidelity select utilities to fidelity banks fund ok sir you want to switch your 50 percent of total stocks which are worth sixty eight thousand pounds from fidelity select utilities to fidelity banks fund oh yes ok sir so i am gonna read the agreement for you i confirm that i want to switch my 50 percent stocks which are worth sixty eight thousand pound from fidelity select utilities to fidelity bank funds in my account number three seven six eight two three yes that’s right ok bye ",{
    'entities':[(503,522,'saccountto'),(474,502,'saccountfrom'),(442,468,'amount'),(544,575,'account'),(401,407,'type')]
}),
("hi i am messi from fidelity international how can i help you i am maradona and i want to switch my thirty percent of funds from amazon to flipkart ok sir so you want to switch your thirty percent of funds which are worth seventeen million to flipkart yes that is right ok sir i am gonna read the deal agreement to you ok i confirm that i want to switch  my thirty percent of funds from  amazon to flipkart which are worth seventeen million pounds in my account number four six nine one seven three yes right thanks for that it is ok sir bye bye",{
    'entities':[(397,405,'saccountto'),(387,393,'saccountfrom'),(422,446,'amount'),(473,497,'account'),(346,352,'type')]
}),
("hi this is maria from fidelity i just got the information that you want to takeout your seventy percent of all stocks invested in our firm yes that is right can you please tell you card numbers last four digits as a security question ok it is three seven two nine ok sir your seventy percent of stocks of alphabet are worth eighty three thousand ok i am gonna read the deal for you i confirm that i want to sell seventy percent of my stocks of alphabet which are worth eighty three thousand pounds from my account number five three nine two one five yes ok sir bye bye",{
    'entities':[(444,452,'fund'),(469,497,'amount'),(521,549,'account'),(407,411,'type')]
}),
("hi this is jack from fidelity international how can i help you i want to invest one point two million dollars in walmart ok sir so you want to buy stocks worth one point two million in walmart yes ok sir so i am going to read the deal for you i confirm that i want to buy one point two million dollars in walmart from my account number three seven six four two two yes it is correct and thanks you are welcome sir is there any other way i can help you no thank you bye bye",{
    'entities':[(305,312,'fund'),(272,301,'amount'),(336,364,'account'),(268,271,'type')]
}),
("hi this is oggy from fidelity international and i just got information that you want to invest in mutual funds yes i want to invest in ibm what is the amount you wanna invest invest in sir i want to invest fifty one thousand pounds ok sir so you want to invest fifty one thousand pounds in ibm yes i am going to read the deal agreement for you ok i confirm that i want to invest fifty one thousand pounds in ibm in my account number three two seven two six four yes thats right ok sir bbye bye",{
    'entities':[(408,411,'fund'),(379,404,'amount'),(433,461,'account'),(372,378,'type')]
}),
("hi this is raman from fidelity international how can i help you i want to redeem my stocks invested in fmr how much percent of that stocks do you want to redeem sir i want to redeem all of it ok sir so you want to redeem hundred percent of your stocks invested in fmr whose current worth is eighty six thousand pounds yes can you please tell your pin code as a security question ye it is four three nine six five five ok sir i am going to read the deal now i confirm that i want to sell hundred percent of my fmr funds which are worth eighty six thousand pounds four three six nine two five yes thats right ok sir thank you for calling bye bye",{
    'entities':[(509,518,'fund'),(535,561,'amount'),(583,611,'account'),(482,486,'type')]
}),
("hi this is joe from fidelity international how can i help you i am looking to invest sixty thousand bucks in directi ok sir so you want to buy directi funds worth sixty thousand pounds yes ok so i am going to repeat the deal to you ok i confirm that i want to buy directi funds worth sixty thousand dollars in my account number six three four four two nine yes it is right thanks your welcome sir bye bye",{
    'entities':[(264,277,'fund'),(284,306,'amount'),(328,356,'account'),(260,263,'type')]
}),
("hii this a neymar from fidelity international how can i help you i am looking to put in seventy two thousand dollars in jupiter ok sir so you want to buy funds worth seventy two thousands in jupiter yes it is correct i am going to repeat the deal for you i confirm that i want to buy jupiter funds of seventy two thousand pound in my account number three one four six nine nine yes ok sir bye  bye",{
    'entities':[(284,291,'fund'),(301,327,'amount'),(349,377,'account'),(280,283,'type')]
}),
("hii this is gracy from fidelity international how can i help you i want to move my stocks from fidelity real estate to fidelity otc how much do you want to move sir all ok sir so you want to switch all of your stocks from fidelity real estate to fidelity otc which are worth sixty seven thousand pounds yes so i am going to read the deal for you i confirm that i want to switch 100 percent of my stocks from fidelity real estate to fidelity otc which are worth sixty seven thousand pounds in my account number two three six nine five four yes its correct thanks your welcome sir",{
    'entities':[(432,444,'saccountto'),(408,428,'saccountfrom'),(461,488,'amount'),(510,538,'account'),(371,377,'type')]
}),
("hii this is bill from fil how can i help you i want to switch my all my stocks from fidelity sai us to fidelity nordic ok sir so you want to switch all of your stocks from fidelity sai to fidelity nordic which are worth fifty three thousand pounds yes so i am going to read the deal for you i confirm that i want to switch 100 percent of my stocks from fidelity sai to fidelity nordic which are worth fifty three thousand pounds in my account number five nine three seven one four yes its correct thanks your welcome sir ",{
    'entities':[(369,384,'saccountto'),(353,365,'saccountfrom'),(401,428,'amount'),(450,480,'account'),(316,322,'type')]
}),
("hi this is elon musk from fidelity international and i just got information that you want to invest in mutual funds yes i want to invest in fidelity japan what is the amount you wanna invest invest in sir i want to invest seventy seven thousand pounds ok sir so you want to invest seventy seven thousand pounds in fidelity japan yes i am going to read the deal agreement for you ok i confirm that i want to invest seventy seven thousand pounds in fidelity japan in my account number three two seven two six four yes thats right ok sir bbye bye",{
    'entities':[(447,492,'fund'),(414,443,'amount'),(483,511,'account'),(407,413,'type')]
}),
("hi this is john from fidelity how can i help you i want to takeout my forty percent of all stocks invested in fidelity mega cap stock ok sir can you please tell you card numbers last four digits as a security question ok it is three two three two ok sir your forty percent of stocks worth eighty three thousand ok i am gonna read the deal for you i confirm that i want to sell forty percent of my stocks of fidelity mega cap which are worth ninety nine thousand euro from my account number two five  nine  one five two yes ok sir bye bye",{
    'entities':[(407,424,'fund'),(441,446,'amount'),(490,516,'account'),(372,376,'type')]
}),
("hi i am ronny from fil how may i help you i am johny and i am calling to do a deal ok sir can you tell me the details of your deal i want to put in six hundred thousand pounds in fidelity nasdaq composite index funds ok sir you want to invest six hundred thousand pounds in fidelity nasdaq composite index funds is that right yes ok sir for security concerns please tell last four digits of your card number it is  six nine four two ok sir now i am going to read the deal for you i confirm that i want to buy  funds worth six hundred thousand pounds of fidelity nasdaq composite index in my account number nine five two two two four yes that’s correct ok sir is there anything else i can help you with no thank you thank you for calling in fidelity sir bye",{
    'entities':[(552,583,'fund'),(521,548,'amount'),(605,631,'account'),(505,508,'type')]
}),
("hii this is cristine from fil how can i help you i am alan i want to switch my funds invested in fidelity series intrinsic opps to fidelity total bond fund how much of your funds do you wanna switch thirty seven percent so you want to switch your thirty seven percent funds from fidelity series intrinsic opps to fidelity total bond fund which are worth fifty three thousand pounds yes ok so i am going to read the deal for you i confirm that i want to switch my thirty seven percent funds from fidelity series intrinsic opps to fidelity total bond fund which are worth fifty three thousand pounds in my account number five seven nine one three five yes thats right",{
    'entities':[(529,553,'saccountto'),(495,525,'saccountfrom'),(570,597,'amount'),(619,649,'account'),(453,459,'type')]
}),
("hi i am annah from fidelity international how can i help you i am peter and i want to switch my twenty percent of funds from fidelity puritan to fidelity japan ok sir so you want to switch your twenty percent of funds which are worth seven million to fidelity japan yes that is right ok sir i am gonna read the deal agreement to you ok i confirm that i want to switch my twenty percent of funds from fidelity puritan to fidelity japan which are worth seven million euro in my account number one one two three five eight yes right thanks for that it is ok sir bye bye",{
    'entities':[(420,434,'saccountto'),(400,416,'saccountfrom'),(451,469,'amount'),(491,519,'account'),(361,367,'type')]
}),
("hii i am peter theil from fidelity how can i help you i am steve jobs and i want to invest thirty seven billion pounds in fidelity small cap funds ok sir so you want to buy funds worth thirty seven billion pounds of fidelity small cap so i am gonna read the agreement of your deal i confirm that i want to buy fidelity small cap funds worth thirty seven billion pounds in my account number seven nine nine five four three yes thats correct ok sir bbye",{
    'entities':[(310,334,'fund'),(341,368,'amount'),(390,421,'account'),(306,309,'type')]
}),
("hi this is tracy from fidelity international how can i help you i want to redeem my stocks invested in fidelity limited terms fund how much percent of that stocks do you want to redeem sir i want to redeem all of it ok sir so you want to redeem hundred percent of your stocks invested in fidelity limited terms fund whose current worth is eighty six thousand pounds yes can you please tell your pin code as a security question yes it is nine six three four two two ok sir i am going to read the deal now i confirm that i want to sell hundred percent of my fidelity limited terms funds which are worth eighty six thousand pounds in my account number two five five six five seven yes thats right ok sir thank you for calling bye bye",{
    'entities':[(556,584,'fund'),(601,627,'amount'),(649,677,'account'),(529,533,'type')]
}),
("hii this is eliza from fil how can i help you i am stacy i want to put in thirty three hundred thousand in fidelity series value discovery funds ok sir i will now repeat the deal for you i confirm that i want to buy funds worth thirty three hundred pounds in fidelity series value discovery funds in account no one six nine seven three four okay it is correct thanks for the deal you are welcome sir",{
    'entities':[(259,296,'fund'),(228,255,'amount'),(315,344,'account'),(212,215,'type')]
}),
("hii this is emma from fil how can i help you i am bella i want to switch my funds invested in fidelity value strategies to fidelity value discovery how much of your funds do you wanna switch ninety percent so you want to switch your ninety percent funds from fidelity value strategis to fidelity value discovery which are worth ninety two thousand pounds yes ok so i am going to read the deal for you i confirm that i want to switch my ninety percent funds from fidelity value strategies to fidelity value discovery which are worth ninety two thousand pounds three seven four two two one yes thats right",{
    'entities':[(491,515,'saccountto'),(462,487,'saccountfrom'),(532,558,'amount'),(580,608,'account'),(426,432,'type')]
})

]


@plac.annotations(
    model=("Model name. Defaults to blank 'en' model.", "option", "m", str),
    new_model_name=("New model name for model meta.", "option", "nm", str),
    output_dir=("Optional output directory", "option", "o", Path),
    n_iter=("Number of training iterations", "option", "n", int))
def main(model='/home/sangeetha/Desktop/spa/combine', new_model_name='fund', output_dir='', n_iter=0):
    """Set up the pipeline and entity recognizer, and train the new entity."""
    if model is not None:
        nlp = spacy.load('/home/sangeetha/Desktop/spa/combine')  # load existing spaCy model
        print("Loaded model '%s'" % model)
    else:
        nlp = spacy.blank('en')  # create blank Language class
        print("Created blank 'en' model")
    # Add entity recognizer to model if it's not in the pipeline
    # nlp.create_pipe works for built-ins that are registered with spaCy
    if 'ner' not in nlp.pipe_names:
        ner = nlp.create_pipe('ner')
        nlp.add_pipe(ner)
        f=1
    # otherwise, get it, so we can add labels to it
    else:
        ner = nlp.get_pipe('ner')

    ner.add_label(LABEL1)   # add new entity label to entity recognizer
    ner.add_label(LABEL2)
    ner.add_label(LABEL3)    
    ner.add_label(LABEL4)
    ner.add_label(LABEL5)
    ner.add_label(LABEL6)
    if model is None:
        optimizer = nlp.begin_training()
    else:
        # Note that 'begin_training' initializes the models, so it'll zero out
        # existing entity types.
        optimizer = nlp.entity.create_optimizer()



    # get names of other pipes to disable them during training
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
    with nlp.disable_pipes(*other_pipes):  # only train NER
        for itn in range(n_iter):
            random.shuffle(TRAIN_DATA)
            losses = {}
            for text, annotations in TRAIN_DATA:
                nlp.update([text], [annotations], sgd=optimizer, drop=0.35,
                           losses=losses)
            print(losses)
#    with open('test_data.txt', 'r') as myfile:
#    	data=myfile.read().replace('\n', '')
    # test the trained model
    data = 'hey im from fil how can i help you let me place a buy deal of ten thousand pounds eleven cents in fund demon okay let me reconfirm your deal okay i confirm to place a buy deal amounting ten thousand pounds eleven cents in fund demon with the associated account number one two three nine okay okay thank you'    

    doc = nlp(data)
    n=10
    print("entities in '%s'" % data)
    for ent in (doc.ents):    
    	print(ent.text, ent.label_)

    # save model to output directory
    if output_dir is not None:
        output_dir = Path(output_dir)
        if not output_dir.exists():
            output_dir.mkdir()
        nlp.meta['name'] = new_model_name  # rename model
        nlp.to_disk(output_dir)
        print("Saved model to", output_dir)

        # test the saved model
        print("Loading from", output_dir)
        nlp2 = spacy.load(output_dir)
        doc2 = nlp2(data)
        for ent in doc2.ents:
            print(ent.label_, ent.text)


if __name__ == '__main__':
    plac.call(main)
    
