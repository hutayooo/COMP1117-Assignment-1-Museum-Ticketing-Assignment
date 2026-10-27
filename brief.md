# A1 Museum Ticketing Assignment

## Overview

A group of visitors arrives at a museum and needs to buy tickets. Write a program that reads the visit day and the visitors’ ages, works out the cheapest correct total, which means forming a group whenever a group of 5 adults is possible, and prints a short summary.

**This assignment is done with the course AI assistant, in a specific order.**
First, reason through the problem yourself with your AI assistant, and
record the outcome in `Specifications.md`. You supply the reasoning and
fill in the worksheet in your own words. Then implement the program:
either ask the AI to write
it against your specification, or write it yourself. Finally, test it: run
the supplied checks `test.py` and your own test cases against values you
predicted by hand. You must understand and be able to explain every part.

You submit four things: the program, your test cases, `Specifications.md`
and your full chat transcript `History.md`. See How this is graded below.

## Description

### Day

The first input is an integer from 1 to 8. Days 1 to 5 mean a weekday, days 6 and 7 mean a weekend, and day 8 means a holiday.

### Ages

After the day, the program reads visitor ages, one per line. Each age is a valid integer between 0 and 80. Input ends when the user enters -1. The -1 is not a visitor and is not counted.

### Ticket prices

Each visitor is a child, a senior, or an adult. A child is age 12 or under, a senior is age 60 or over, and an adult is age 13 to 59. The individual price depends on category and day type. There is also a flat group price for the day:

|         | Child | Adult | Senior | Group price |
|---------|------:|------:|-------:|------------:|
| Weekday | 30    | 60    | 40     | 35          |
| Weekend | 40    | 80    | 50     | 65          |
| Holiday | 50    | 100   | 60     | 75          |

### Group tickets

Only adults can be placed into groups of exactly 5. Everyone in a group pays the flat group price instead of their individual price. The museum forms as many complete groups of 5 adults as possible; any adult left over who does not fill a whole group pays their individual price, and children and seniors always pay their individual price. A person is never charged both a group price and an individual price.

### Discount

On a weekend or holiday, if at least one complete group was formed, apply a 10% discount to the total ticket cost. The discount does not apply on weekdays, nor if no complete group was formed.

### Service fee

A service fee of 5 per person is added, but capped at 30. The fee is 0 if it is a weekday and there are fewer than 3 visitors.

## Input and output format

Your program is tested automatically, so it must follow this format exactly.

Read the day with the prompt `Enter day (1-8): ` and each age with the prompt `Enter age (-1 to stop): `. Input is one value per line: the day, then one age per line, then `-1`.

After input ends, print **exactly these nine lines and nothing else**.
Labels, capitalisation, and punctuation must match exactly. The three money
values Discount, Service fee and Total cost must always show two decimal
places; the other values are plain integers. Output is compared exactly, so
mind the spaces, the capitalisation, and the two decimals.

```
Day type: <weekday|weekend|holiday>
Children: <int>
Adults: <int>
Seniors: <int>
Total people: <int>
Groups formed: <int>
Discount: <0.00>
Service fee: <0.00>
Total cost: <0.00>
```

## Constraints

Use only what we have covered in class: the basic types int, float, str and bool; `input()` and `print()`; conditionals if, elif and else; loops; and operators. Do not use anything outside this: no lists, no dictionaries, no functions of your own, and no try and except statements. Even when working with an AI, keep the program within these tools; if the AI produces code using something we have not covered, ask it to rewrite the program using only the features above. You should be able to read and explain every line yourself.

## Worked examples

Each example is a full console session: the value after each prompt is what the user types.

### Example 1

```
Enter day (1-8): 1
Enter age (-1 to stop): 5
Enter age (-1 to stop): 30
Enter age (-1 to stop): -1
Day type: weekday
Children: 1
Adults: 1
Seniors: 0
Total people: 2
Groups formed: 0
Discount: 0.00
Service fee: 0.00
Total cost: 90.00
```

No group forms, and the fee is waived because it is a weekday with fewer than 3 people.

### Example 2

```
Enter day (1-8): 1
Enter age (-1 to stop): 30
Enter age (-1 to stop): 30
Enter age (-1 to stop): 30
Enter age (-1 to stop): 30
Enter age (-1 to stop): 30
Enter age (-1 to stop): 30
Enter age (-1 to stop): 65
Enter age (-1 to stop): 65
Enter age (-1 to stop): 8
Enter age (-1 to stop): 8
Enter age (-1 to stop): -1
Day type: weekday
Children: 2
Adults: 6
Seniors: 2
Total people: 10
Groups formed: 1
Discount: 0.00
Service fee: 30.00
Total cost: 405.00
```

One group of 5 adults forms; there is no weekday discount, and the fee of 5 × 10 = 50 is capped at 30.

### Example 3

```
Enter day (1-8): 6
Enter age (-1 to stop): 30
Enter age (-1 to stop): 30
Enter age (-1 to stop): 30
Enter age (-1 to stop): 30
Enter age (-1 to stop): 30
Enter age (-1 to stop): 30
Enter age (-1 to stop): 65
Enter age (-1 to stop): 65
Enter age (-1 to stop): 8
Enter age (-1 to stop): 8
Enter age (-1 to stop): -1
Day type: weekend
Children: 2
Adults: 6
Seniors: 2
Total people: 10
Groups formed: 1
Discount: 58.50
Service fee: 30.00
Total cost: 556.50
```

## Tips

### Printing the money values


The three money values must always print with exactly two decimal places, for example 90.00, 30.00 and 556.50. Watch out for two things:

- If no discount applies, a total may still be a whole number of type int, which would print as 90 with no decimals.
- If the 10% discount applies, multiplying by 0.9 gives a float that can print with many decimals, such as 526.5000000001.

To handle both, format the value to two decimal places when you print it. For example, if `x` is the value:

```python
print("Total cost:", "{:.2f}".format(x))
```

"{:.2f}" always shows exactly two decimals whether x was a whole number or a long decimal, so it fixes both cases at once. Use the same approach for the discount and the service fee.

## Testing your program


**The target: every decision in the program gets tested at least once, in each direction.** The program makes a handful of decisions: the day type; which price category each age falls into; whether a complete group forms; whether the discount applies; whether the fee is waived, normal, or capped. Your test set does its job when, for every one of these decisions, at least one case makes it go one way and at least one makes it go the other. Design at most ten cases toward that target. A case that changes no decision is a wasted one.

Predict before you run. For each case, work out the expected output first by reasoning about the rules, then run your program and confirm it matches. A test only proves something if you predicted the result. Running and copying whatever the program prints does not catch bugs.

You may assume all input is valid: day 1 to 8 and ages 0 to 80. You do not need to test invalid input.

### Submission format for tests

Put all your test cases in a single plain-text file, `tests.txt`. For each case, give the input, one value per line, followed by the expected output. Separate cases with a blank line. For example:

```
1
5
30
-1
Day type: weekday
Children: 1
Adults: 1
Seniors: 0
Total people: 2
Groups formed: 0
Discount: 0.00
Service fee: 0.00
Total cost: 90.00

6
30
30
30
30
30
-1
Day type: weekend
Children: 0
Adults: 5
Seniors: 0
Total people: 5
Groups formed: 1
Discount: 32.50
Service fee: 25.00
Total cost: 317.50
```

## The AI chat history


The AI-usage marks are read from `Specifications.md` and `History.md`
together: the worksheet is your distilled reasoning, and the chat shows
that it came before the code, in your own words.

Before any code is written, by the AI or by you, your chat should show your own thinking, worked out by you, not asked of the AI. In particular it should cover how you read the rules off the specification, such as the age cutoffs, the group of 5 rule, the discount, the fee cap and waiver, and the order these apply; what type you expect each value to be; and how you would structure the decision logic and the order of the steps, sketched in your own words as a numbered list of steps rather than Python.


**Avoid these weak chat history patterns:**


- Delegating the thinking: “Write me a Python program for museum ticket pricing.” The AI does everything and your history shows none of your own reasoning. Low marks even if the code is perfect.
- Pasting instead of specifying: copying the specification or the price table straight into the AI. You haven’t worked the rules out yourself; the plan has to be in your own words, with the boundaries you derived.
- Retrofitting the plan: asking for the code first, then writing “here’s how I would have structured it.” Your reasoning must come before the AI generates code. A plan written after you’ve seen the answer is a paraphrase, and it doesn’t count.
- Padding for length: a long string of “try again”, “make it better”, “are you sure” with no real reasoning. Length earns nothing.


**What a strong chat history looks like:** you reason out the rules, boundaries, and the order of the steps yourself first; you state what types you expect; then the program gets written, either by the AI against your specification or by you.


**What we are not grading:** you are not marked on whether your initial thinking turned out correct. If you expected the wrong type, or sketched a logic structure the AI improved on, that costs you nothing. Being wrong and then noticing it is the exercise. A mistake the AI points out and you correct in the chat is Full level reasoning, not a defect. Your reasoning grade does not double-count code errors: the code output component covers whether the program works; the reasoning component covers how you worked with the AI to design the program. An honest “I expected X, but the AI did Y, and here’s why Y is better” scores full marks. You are also not marked on length: a short, precise exchange beats a long one, and padding will not help. What we look for is simply that the thinking was genuinely yours and came before the code.


## Why we do it this way

Read this. It is the point of the whole assignment. In real projects this is genuinely how you work with an AI: you give it a clear design and specification before it writes code, because a vague request produces vague or wrong results, and because you, not the tool, are responsible for the decisions. In practice that specification is usually looser; an experienced developer relies on shared context. We go into this much detail deliberately, because this is a small, self-contained project and the point is to build the habit of thinking a problem through before handing it off. Once the habit is yours, you’ll do it faster and more loosely on real work. For now, spell it out.


## How this is graded

| Component       | Share | Marked by                              |
|-----------------|------:|----------------------------------------|
| Code output     | 35%   | Automatic, against the test data       |
| Your test cases | 35%   | A teaching assistant, against a rubric |
| How you used the AI | 30% | A teaching assistant, against a rubric |

The rubrics below describe each band; the mark for a band is fixed and shared with TAs. 

**Test cases, 35%:**

| Level | What it looks like |
|---|---|
| Full | Cases together cover **all** of the different situations the program must handle, and all expected outputs are correct. |
| Substantial | Most situations are covered, with only a few gaps, and all expected outputs are correct. |
| Partial | Several situations are not covered, **or** one or more expected outputs are incorrect. |
| Weak / none | Very few cases and no meaningful coverage; no test file counts here. |

**How you used the AI, 30%:**

| Level | What it looks like |
|---|---|
| Full | Your own reasoning about what the program has to do appears before any code is written, by you or by the AI, in your own words. It is translated toward code rather than restated from the brief: what to check, in what order, and how the pieces fit together. Wrong first attempts are fine when the chat shows the AI pointing them out and you discussing and correcting them. |
| Substantial | Reasoning is in your own words and clearly came before the code, but stays close to rephrasing the brief. What the program needs to handle is stated correctly, without much sign of how it will turn into code. |
| Partial | Very little real reasoning: most of the specification is pasted back, key cases or boundaries are not worked out, or the shape of the code is missing or borrowed from the AI. |
| Weak / none | No own reasoning at all: the specification pasted into the AI, the plan written after the code already existed, pure delegation, or padding. |


## Academic integrity

This assignment is designed to be done with an AI tool, so the rules are a little different from a normal "write it yourself" task. Using AI to help you reason, generate code, and debug is not only allowed, it is the point. What still matters is that the work you submit is genuinely yours.


**Allowed and encouraged:** discussing the problem with an AI tool, asking it to explain concepts, and having it generate and fix code once you have reasoned through the design; asking the AI to check your thinking or point out mistakes.


**Not allowed:**

- Using the course API key for anything other than this assignment, or sharing the key with anyone outside the course.

- Sharing or copying chat histories, code, or test files with or from another student. Your reasoning and your conversation must be your own. Two submissions with the same chat history or the same test cases will both be treated as a violation.


- Submitting a chat history that is not really yours, for example one produced by someone else, or edited afterwards to look like reasoning that did not actually happen. The chat history must be a truthful record of how you worked.
