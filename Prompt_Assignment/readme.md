when we give a prompt to a LLM its answer depends on what we type :
1st is zero shot prompting, here when we type "hello, translate it to French", the LLM will just give us the translated version of the word "hello", it does not give us unnecessary explanations or the history behind the word or that kind of information, its just gives us the translation.
the output we got was "Bonjour"

The second one in one shot prompting we give it a similar example, like asking it to translate Goodbye in French to which we will get response "Au revoir", one shot allows us to give it a similar task as the previous one

The third one is few-shot, in few-shot prompting we give it multiple similar tasks such as translating multiple phrases to french such as hello, thanks, goodbye to which we will get the response, "Bonjour","Merci","Au revoir" 

The fourth one is chain of thought prompting, in this we ask the LLM to think each step and ask it to return the step so we also get to know the process behind the solution
when we give the prompt “If I have 10 apples and give 3 apples to John, then buy 5 more apples, how many apples do I have? list step by step.”  we will the answer:
"Start with 10 apples.
Give 3 apples to John: 10 − 3 = 7 apples.
Buy 5 more apples: 7 + 5 = 12 apples.
Final answer: 12 apples."
as we can see we were given step by step about what the solution would be

The fifth type is Role prompting, in role prompting we ask the LLM to assume a role of particular person or any object and ask it to give a solution to our query, like "you are a senior doctor, explain fever in simple terms", in this we get answer to this from the POV of a senior doctor and how he would describe the fever
this prompting is usefull in generating more relevant and focused responses.


The sixth type is Structured-output prompting, in Structured-output prompting it makes the LLM's response consistent, organized, and easier to understand by clearly specifying the required format. It is especially useful when the output needs to follow a particular structure, such as JSON, tables, lists, or specific fields, making the information easier to read, analyze, and use in other applications.
for example "john is 25 years old, return this information in JSON " in which we will get the response 
{
  "name": "John",
  "age": 25
} 

in this type of prompting when we give it a task it will use tools to generate a answer, this usually takes more time then the regular tasks as the task is much complex then the regular one which we give such as translating
for example "what's today's date and how many days till diwali?" 
we will get the response as 
Today is **Sunday, August 23, 2026**. 

**Diwali 2026 is on Sunday, November 8, 2026.** ([Time and Date][1])

That means there are **77 days until Diwali!** 🎆

So:

*  Today: **23 August**
*  Diwali: **8 November**
*  **77 days to go**
*  That's about **11 weeks**.

to get all of this information LLM will have to use tools in order to generate the response as predicting the number of days remaining, finding when diwali will occur, calculating the number of weeks

