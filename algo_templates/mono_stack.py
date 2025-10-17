def mono_stack(insert_entries):
  stack = []
  for entry in insert_entries:
    while stack and stack[-1] <= entry:
      stack.pop()
    stack.append(entry)
