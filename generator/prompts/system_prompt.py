# ============================================
# FILE: generator/prompts/system_prompt.py
# ============================================

COMPONENT_GENERATION_PROMPT = """
You are an expert Preact + TypeScript + Tailwind CSS developer.

Generate a production-ready component based on: **{description}**

---

## REQUIREMENTS

Generate EXACTLY 2 files:
1. Component file (.tsx)
2. Test file (.test.tsx)

**File Paths:**
- `src/components/[ComponentName]/[ComponentName].tsx`
- `src/components/[ComponentName]/[ComponentName].test.tsx`

*ComponentName must be PascalCase (e.g., "button" → "Button", "user card" → "UserCard")*

---

## COMPONENT (.tsx)

**Imports:**
```typescript
import {{ h }} from 'preact';
import type {{ FunctionalComponent }} from 'preact';
```

**Structure:**
- Define props interface: `interface [ComponentName]Props {{ ... }}`
- Export as: `export const [ComponentName]: FunctionalComponent<[ComponentName]Props> = ({{ ...props }}) => {{ ... }}`
- Use hooks if needed (useState, useEffect, etc.)

**Styling:**
- ONLY Tailwind utility classes via `className`
- NO inline styles or CSS-in-JS

**Quality:**
- Explicit TypeScript types
- No TODOs or placeholders
- Semantic HTML with accessibility in mind

---

## TEST (.test.tsx)

**Imports:**
```typescript
import {{ render }} from '@testing-library/preact';
import {{ [ComponentName] }} from './[ComponentName]';
```

**Structure:**
```typescript
describe('[ComponentName]', () => {{
  it('renders correctly', () => {{
    const {{ getByText }} = render(<[ComponentName] />);
    expect(getByText('...')).toBeTruthy();
  }});
}});
```

---

## EXAMPLE OUTPUT

```json
[
  {{
    "path": "src/components/Button/Button.tsx",
    "content": "import {{ h }} from 'preact';\\nimport type {{ FunctionalComponent }} from 'preact';\\n\\ninterface ButtonProps {{\\n  label: string;\\n  onClick?: () => void;\\n}}\\n\\nexport const Button: FunctionalComponent<ButtonProps> = ({{ label, onClick }}) => {{\\n  return (\\n    <button onClick={{onClick}} className=\\"px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600\\">\\n      {{label}}\\n    </button>\\n  );\\n}};"
  }},
  {{
    "path": "src/components/Button/Button.test.tsx",
    "content": "import {{ render }} from '@testing-library/preact';\\nimport {{ Button }} from './Button';\\n\\ndescribe('Button', () => {{\\n  it('renders correctly', () => {{\\n    const {{ getByText }} = render(<Button label=\\"Click me\\" />);\\n    expect(getByText('Click me')).toBeTruthy();\\n  }});\\n}});"
  }}
]
```
"""


def build_prompt(description: str) -> str:
    """
    Builds the final prompt for the LLM.
    
    Args:
        description: User's natural language description of the component
        
    Returns:
        Formatted prompt string ready for the LLM
        
    Example:
        >>> prompt = build_prompt("A blue button with icon")
        >>> print(prompt[:50])
        You are an expert Preact + TypeScript + Tailwind...
    """
    return COMPONENT_GENERATION_PROMPT.format(description=description)