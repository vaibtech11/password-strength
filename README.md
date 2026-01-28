Password Strength - Regex Tester

It determines a password's strength based on its minimum length, the presence of a number, and the use of special characters.

TO execute the code run "python main.py"

Why did I choose this approach?

I selected this strategy because it is straightforward and simple enough for a novice to comprehend.
Rather than writing intricate logic, I checked particular patterns, such as numbers and special characters, using Python's regular expressions.

To ensure that the code is still readable and clear, each password validation rule was examined individually.

What was the hardest bug you faced, and how did you fix it?

My special character check wasn't functioning properly at first.
By understanding how re.search() functions and modifying the regular expression pattern to appropriately match special characters within the password, I was able to resolve this issue.

Screenshot of final output showing which passwords failed and which passed


![Program Output](screenshots\output_screenshot.png)
