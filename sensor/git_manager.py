import argparse
from git_operations import GitOperations

def main():
    parser = argparse.ArgumentParser(description="Git Operations Manager")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Commit
    commit_parser = subparsers.add_parser("commit", help="Commit changes")
    commit_parser.add_argument("message", help="Commit message")
    commit_parser.add_argument("-a", "--all", action="store_true", help="Commit all changes")
    
    # Push
    push_parser = subparsers.add_parser("push", help="Push to remote")
    push_parser.add_argument("-b", "--branch", default="main", help="Branch name")
    push_parser.add_argument("-f", "--force", action="store_true", help="Force push")
    
    # Pull
    pull_parser = subparsers.add_parser("pull", help="Pull from remote")
    pull_parser.add_argument("-b", "--branch", default="main", help="Branch name")
    
    # Branch operations
    branch_parser = subparsers.add_parser("branch", help="Branch operations")
    branch_parser.add_argument("action", choices=["create", "checkout", "list"])
    branch_parser.add_argument("name", nargs="?", help="Branch name")
    
    # Merge
    merge_parser = subparsers.add_parser("merge", help="Merge branch")
    merge_parser.add_argument("branch", help="Branch to merge")
    
    # Stash
    stash_parser = subparsers.add_parser("stash", help="Stash operations")
    stash_parser.add_argument("action", choices=["save", "pop"], default="save")
    stash_parser.add_argument("-m", "--message", help="Stash message")
    
    # Rebase
    rebase_parser = subparsers.add_parser("rebase", help="Rebase branch")
    rebase_parser.add_argument("branch", help="Branch to rebase onto")
    
    # Tag
    tag_parser = subparsers.add_parser("tag", help="Tag operations")
    tag_parser.add_argument("action", choices=["create", "delete", "list"])
    tag_parser.add_argument("name", nargs="?", help="Tag name")
    tag_parser.add_argument("-m", "--message", help="Tag message")
    
    # Status
    subparsers.add_parser("status", help="Show git status")
    
    # Add
    add_parser = subparsers.add_parser("add", help="Stage files")
    add_parser.add_argument("files", nargs="*", help="Files to stage")
    add_parser.add_argument("-a", "--all", action="store_true", help="Stage all changes")
    
    args = parser.parse_args()
    git = GitOperations()
    
    if args.command == "commit":
        result = git.commit(args.message, args.all)
    elif args.command == "push":
        result = git.push(args.branch, args.force)
    elif args.command == "pull":
        result = git.pull(args.branch)
    elif args.command == "branch":
        if args.action == "create":
            result = git.create_branch(args.name)
        elif args.action == "checkout":
            result = git.checkout_branch(args.name)
        else:
            result = git.list_branches()
    elif args.command == "merge":
        result = git.merge(args.branch)
    elif args.command == "stash":
        if args.action == "save":
            result = git.stash(args.message or "")
        else:
            result = git.stash_pop()
    elif args.command == "rebase":
        result = git.rebase(args.branch)
    elif args.command == "tag":
        if args.action == "create":
            result = git.create_tag(args.name, args.message or "")
        elif args.action == "delete":
            result = git.delete_tag(args.name)
        else:
            result = git.list_tags()
    elif args.command == "status":
        result = git.status()
    elif args.command == "add":
        result = git.add(args.files if args.files else None, args.all)
    else:
        parser.print_help()
        return
    
    print(f"[{result['status'].upper()}] {result['output']}")

if __name__ == "__main__":
    main()
