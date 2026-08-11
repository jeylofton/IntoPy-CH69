"""
-------------------------------
 MINI CHALLENGE: THE GROCERY LIST
-------------------------------
You're building a grocery list app.
1. Create a list called "groceries" with at least 5 items.
2. Print the first and last item using indexing.
3. Use slicing to print just the first 3 items.
4. Add "eggs" to the end of the list using append().
5. Insert "milk" at the very beginning of the list.
6. Remove one item using remove().
7. Check if "bread" is in the list — print a message either way.
8. Sort the list alphabetically and print it.
9. Print how many items are in the final list.
"""

groceries = ["bread", "apples", "rice", "cheese", "bananas"]
print("Groceries:", groceries)

print("First item:", groceries[0])
print("Last item:", groceries[-1])

print("First 3 items:", groceries[:3])

groceries.append("eggs")
print("After append:", groceries)

groceries.insert(0, "milk")
print("After insert:", groceries)

groceries.remove("rice")
print("After remove:", groceries)

if "bread" in groceries:
   print("Yes, bread is on the list!")
else:
   print("No bread on the list.")

groceries.sort()
print("Sorted:", groceries)

print("Total items:", len(groceries))
