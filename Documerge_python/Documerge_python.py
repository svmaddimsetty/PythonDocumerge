import os 
import re

def process_files(file1, file2, output_file_prefix):
    # Read content of File1
    with open(file1, 'r') as f1:
        lines1 = f1.readlines()

    # Read content of File2 (names list)
    with open(file2, 'r') as f2:
        forms_list = f2.readlines()

    batch_counter = 0  # To count which output file to write to
    
    start_batch = lines1[:6]
    mid_batch = lines1[6:22]
    last_step = lines1[26:]

    forms_counter = 0 
    each_form = 0

    while each_form < len(forms_list):

        step_lines = []

        len_forms = len(forms_list)


        for each_step in range(20):
            
            step_value = f"STEP{(each_step+1)*10:03d}"
            mid_batch[0] = re.sub(r"STEP\w{3}", step_value, mid_batch[0])
            
            step_lines += mid_batch

            if each_form >= len_forms:
                break

            for _ in range(5):
                
                if each_form >= len_forms:
                    break

                step_lines.append(lines1[22])

                if "<form_number>" in lines1[23]:
                    modified_line = lines1[23].replace("<form_number>", forms_list[each_form].strip())
                    step_lines.append(modified_line)
                    step_lines.append(lines1[24])
                if "<form_number>" in lines1[25]:
                    modified_line = lines1[25].replace("<form_number>", forms_list[each_form].strip())
                    step_lines.append(modified_line)

                each_form += 1
        
            file_out_lines = start_batch + step_lines + last_step

        print('at end' + str(each_form))

        batch_counter += 1
        output_file = open(f"{output_file_prefix}_{batch_counter}.txt", 'a')

        for each_line in file_out_lines:
            output_file.write(each_line) 

    # Close the final output file
        output_file.close()




# This block ensures the function is called when the script is executed directly
if __name__ == "__main__":
    # Set file paths (adjust these to your actual file paths)
    file1_path = r'C:\Users\maddswa\source\repos\PythonDocumerge\Documerge_python\constant_JCL.txt'
    file2_path = r'C:\Users\maddswa\source\repos\PythonDocumerge\Documerge_python\form_numbers.txt'   
    output_path = r'C:\Users\maddswa\source\repos\PythonDocumerge\Documerge_python\JCL'       

    # Call the function to process the files
    process_files(file1_path, file2_path, output_path)
