def backtrack_order_matters(choices, branch_container, master_container, visited):
    # 1. Base Case: Is the goal achieved?
    if is_goal_achieved(branch_container):
        master_container.append(list(branch_container))  # Copy the current branch
        return

    # 2. Iterate through all available choices
    for choice in choices:
        # 3. Validation check
        if choice not in visited: 
            
            # 4. Make the move (Take)
            branch_container.append(choice)
            visited.add(choice)
            
            # 5. Recurse
            backtrack_order_matters(choices, branch_container, master_container, visited)
            
            # 6. Undo the move (Clean up / Backtrack)
            branch_container.pop()
            visited.remove(choice)

# --- How to invoke ---
# master_container = []
# backtrack_order_matters(choices, [], master_container, set())
