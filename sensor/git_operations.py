import subprocess
from typing import List, Dict, Optional
import os

class GitOperations:
    """Handle all git operations"""
    
    def __init__(self, repo_path: str = "."):
        self.repo_path = repo_path
        os.chdir(self.repo_path)
    
    def _run_command(self, command: List[str]) -> Dict[str, str]:
        """Execute git command and return output"""
        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            return {"status": "success", "output": result.stdout.strip()}
        except subprocess.CalledProcessError as e:
            return {"status": "error", "output": e.stderr.strip()}
    
    def commit(self, message: str, all: bool = False) -> Dict[str, str]:
        """Commit changes"""
        cmd = ["git", "commit"]
        if all:
            cmd.append("-a")
        cmd.extend(["-m", message])
        return self._run_command(cmd)
    
    def push(self, branch: str = "main", force: bool = False) -> Dict[str, str]:
        """Push changes to remote"""
        cmd = ["git", "push", "origin", branch]
        if force:
            cmd.append("-f")
        return self._run_command(cmd)
    
    def pull(self, branch: str = "main") -> Dict[str, str]:
        """Pull changes from remote"""
        cmd = ["git", "pull", "origin", branch]
        return self._run_command(cmd)
    
    def create_branch(self, branch_name: str) -> Dict[str, str]:
        """Create new branch"""
        cmd = ["git", "checkout", "-b", branch_name]
        return self._run_command(cmd)
    
    def checkout_branch(self, branch_name: str) -> Dict[str, str]:
        """Checkout existing branch"""
        cmd = ["git", "checkout", branch_name]
        return self._run_command(cmd)
    
    def list_branches(self) -> Dict[str, str]:
        """List all branches"""
        cmd = ["git", "branch", "-a"]
        return self._run_command(cmd)
    
    def merge(self, branch_name: str) -> Dict[str, str]:
        """Merge branch into current branch"""
        cmd = ["git", "merge", branch_name]
        return self._run_command(cmd)
    
    def stash(self, message: str = "") -> Dict[str, str]:
        """Stash changes"""
        cmd = ["git", "stash", "push"]
        if message:
            cmd.extend(["-m", message])
        return self._run_command(cmd)
    
    def stash_pop(self) -> Dict[str, str]:
        """Pop stashed changes"""
        cmd = ["git", "stash", "pop"]
        return self._run_command(cmd)
    
    def rebase(self, branch_name: str) -> Dict[str, str]:
        """Rebase current branch onto another branch"""
        cmd = ["git", "rebase", branch_name]
        return self._run_command(cmd)
    
    def create_tag(self, tag_name: str, message: str = "") -> Dict[str, str]:
        """Create git tag"""
        cmd = ["git", "tag", tag_name]
        if message:
            cmd.extend(["-a", "-m", message])
        return self._run_command(cmd)
    
    def delete_tag(self, tag_name: str) -> Dict[str, str]:
        """Delete git tag"""
        cmd = ["git", "tag", "-d", tag_name]
        return self._run_command(cmd)
    
    def list_tags(self) -> Dict[str, str]:
        """List all tags"""
        cmd = ["git", "tag"]
        return self._run_command(cmd)
    
    def status(self) -> Dict[str, str]:
        """Get git status"""
        cmd = ["git", "status"]
        return self._run_command(cmd)
    
    def add(self, files: List[str] = None, all: bool = False) -> Dict[str, str]:
        """Stage files"""
        cmd = ["git", "add"]
        if all:
            cmd.append(".")
        elif files:
            cmd.extend(files)
        return self._run_command(cmd)
