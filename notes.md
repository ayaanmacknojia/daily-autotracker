GOAL: add weekly summary feature

Looks like:
- prints avg sleep
- prints gym days this week
- prints avg hours worked
- prints list of moods (maybe)

Steps:
- ask user to enter "view" as input to trigger summary
- create weekly summary function:
    - use for key in dictionary loop
    - loop over relevant variables and add them to a sum
    - calc avg (sum / counter)
    - edge case: some values might not exist, not even as 'None' so crash proof function for this (check if it exists?)
    - weekly summary works at any point in the week