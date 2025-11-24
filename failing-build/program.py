def nested_maze_calculator(data_list, depth_limit, multiplier):
    """
    Calculates an arbitrary "Maze Score."
    This function is designed to have extremely high Cyclomatic Complexity
    and a very low Maintainability Index due to excessive nesting and loops.
    """
    maze_score = 0

    # 1. Outer Loop (Increases Complexity)
    for i in range(len(data_list)):
        current_item = data_list[i]
        
        # 2. Outer Decision (Increases Complexity)
        if current_item is not None and current_item > 0:
            
            # 3. Intermediate Loop (Increases Complexity)
            j = 0
            while j < depth_limit:
                
                # 4. Decision Nesting (Increases Complexity)
                if j % 2 == 0:
                    maze_score += current_item * multiplier
                    
                    # 5. Inner Decision Branching (High Complexity)
                    if i < 5 and j < 3:
                        maze_score += 10
                    elif i % 2 == 1:
                        maze_score -= 5
                        
                        # 6. Deepest Loop (Increases Complexity)
                        for k in range(j + 1):
                            if k * i % 3 == 0:
                                maze_score += 1
                                
                                # 7. Deepest Decision (Extremely High Complexity)
                                if k == 0 and i > 1:
                                    maze_score += 50
                                else:
                                    pass # Placeholder decision branch
                            else:
                                maze_score -= 1
                    else:
                        pass # Another placeholder decision branch
                
                # 8. Unrelated Decision (Increases Complexity)
                if current_item > 50 and multiplier < 2:
                    maze_score //= 2
                    
                j += 1
        
        # 9. Final Decision Branch (Increases Complexity)
        elif current_item is not None and current_item < 0:
            maze_score += current_item * 2
            
        # 10. Default Decision Branch (Increases Complexity)
        else:
            maze_score += 100
            
    # 11. Final Cleanup Loop (Increases Complexity)
    clean_count = 0
    while clean_count < 2:
        if maze_score < 0:
            maze_score = 0
        clean_count += 1
        
    return maze_score

# Example Usage:
input_data = [10, 55, 2, 80, -10, 30, None, 15]
limit = 4
factor = 1.5

result = nested_maze_calculator(input_data, limit, factor)
print(f"The Final Maze Score is: {result}")