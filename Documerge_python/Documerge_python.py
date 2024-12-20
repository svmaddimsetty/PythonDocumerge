import os




def generate_output_files(input_file_1, input_file_2, output_file_prefix, batch_size=10):
    # Step 1: Read Input File 1 and extract lines 5 to 10

    print("Current working directory:", os.getcwd())

    with open(input_file_1, 'r') as file:
        lines = file.readlines()
    
    # Extract lines 5 to 10 (index 4 to 9 in Python)
    lines_to_repeat = lines[4:10]
    
    # Step 2: Read Input File 2 (list of form names)
    with open(input_file_2, 'r') as file:
        form_names = file.readlines()
    
    # Clean up form names (strip extra spaces or newlines)
    form_names = [form.strip() for form in form_names]
    
    # Step 3: Generate the output content in chunks
    total_forms = len(form_names)
    num_batches = (total_forms // batch_size) + (1 if total_forms % batch_size != 0 else 0)
    
    for batch_num in range(num_batches):
        # Output file name based on the batch number
        output_file = f"{output_file_prefix}_{batch_num + 1}.txt"
        
        # Write to the batch output file
        with open(output_file, 'w') as output:
            start_index = batch_num * batch_size
            end_index = start_index + batch_size
            batch_form_names = form_names[start_index:end_index]
            
            for index, form_name in enumerate(batch_form_names, start=start_index + 1):
                # Modify line 5 to reflect the step number
                step_label = f"STEP{index:03d}"  # Format STEP001, STEP002, etc.
                
                # Copy the lines to repeat and replace line 5 and line 6
                modified_lines = lines_to_repeat[:]
                modified_lines[0] = step_label  # Replace line 5 (index 0)
                modified_lines[1] = form_name   # Replace line 6 (index 1)
                
                # Write the modified lines to the output file
                output.writelines(modified_lines)
                output.write("\n")  # Add a blank line between sections

# Example usage:

generate_output_files('input_file_1.txt', 'input_file_2.txt', 'output_file', batch_size=10)

