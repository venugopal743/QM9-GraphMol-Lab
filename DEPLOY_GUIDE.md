# Deployment Guide — QM9-GraphMol Lab (GitHub & Vercel)

This project is fully prepared for continuous deployment on **GitHub** and **Vercel** with Python serverless function support.

---

## Part 1: Push to GitHub

1. Create a new repository on GitHub:
   * Go to [github.com/new](https://github.com/new)
   * Repository name: e.g. `QM9-GraphMol-Lab` (or `molecular-ai`)
   * Choose **Public** or **Private**
   * **Do not** initialize with README or .gitignore (they are already created)
   * Click **Create repository**

2. Link your local project to GitHub and push:
   Open **PowerShell** or **Command Prompt** and run:
   ```bash
   cd "C:\Users\chunc_yhjtd63\.gemini\antigravity\scratch\qm9-gnn-project\QM9-GNN-Molecular-AI"
   git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/<YOUR_REPO_NAME>.git
   git push -u origin main
   ```
   *(Replace `<YOUR_GITHUB_USERNAME>` and `<YOUR_REPO_NAME>` with your actual GitHub username and repository name)*

---

## Part 2: Deploy to Vercel

### Method A: Connect with GitHub (Recommended — Auto-deploys on every git push)
1. Go to [vercel.com](https://vercel.com) and log in with your GitHub account.
2. Click **Add New...** $\rightarrow$ **Project**.
3. Find your repository `QM9-GraphMol-Lab` in the list and click **Import**.
4. Vercel will automatically read `vercel.json` and `api/index.py`.
5. Click **Deploy**.
6. In ~30–45 seconds, your app will be live with a URL like `https://qm9-graphmol-lab.vercel.app`!

---

### Method B: Deploy from Terminal via Vercel CLI
You can also deploy directly from your local terminal using `npx`:
```bash
cd "C:\Users\chunc_yhjtd63\.gemini\antigravity\scratch\qm9-gnn-project\QM9-GNN-Molecular-AI"
npx vercel
```
* Follow the on-screen prompts (log in with your browser if requested).
* When asked `Set up and deploy?`, type `Y`.
* To deploy directly to production:
  ```bash
  npx vercel --prod
  ```

---

## Technical Configuration Details
* **Entrypoint**: [`api/index.py`](api/index.py) exports the FastAPI `app`.
* **Vercel Configuration**: [`vercel.json`](vercel.json) routes all requests to `@vercel/python`.
* **Dependencies**: [`requirements.txt`](requirements.txt) contains optimized serverless dependencies (FastAPI, Uvicorn, RDKit, NumPy, Pandas) that fit within Vercel's 250MB lambda limit.
* **Model Training**: PyTorch & PyTorch Geometric dependencies are preserved in [`requirements-train.txt`](requirements-train.txt) for local training.
