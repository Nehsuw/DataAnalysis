# AGENTS.md - Agentic Coding Guidelines

## Project Overview

AI-driven data analysis system with: **FastAPI** (Python) backend + **React/TypeScript** (Vite) frontend.

- Backend: `http://localhost:8708` (API at `/docs`)
- Frontend: `http://localhost:3000`
- Full pipeline: Upload → OCR → Structuring → Q&A → Visualization → PDF Export

---

## Build / Lint / Test Commands

### Frontend (React + TypeScript + Vite)

```bash
cd frontend

# Install dependencies
npm install

# Development server
npm run dev

# Production build
npm run build

# Preview production build
npm run preview

# Lint (ESLint)
npm run lint
```

**Running a single test**: No test framework configured (no Jest/Vitest). If adding tests later:
```bash
npm test              # Run all tests
npm test -- --testPathPattern=ComponentName  # Single test file
```

### Backend (Python + FastAPI)

```bash
cd backend

# Install dependencies
pip install -r requirements.txt

# Run service
python app.py
# or: uvicorn app:app --host 0.0.0.0 --port 8708 --reload

# Type checking (mypy - optional)
pip install mypy && mypy backend/ --ignore-missing-imports

# Linting (ruff - optional)
pip install ruff && ruff check backend/
```

**No formal test suite exists** - tests can be added with `pytest`:
```bash
pip install pytest pytest-asyncio
pytest              # Run all tests
pytest tests/test_api.py::test_name  # Single test
```

---

## Code Style Guidelines

### Frontend (TypeScript / React)

**Imports**:
```typescript
// React core first, then third-party, then local
import { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import { Button } from '@/components/ui/button';
import { useToast } from '@/components/ui/use-toast';
import { api } from './api';
import type { OCRResult } from './types';
```

**Formatting**:
- Use Prettier (enabled in project) - run `npm run lint` to format
- 2-space indentation, no tabs
- Single quotes for strings, semicolons at line ends
- Max line length: 100 characters

**Types**:
- Use explicit types for props, state, and API responses
- Avoid `any` - use `unknown` if type is truly unknown
- Use interfaces for objects, types for unions/aliases

```typescript
interface OCRResult {
  markdown: string;
  page_count: number;
  file_info?: {
    original_name: string;
    size_bytes: number;
  };
}
```

**Naming Conventions**:
- Components: PascalCase (`DataVisualization.tsx`)
- Hooks: camelCase with `use` prefix (`useAuth`)
- Constants: UPPER_SNAKE_CASE
- Files: kebab-case (`api-helper.ts`)
- Props interfaces: `{ComponentName}Props`

**Error Handling**:
- Use try/catch for async operations
- Display user-friendly error messages via toast
- Log errors to console with context

```typescript
try {
  const result = await api.uploadFile(file);
} catch (error) {
  console.error('Upload failed:', error);
  toast({ title: 'Error', description: 'Failed to upload file' });
}
```

---

### Backend (Python / FastAPI)

**Imports** (per PEP 8):
```python
# Standard library
import os
import json
from typing import Optional, Dict, Any

# Third-party
from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel

# Local application
from config.settings import settings
from services.ocr_service import OCRService
```

**Formatting**:
- Follow PEP 8 (run `ruff check` for auto-fix)
- 4-space indentation
- Max line length: 88 characters (Black default)

**Types** (type hints required):
```python
from typing import Optional

def process_file(file_path: str, enable_desc: bool = True) -> Dict[str, Any]:
    """Process a file with optional description.
    
    Args:
        file_path: Path to the file
        enable_desc: Whether to enable description
        
    Returns:
        Dictionary with processing results
    """
    pass
```

**Naming Conventions**:
- Functions/methods: snake_case (`def process_ocr_result`)
- Classes: PascalCase (`class DataAnalyzer`)
- Constants: UPPER_SNAKE_CASE
- Private methods: prefix with underscore

**Error Handling**:
- Use FastAPI's `HTTPException` for API errors
- Catch specific exceptions, not bare `Exception`
- Include traceback in logs for debugging

```python
from fastapi import HTTPException

@app.post("/ocr")
async def ocr_upload(file: UploadFile = File(...)):
    try:
        result = await process_file(file)
        return result
    except ValueError as e:
        raise HTTPException(400, f"Invalid file: {e}")
    except Exception as e:
        import traceback
        print(f"Processing failed: {e}")
        print(traceback.format_exc())
        raise HTTPException(500, "Internal server error")
```

---

## Architecture Patterns

### Frontend Component Structure

```typescript
// components/ComponentName.tsx
import { useState } from 'react';
import { cn } from '@/lib/utils';

interface ComponentNameProps {
  className?: string;
  onComplete?: (result: ResultType) => void;
}

export function ComponentName({ className, onComplete }: ComponentNameProps) {
  const [loading, setLoading] = useState(false);
  
  // Logic here
  
  return (
    <div className={cn("base-classes", className)}>
      {/* Content */}
    </div>
  );
}
```

### Backend API Endpoint Pattern

```python
@app.post("/endpoint")
async def handle_endpoint(request: RequestModel):
    """Endpoint description."""
    try:
        result = service.process(request)
        return {"status": "success", "data": result}
    except ValidationError as e:
        raise HTTPException(400, str(e))
```

---

## Important Project Notes

1. **API Connection**: Frontend connects to `localhost:8708` (hardcoded in `api.ts`)
2. **No Tests**: Project lacks test infrastructure - consider adding Jest/Vitest + pytest
3. **Environment Variables**: Backend uses `.env` for configuration
4. **CORS**: Enabled for all origins in development (`app.py`)
5. **shadcn/ui**: Components are in `components/ui/` - don't modify files directly, extend via props

---

## File Patterns to Follow

- Frontend components: `components/` (not `src/`)
- Backend services: `backend/services/`, `backend/core/`
- API definitions: `frontend/components/api.ts`
- Styles: Tailwind in `styles/globals.css`
- Configuration: `backend/config/settings.py`

---

## Common Development Tasks

**Add a new API endpoint**:
1. Add route in `backend/app.py`
2. Create service function in `backend/services/`
3. Add frontend API function in `frontend/components/api.ts`
4. Use new API in component

**Add a new UI component**:
1. Use existing shadcn component from `components/ui/`
2. Extend with custom props for project needs
3. Document in component if complex

**Modify OCR pipeline**:
1. Update `backend/core/analysis/data_analyzer.py`
2. Or modify `backend/backwark/Information_structuring.py`
3. Test with sample PDF in `pdfs/` directory