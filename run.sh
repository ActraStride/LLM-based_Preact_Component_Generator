#!/bin/bash
# ============================================
# FILE: run.sh (VERSIÓN CORREGIDA)
# ============================================

# Crear directorio output si no existe
mkdir -p output/components

# Ejecutar con volumen montado, pero como el usuario actual
# $(id -u) obtiene tu ID de usuario (ej: 1000)
# $(id -g) obtiene tu ID de grupo (ej: 1000)
docker run --rm -it \
  --user "$(id -u):$(id -g)" \
  --env-file generator/.env \
  -v "$(pwd)/output:/app/output" \
  llm-generator

# Mostrar archivos generados
echo ""
echo "📂 Archivos generados:"
find output/components -name "*.tsx" -type f 2>/dev/null | while read file; do
  echo "   📄 $file"
done