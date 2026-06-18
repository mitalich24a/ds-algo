def backtrack_order_doesnt_matter(choices, start_index, branch_container, master_container):
    # 1. Base Case: Is the goal achieved?
    # (Note: For subsets, you might append to master_container at every step)
    if is_goal_achieved(branch_container):
        master_container.append(list(branch_container))
        return

    # 2. Iterate through choices *starting from the current index*
    for i in range(start_index, len(choices)):
        choice = choices[i]
        
        # 3. Validation check (if any specific constraints apply)
        if is_valid(choice):
            
            # 4. Make the move (Take)
            branch_container.append(choice)
            
            # 5. Recurse (i + 1 ensures we don't reuse the same element)
            backtrack_order_doesnt_matter(choices, i + 1, branch_container, master_container)
            
            # 6. Undo the move (Clean up / Backtrack)
            branch_container.pop()

# --- How to invoke ---
# master_container = []
# backtrack_order_doesnt_matter(choices, 0, [], master_container)
