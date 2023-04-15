from pympler import asizeof

def find_a_match(file: str, word: str)-> GeneratorExit:
    with open(file, "r", encoding= "utf-8") as file_1:
        while True:
            line = file_1.readline()
            if not line:
                break
            if word.lower() in line:
                yield line

def write_down(match_data: list)-> None:
    with open("results.txt", "w", encoding="utf-8") as file:
        file.writelines(match_data)

def main():
    file_name = "rockyou.txt"
    input_user = input("enter a search term ") 
    data = find_a_match(file_name, input_user)
    result = list(data)
    write_down(result)
    print (f" in the file {len(result)} lines, syze {asizeof.asizeof('results.txt')} bytes")
    

if __name__=="__main__":
    main()