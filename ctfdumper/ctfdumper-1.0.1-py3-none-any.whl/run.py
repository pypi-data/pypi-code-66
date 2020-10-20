import argparse, getpass
from ctfdumper.ctfdumper import CTFDumper

banner = """
  ___  ____  ____  ____  _  _  _  _  ____  ____  ____
 / __)(_  _)(  __)(    \\/ )( \\( \\/ )(  _ \\(  __)(  _ \\
( (__   )(   ) _)  ) D () \\/ (/ \\/ \\ ) __/ ) _)  )   /
 \\___) (__) (__)  (____/\\____/\\_)(_/(__)  (____)(__\\_)
"""

def parse_args():
    parser =  argparse.ArgumentParser(description="Dumps the submissions from a CTFD website")

    parser.add_argument('url',
                            type=str,
                            help='the url for the CTFD site example "https://demo.ctf.org"')

    parser.add_argument('-t', '--threads',
                            type=int,
                            help='the number of threads to use when dumping data',
                            default=10)

    parser.add_argument('-u', '--username',
                            type=str,
                            help='the username to login as')

    parser.add_argument('-o', '--output',
                            type=str,
                            help='location to save the csv file of the submission data',
                            required=True)

    return parser.parse_args()

def main():
    print(banner, end='\n\n')

    args = parse_args()

    username = input("CTFD Username: ") if not args.username else args.username
    threads = args.threads

    dumper = CTFDumper(args.url, threads=threads)
    submissions = dumper.get_submissions(username, getpass.getpass(prompt="CTFD Password: "))

    submissions.to_csv(args.output, index=False)

    print("Submissions saved to {}".format(args.output))

if __name__ == "__main__":
    main()
