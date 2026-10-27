# A1 Museum Ticketing: My Specifications

**Finish this file first, before any code is written.** You supply the
reasoning and fill in this worksheet in your own words. The AI can then
write the code against it.

## Input and output types

What the program reads and what it prints, with the type of each value:
int, float, str, bool. Say why.

- **Inputs:** what values does the program read, and what type is each?
1. Day: Should be an integer, as it takes values from 1 through 8 as a whole number which represents the day types
2. Age: Also an integer, as it takes values from 1-80 as a whole number. The program will keep looping age input until -1 is entered, which will break the loop. Notice how -1 is also an integer, hence the data type int will work for all possible values (1-80 and -1)

- **Outputs:** 
1. Day type: str, or string. The day type will explicitly output either "weekend", "weekday", or "holiday". Hence a string is used here to represent words
2. Children, adults, and seniors are all integers as it counts the number of visitors in each category
3. Total people: int too, as it counts the total visitor count
4. Groups formed: Also integer, as the number of groups cannot be represented by a decimal or fraction. It can only be represented by a whole number

Notice how in specifications.md and the test cases, Discount, Service Fee, and Total cost are printed with 2 decimal places. As such, the float data type is used here, as the int data type cannot represent decimal numbers

## The rules in my own words

State what the program must do, in your own words, not the assignment's
wording pasted back. Work through each part below:

- **Logic:** what the program must do, rule by rule.
1. Day mapping: Grab the input (1-8) and store in variable 'day'. If the input is 1 through 5 inclusive, it maps to a weekday. A 6 or a 7 maps to a weekend, and an 8 maps to a holiday
2. Pricing: Each visitor is categorized by their age, then re-categorized as a senior, child, or adult. We can then use this data, combined with that day type it is, to compute their price ticket
  - Weekday: Child = 30, Adult = 60, Senior = 40.
  - Weekend: Child = 40, Adult = 80, Senior = 50.
  - Holiday: Child = 50, Adult = 100, Senior = 60.
3. Groups
  - Every full block of 5 adults form a group, where they pay the group rate instead. We can find the number of groups by doing integer division (//) of the total number of adults by 5, then multiply them by the group rate at that time (35 on weekday, 65 on weekend, 75 on holiday) to compute their cost (groups * 5 * price)
  - The remaining adults need to pay their individual prices. We can take the remainder (% or modulo) of the total number of adults by 5, then multiply them by the individual rate at that time to compute their cost
  - The remaining number of people that pays the individual price must be less than 5. Because otherwise, they can form another group
4. Discounts
  - A 10% discount is applied to the overall total if the following conditions meet:
    - The day type is a weekend OR holiday
    - AND there are at least 1 group formed
    - if (day_type == "weekend" OR day_type == "holiday") AND groups_formed > 0
    - else, no discount
  5. Service Fee
    - A service fee is generally applied, that being $5 per visitor, but capped at 30. Meaning that if there are 6 or more visitors, the service fee will always be 30
    - However, if the day type is a weekday and there are less than 3 visitors, the service fee is waived
  6. Total cost: Ticket cost - discount + service fee

- **Boundaries:**
1. Age boundaries
  - Age 12 is a Child (30/40/50), age 13 shifts to an Adult (60/80/100).
  - Age 59 is an Adult (60/80/100), age 60 shifts to a Senior (40/50/60).
  - Anything above 60 is a senior
2. Day boundaries: Days 1 to 5 are weekdays, day 6 shifts to weekend, day 8 shifts to holiday
3. Group boundaries:
  - 4 adults: 0 groups (all 4 pay the individual price)
  - 5 adults: 1 group (all 5 pay the group rate)
  - 6 adults: 1 group (5 pays the group rate, 1 pays individual)
  - 9 adults: 1 group (5 pays the group rate, 4 pays the individual)
  - 20 adults: 4 groups (all 20 pays the group rate)
  - The number of groups increase strictly every multiple of 5
4. Service Fee:
  - Weekday with 2 visitors: 0.00 fee
  - Weekday with >2 visitors: min(visitor_count * 5, 30). For the purposes of the program, the min() function will not be used, and standard if statements will be used instead
  - In other words,
    - 5 visitors = 25.00
    - 6 or more visitors = 30.00 (capped)

- **Order:** the steps as a numbered list in plain sentences, not Python:
  what must happen first, and what can only be done after input ends?
1. Prompt for and read the 'day' integer (1-8) and determine the 'day_type' string using IF statements
2. Using a while loop, repeatedly prompt for visitor's ages until a '-1' is entered
3. For each valid read, classify the visitor as a child, adult, or senior. Then increment their respective counters and the total count
4. After input stops (-1), calculate the number of groups (Adults//5), and the remaining number of adults not in a group (Adults%5)
5. Compute the ticket subtotal by summing the costs for children, seniors, grouped adults, and un-grouped adults
6. Determine if the 10% discount conditions are met (weekend/holiday AND at least 1 group). If so, calculate the discount amount
7. Compute the service fee based on total people, capping it at 30, or waiving it if it is a weekday with fewer than 3 people
8. Calculate the final total cost, given by ticket_cost - discount + service_fee.
9. Print the 9 required lines