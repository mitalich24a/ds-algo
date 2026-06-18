def backtrack_split(sequence, start_index, branch_container, master_container):
    # 1. Base Case: If we've successfully sliced to the end of the sequence
    if start_index == len(sequence):
        # Optional: Check if the full partition meets your specific goal
        if is_goal_achieved(branch_container):
            master_container.append(list(branch_container))
        return

    # 2. Iterate through all possible end positions for the current slice
    for end_index in range(start_index + 1, len(sequence) + 1):
        # Extract the current slice/segment
        current_slice = sequence[start_index:end_index]
        
        # 3. Validation check: Is this specific slice valid?
        if is_valid_slice(current_slice):
            
            # 4. Make the move (Take the slice)
            branch_container.append(current_slice)
            
            # 5. Recurse: Start the next slice exactly where this one ended
            backtrack_split(sequence, end_index, branch_container, master_container)
            
            # 6. Undo the move (Clean up / Backtrack)
            branch_container.pop()

# --- How to invoke ---
# master_container = []
# backtrack_split("abcdef", 0, [], master_container)
