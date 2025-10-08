# ============================================
# FILE: generator/core/generator.py
# ============================================
from pathlib import Path
from typing import List
from clients.gemini_client import GeminiClient
from models.component_schema import ComponentFile
from prompts.system_prompt import build_prompt

class ComponentGenerator:
    """Generates Preact components using LLM structured output"""
    
    def __init__(self, api_key: str, output_dir: str = "./output"):
        """
        Args:
            api_key: Gemini API key
            output_dir: Directory to save generated components
        """
        self.client = GeminiClient(api_key)
        self.output_dir = Path(output_dir)
    
    def generate(self, description: str) -> List[ComponentFile]:
        """
        Generates a complete component from a description.
        
        Args:
            description: Natural language description of the component
            
        Returns:
            List of ComponentFile objects (component + test)
        """
        print("🤖 Generating component with AI...")
        
        # 1. Build prompt
        prompt = build_prompt(description)
        
        # 2. Call Gemini with simple schema
        try:
            files: List[ComponentFile] = self.client.generate_structured(
                prompt=prompt,
                response_schema=List[ComponentFile]
            )
        except Exception as e:
            raise RuntimeError(f"Error generating component: {str(e)}")
        
        # 3. Validate
        if not files:
            raise ValueError("The model did not generate any files")
        
        print(f"✅ Generated {len(files)} files")
        
        # 4. Save files to disk
        for file in files:
            filepath = self.output_dir / file.path
            filepath.parent.mkdir(parents=True, exist_ok=True)
            filepath.write_text(file.content, encoding='utf-8')
            print(f"   📄 {file.path}")
        
        # 5. Extract component name from first file path
        component_name = self._extract_component_name(files[0].path)
        print(f"\n✨ Component '{component_name}' generated successfully")
        
        return files
    
    def generate_variants(
        self, 
        description: str, 
        count: int = 3
    ) -> List[List[ComponentFile]]:
        """
        Generates multiple variants of the same component.
        
        Args:
            description: Base description
            count: Number of variants to generate
            
        Returns:
            List of file lists (one per variant)
        """
        variants = []
        
        for i in range(1, count + 1):
            print(f"\n🎨 Generating variant {i}/{count}...")
            
            # Modify prompt for variation
            variant_prompt = f"{description}\n\nStyle variation #{i}: Use a different visual approach."
            files = self.generate(variant_prompt)
            variants.append(files)
        
        return variants
    
    def _extract_component_name(self, path: str) -> str:
        """
        Extracts component name from file path.
        
        Example: 'src/components/Button/Button.tsx' -> 'Button'
        """
        return Path(path).stem  # Returns filename without extension