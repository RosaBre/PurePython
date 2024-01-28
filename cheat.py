def cheat(cheat_string):
    """print the model answer for selected questions from week 1 and 2"""
    if cheat_string == "Q1.2P.9":
        print("""# Q1.2P.9 ----------------------------------------------------------------------
        np.random.seed(1234)  # Set the random seed
        speed_sec = np.zeros(10)
        sim_speed = np.random.uniform(size=5)  # Speed simulation in seconds
        speed_sec[0:5] = sim_speed * np.random.uniform(low=0.5, high=10, size=5)
        speed_sec[5:10] = sim_speed

        language = np.repeat(np.array(['R', 'Python']), 5)

        code_type = np.char.add(np.array(['forloop'] * 5), np.arange(1,6).astype(str))
        code_type = np.tile(code_type, 2)

        all_data = {"language" : language,
                   "code_type" : code_type,
                   "speed" : speed_sec}
        my_data = pd.DataFrame(all_data)
        print(my_data)""")
    elif cheat_string == "Q1.2P.4":
        print("""# Q1.2P.4 ----------------------------------------------------------------------
        if False:  # we do not want to execute this in python when running the script
            # to change the working directory:
            %cd "your directory"
            # print the current working directory:
            %pwd
            # list the contents of the working directory:
            %ls
            # list current workspace variables:
            %who   # variable names
            %whos  # objects with additional information""")
    else:
        print("I'm sorry. This code only tells you the answer to Q1.2P.9 and Q1.2P.4 \nPlease try again.")

cheat("Q1.2P.9")






