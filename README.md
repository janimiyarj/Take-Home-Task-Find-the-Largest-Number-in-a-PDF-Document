# Take-Home-Task-Find-the-Largest-Number-in-a-PDF-Document
Timeline: 1-2 Days

Task Overview:
Build a simple solution that scans the provided PDF document and identifies the single largest numerical value it contains. This mimics a real-world scenario of parsing unstructured or semi-structured documents to extract meaningful data.
Source Material:
PDF: Cadre AI - AI Engineer TakeHome Task 3: Parse PDF (Source Material).pdf


Goal:
Primary Goal: Locate the greatest numeric value in the document. The specific unit (dollars, years, pounds, etc.) is irrelevant - just find the largest number.


Bonus Challenge: Account for natural language context. For example, if the document mentions that values are listed in millions, then 3.15 should be interpreted as 3,150,000 instead of 3.15.

(continued on next page)
What You’ll Be Building:
Document Parsing Logic:


Parse the PDF (or a local copy of the PDF) and read its contents.
Identify all numerical values present in the text.
If applicable, adjust values based on textual indicators (e.g., “millions,” etc.).


Result Extraction:


Compare all discovered numeric values.
Determine which one is the largest overall.
Output that value in a clear, readable format.


Implementation:


You are free to use any programming language or open-source libraries.
Your solution can call any external APIs, but do so at a minimal/negligible cost.



What We’re Looking For:
Correctness & Functionality: The solution should accurately parse the PDF and find the largest value.


Clean, Maintainable Code: Show clear organization, sensible abstractions, and readability.


Handling of Natural Language Context (Bonus): Where the document references values in millions (or similar qualifiers), handle those cases correctly.


Reasonable Performance: Should complete in well under a minute for a typical PDF such as the one provided.


No External Service Calls: The solution must be self-contained, referencing local files or libraries only.




What You Can Use:
Languages & Frameworks: Any language is acceptable. Python is suggested if you don’t have a preference.


Libraries: Open-source packages (e.g., PDF parsing libraries in Python).


Resources: ChatGPT, Gemini, Claude, etc. are allowed during development.



Submission:
Public Repo (Preferred): Host your solution in a public GitHub repository (or similar). Provide a short README that describes:
How to install dependencies
How to run the code
Notify Cadre AI: Email the link to the person who provided you with this task.
A 5-minute Loom or video walk-through is required.



Report:
In your README or accompanying documentation, please include:
Further Improvements: If you had more time, what would you add or optimize?
Highlights: Which parts of your solution are you most proud of?
Complexities: Which parts were the most challenging or time-consuming?
Feedback: How was the experience? Do you have any suggestions for improving this task?



Have fun and best of luck!
You may be asked to walk through your code in a subsequent interview, and you should be prepared to explain your approach and design decisions.
