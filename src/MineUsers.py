import RedditParser


def Save_Reddit_User_Names(file_name, subreddit, number):
    name_set = set()
    try:
        with open(file_name, "r") as f:
            for line in f:
                name_set.add(line.rstrip())
    except:
        pass
    with open(file_name, "a+") as f:
        k = 0
        for user in RedditParser.All_Users(subreddit, users=name_set):
            f.write(user + "\n")
            k += 1
            if k % 100 == 0:
                print k
            if k == number:
                break    

def Save_Random_User_Names(file_name):
    name_set = set()
    try:
        with open(file_name, "r") as f:
            for line in f:
                name_set.add(line.rstrip())
    except:
        pass
    with open(file_name, "a+") as f:
        k = len(name_set)
        for user in RedditParser.Random_User_Stream(users=name_set):
            f.write(user + "\n")
            k += 1
            if k % 100 == 0:
                print k
            

if __name__ == "__main__":
    Save_Random_User_Names("user_names_rand.txt")
    #Save_Reddit_User_Names("user_names_meg.txt", "metal", 200)
