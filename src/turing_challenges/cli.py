import argparse
import sys
from .commands import handle_list, handle_info, handle_solve
from .errors import JSONNotFoundError, ChallengeNotFoundError, ChallengeNotInListError
from .display import print_error
from .loader import load_build_parser, get_challenge_readme

def build_parser():# -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Turing CLI - Liste et résout les challenges",
        formatter_class=argparse.RawTextHelpFormatter
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # LIST
    list_parser = subparsers.add_parser("list", help="Liste les challenges et leur état (résolu ou non)")
    
    # INFO
    info_parser = subparsers.add_parser("info", help="Affiche l'énoncé d'un challenge")
    info_parser.add_argument("n", type=int, help="Numéro du challenge")
    
    # SOLVE
    solve_parser = subparsers.add_parser("solve", help="Résout un challenge", add_help=False)
    solve_parser.add_argument("n", type=int, nargs="?", help="Numéro du challenge")
    solve_parser.add_argument("-h", "--help", action="store_true", help="Affiche l'aide générale ou spécifique")

    return parser


def main():

    parser = build_parser()
    args, unknown_args = parser.parse_known_args()

    try :
        if args.command == "list":
            handle_list()
            #return
        
        elif args.command == "info":
            handle_info(args.n)
            #return
        
        elif args.command == "solve":
            n = args.n

            if n is None:
                if args.help :
                    print("Usage général : turing solve <n> [options spécifiques au challenge]")
                    print("Exemple : turing solve 5 -v --max 100")
                    return
                else :
                    print_error("Vous devez spécifier un numéro de challenge.")
                    return
            
            # Création d'un parser temporaire pour le challenge n
            temp_parser = argparse.ArgumentParser(
                description=get_challenge_readme(n), 
                formatter_class=argparse.RawTextHelpFormatter
            )
                
            challenge_build_parser = load_build_parser(n)
            if challenge_build_parser:
                challenge_build_parser(temp_parser)

            if args.help : 
                temp_parser.print_help()
                return
            
            specific_args = vars(temp_parser.parse_args(unknown_args))
            handle_solve(n, **specific_args)
        
    except JSONNotFoundError as e :
        print_error(str(e))
    except ChallengeNotInListError as e :
        print_error(str(e))
    except ChallengeNotFoundError as e :
        print_error(str(e))
    except Exception as e:
        print_error(f"Erreur : {e}")
    return


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\nInterruption par l'utilisateur")
        sys.exit(130)
