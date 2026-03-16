# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

- Enter does not submit numbers
- Enter field doesn't clear out after new game or submit guess
- Hint is not right
- Score is not initlaized to 0 (tbh what is the point of it?)
- History is offset by one time
- History not reset after new game
- Hint does not reset after new game

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).


I used Claude on this project.

I first asked AI to explain the codebase to me. Then I described the specific bugs I endcountered and asked the AI to figure out why do they behave that way and how to fix them.

One example that is correct is when fixing the hint bug. It correctly find where the bug and suggested correct fix to it. The return of the if statement was swapped. I review the diff to make sure the fix was correct.

Another example is when trying to fix the correct rendering of history. It coun't pinpoint the solution at one attampt. I had to gradually telling the AI how things are performing one change at a time to finally fix the problem.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?
I decided a bug is really fixed by testing out in the application and refactoring functions to pass test cases.

One test I run was for displaying the correct hint. I asked AI to develop pytest cases, and also went to play the game to make sure each time the hint is correct.

The AI helped me design test for fixing the hint bug by providing what test cases to use. It had some hiccups in writing the test as check_guess returns a tuple not a string. But it was able to correct itself after I provided the error message.


---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

The secret number kept changing because random.randint() was protectect and would run every time the script returns.

Every time there was an action to the website, the whole page refreshes, and session_sate is to rembemer what are the current values for each field.

The change that finaly gave the game a stable secret number is to make the random number gernation only execute when secret is not part of the session_state


---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

Constantly test feartures and have testcases for them. There are a lot of bugs I feel are twisted together and it is hard to test when fixing only one of the bugs. Github update after a feature is completed is also important.

One thing would do differently next time is giving the AI a bigger picture of what I encoutered and maybe ask for a plan on where to start first.

I thought AI generated code would be more be comprehsive, but in reality, each time I ask for a change, it only fix part of the problem.