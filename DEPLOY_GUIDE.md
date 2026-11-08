# Deployment Guide — QM9-GraphMol Lab (GitHub & Vercel)

This project is fully prepared for continuous deployment on **GitHub** and **Vercel** with Python serverless function support.

---

## Part 1: GitHub Pages & Repository

Your repository is connected at:
`https://github.com/venugopal743/QM9-GraphMol-Lab`

### GitHub Pages (Instant Free Web Hosting)
1. Go to your repository **Settings** $\rightarrow$ **Pages** (in the left sidebar).
2. Under **Build and deployment**:
   * **Source**: `Deploy from a branch`
   * **Branch**: `main`
   * **Folder**: `/ (root)`
3. Click **Save**.
4. GitHub Pages will build in under 30 seconds with a green checkmark `✓`!
5. Your live site will be accessible at:
   **`https://venugopal743.github.io/QM9-GraphMol-Lab/`**

> [!NOTE]
> Root `index.html`, `assets/`, `.nojekyll`, and `library_bundle.json` are preconfigured so the site runs completely in static mode on GitHub Pages, including 17 curated molecules, live kinetic canvas preview, downside working analysis, and animated benchmark graphs.

---

## Part 2: Deploy to Vercel (Full Python FastAPI Serverless Backend)

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
