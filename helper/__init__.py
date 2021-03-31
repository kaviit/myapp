
import os, subprocess

service_port = os.getenv("service_port")
service_name = os.getenv("service_name")
log_level = os.getenv("log_level")
version = os.getenv("version")

def get_details():
    """ Function to get the details """
    info = {
        "service_name": service_name,
        "version": version,
        "git_commit_sha": get_git_sha(),
        "service_port": service_port, 
        "log_level": log_level,
    }
    return info

def get_git_sha():
    """Get the GIT commit SHA from the git repository"""
    git_head_hash = (subprocess.check_output(["git", "rev-parse", "HEAD"]).decode("utf-8").rstrip("\n"))
    return git_head_hash
