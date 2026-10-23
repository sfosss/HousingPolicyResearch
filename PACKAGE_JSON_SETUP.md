# Package.json Configuration Guide

## Required: Create package.json

If you don't have a `package.json` file in your project root, create one:

### Minimal Setup (Recommended)

```json
{
  "name": "housing-policy-research",
  "version": "1.0.0",
  "description": "Housing policy research tools for Raycast",
  "main": "index.js",
  "type": "module",
  "scripts": {
    "dev": "raycast build --dev",
    "build": "raycast build",
    "lint": "eslint src --ext .ts,.tsx"
  },
  "dependencies": {
    "@raycast/api": "^1.70.0",
    "react": "^18.2.0"
  },
  "devDependencies": {
    "@raycast/eslint-config": "^1.0.0",
    "@types/react": "^18.2.0",
    "typescript": "^5.3.0"
  },
  "engines": {
    "node": ">=18.0.0"
  }
}
```

### Full Setup (with build tools)

```json
{
  "name": "housing-policy-research",
  "version": "1.0.0",
  "description": "Housing policy research tools for Raycast",
  "main": "index.js",
  "type": "module",
  "scripts": {
    "dev": "raycast build --dev",
    "build": "raycast build",
    "publish": "raycast publish",
    "lint": "eslint src --ext .ts,.tsx",
    "typecheck": "tsc --noEmit",
    "format": "prettier --write \"src/**/*.{ts,tsx}\""
  },
  "dependencies": {
    "@raycast/api": "^1.70.0",
    "react": "^18.2.0"
  },
  "devDependencies": {
    "@raycast/eslint-config": "^1.0.0",
    "@types/node": "^20.10.0",
    "@types/react": "^18.2.0",
    "@typescript-eslint/eslint-plugin": "^6.13.0",
    "@typescript-eslint/parser": "^6.13.0",
    "eslint": "^8.54.0",
    "prettier": "^3.1.0",
    "typescript": "^5.3.0"
  },
  "engines": {
    "node": ">=18.0.0"
  },
  "keywords": [
    "raycast",
    "housing",
    "policy",
    "research",
    "legislation",
    "sources"
  ],
  "author": "Housing Policy Research",
  "license": "MIT"
}
```

______________________________________________________________________

## TypeScript Configuration

Create a `tsconfig.json` file in your project root:

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "useDefineForClassFields": true,
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "skipLibCheck": true,
    "strict": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx",
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "noImplicitAny": true,
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true
  },
  "include": ["src"],
  "references": [
    { "path": "./tsconfig.node.json" }
  ]
}
```

Create `tsconfig.node.json`:

```json
{
  "compilerOptions": {
    "composite": true,
    "skipLibCheck": true,
    "module": "ESNext",
    "moduleResolution": "bundler",
    "allowSyntheticDefaultImports": true
  },
  "include": ["vite.config.ts"]
}
```

______________________________________________________________________

## ESLint Configuration

Create `.eslintrc.json`:

```json
{
  "extends": ["@raycast/eslint-config"],
  "parserOptions": {
    "ecmaVersion": 2020,
    "sourceType": "module",
    "ecmaFeatures": {
      "jsx": true
    }
  },
  "rules": {
    "no-console": "warn",
    "@typescript-eslint/no-explicit-any": "warn"
  }
}
```

______________________________________________________________________

## Installation & Build

### Step 1: Install Dependencies

```bash
cd ~/Documents/GitHub/HousingPolicyResearch

# Using npm
npm install

# Or using yarn
yarn install

# Or using pnpm
pnpm install
```

### Step 2: Verify Installation

```bash
# Check TypeScript
npm run typecheck

# Lint code
npm run lint

# Build extension
npm run build
```

### Step 3: Development Mode

```bash
# Start development server
npm run dev

# Extension will reload on file changes
```

### Step 4: Load into Raycast

```bash
# Keep dev server running in one terminal
npm run dev

# In Raycast:
# Cmd + Shift + A → "Load Extension" → Select your project directory
```

______________________________________________________________________

## Environment Setup

### Node.js Version

Ensure you have Node.js 18+:

```bash
node --version  # Should be v18.0.0 or higher
```

If you need to upgrade:

```bash
# Using Homebrew
brew install node

# Or using nvm (Node Version Manager)
nvm install 20
nvm use 20
```

### NPM Version

Ensure npm is up to date:

```bash
npm --version
npm install -g npm@latest
```

______________________________________________________________________

## Optional: .gitignore

Add this to `.gitignore`:

```
# Dependencies
node_modules/

# Build outputs
dist/
build/

# Logs
*.log
npm-debug.log*
yarn-debug.log*

# IDE
.idea/
.vscode/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Environment
.env
.env.local
.env.*.local
```

______________________________________________________________________

## Optional: Prettier Configuration

Create `.prettierrc.json`:

```json
{
  "semi": true,
  "singleQuote": false,
  "tabWidth": 2,
  "useTabs": false,
  "trailingComma": "es5",
  "bracketSpacing": true,
  "arrowParens": "always",
  "printWidth": 100
}
```

______________________________________________________________________

## Troubleshooting

### Issue: "Command not found: raycast"

**Solution:** The Raycast CLI tools may not be installed globally:

```bash
# Install Raycast CLI (if needed)
npm install -g @raycast/cli

# Or use npx
npx raycast build
```

### Issue: "Module not found: @raycast/api"

**Solution:** Dependencies not installed:

```bash
rm -rf node_modules
rm package-lock.json
npm install
```

### Issue: "TypeScript errors"

**Solution:** Ensure tsconfig.json exists and dependencies are installed:

```bash
npm install --save-dev typescript @types/react @types/node
npm run typecheck
```

### Issue: "ESLint errors"

**Solution:** Run formatter and fix issues:

```bash
npm run format
npm run lint -- --fix
```

______________________________________________________________________

## Verification Checklist

- [ ] `package.json` exists in project root
- [ ] `tsconfig.json` exists in project root
- [ ] `.eslintrc.json` exists in project root
- [ ] `node_modules/` directory created after `npm install`
- [ ] `npm run typecheck` passes without errors
- [ ] `npm run lint` passes or shows only warnings
- [ ] `npm run build` completes successfully
- [ ] `npm run dev` runs without errors
- [ ] Extension loads in Raycast (Cmd + Shift + A)

______________________________________________________________________

## Next Steps

1. Create `package.json` if it doesn't exist (copy one from above)
1. Run `npm install`
1. Run `npm run build`
1. Load extension into Raycast
1. Test all three commands

See `RAYCAST_QUICK_START.md` for testing instructions.

______________________________________________________________________

**Status:** ✅ Configuration Complete\
**Last Updated:** December 26, 2024
