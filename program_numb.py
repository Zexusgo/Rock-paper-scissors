from random import choice

def random_numb():
    
    scp_list = ["Rock","Scissors","Paper"]
    prog_output = choice(scp_list)
    return prog_output

if __name__ == "__main__":
    print(f"Computer choice: {random_numb}")