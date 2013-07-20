import argparse

import github




def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--user')
    parser.add_argument('-p', '--password')

    names = parser.parse_args()
    user_name, password = names.user, names.password

    gh = github.GitHub(user_name, password)
    # user = gh.users(user_name).get()
    repos = gh.users(user_name).repos.get()
    print repos

if __name__ == "__main__":
    main()

