from main import app


@app.get("/repos")
async def get_repos():
    return {"message": "List of repositories"}


@app.get("/repos/{repo_id}")
async def get_repo(repo_id: str):
    return {"repo_id": "{repo_id}"}


@app.get("/repos/{repo_id}/prs")
async def get_prs_by_repo(repo_id: str):
    return {"repo_id": "{repo_id}"}


@app.get("/repos/{repo_id}/prs/{pr_id}")
async def get_pr(repo_id: str, pr_id: str):
    return {"repo_id": "{repo_id}"}


@app.post("/repos/{repo_id}/prs/{pr_id}/analyze")
async def analyze_repo(repo_id: str, pr_id: str):
    return "analyze repo"
