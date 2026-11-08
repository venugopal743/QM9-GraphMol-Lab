from pathlib import Path
import uvicorn

ROOT = Path(__file__).resolve().parent

if __name__ == '__main__':
    print('=' * 65)
    print('  QM9-GraphMol LAB — Molecular GNN Research Platform')
    print('  Server running at: http://127.0.0.1:8000')
    print('=' * 65)
    uvicorn.run('web.app:app', host='127.0.0.1', port=8000, reload=False)
