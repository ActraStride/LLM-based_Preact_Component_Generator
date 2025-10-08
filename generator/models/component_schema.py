# ============================================
# FILE: generator/models/component_schema.py
# ============================================

from pydantic import BaseModel, Field
from typing import List

class ComponentFile(BaseModel):
    """Represents a single generated file with its path and content."""
    path: str = Field(
        ..., 
        description="Relative path for the file (e.g., 'src/components/Button/Button.tsx')"
    )
    content: str = Field(
        ..., 
        description="The full source code or content of the file."
    )

# Hemos eliminado ComponentMetadata y ComponentResponse por ahora para la prueba.