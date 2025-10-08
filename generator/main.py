# ============================================
# FILE: main.py
# ============================================
import os
from pathlib import Path
from dotenv import load_dotenv
from core.generator import ComponentGenerator

def main():
    """CLI entry point for component generation"""
    load_dotenv()
    
    # Get API key
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("❌ Error: GEMINI_API_KEY not found in .env")
        return
    
    print("🧩 LLM-based Preact Component Generator")
    print("=" * 50)
    
    # Initialize generator
    generator = ComponentGenerator(
        api_key=api_key,
        output_dir="./output/components"
    )
    
    # Get user input
    description = input("\n📝 Describe el componente: ")
    
    if not description.strip():
        print("❌ Error: Description cannot be empty")
        return
    
    try:
        # Generate component (returns List[ComponentFile])
        files = generator.generate(description)
        
        # Display summary
        print("\n" + "=" * 50)
        print("📦 Generation Summary")
        print(f"📁 Total files: {len(files)}")
        print()
        
        # Show each file
        for file in files:
            # Determine file type
            if ".test." in file.path:
                file_type = "🧪 Test"
            else:
                file_type = "⚛️  Component"
            
            # Get file size
            file_size = len(file.content)
            
            print(f"{file_type:12} {file.path}")
            print(f"             └─ {file_size} characters")
        
        # Extract component name from path
        component_name = Path(files[0].path).stem
        
        print()
        print(f"✨ Component '{component_name}' ready to use!")
        print(f"📂 Location: ./output/components/")
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()