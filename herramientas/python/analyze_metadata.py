import pandas as pd
import os

excel_path = 'c:/_Consultas/datos_alma/data/Columnas.xlsx'

print(f"Reading local Excel file: {excel_path}...")
try:
    # Row 2 contains headers (0-indexed is row 2)
    df = pd.read_excel(excel_path, header=2)
    
    # Filter for relevant columns (assuming names match the inspect output)
    # TABLE_NAME, COLUMN_NAME, DATA_TYPE, DESCRIPTION
    # Rename for clarity if needed, but let's just use them
    df_clean = df[['TABLE_NAME', 'COLUMN_NAME', 'DESCRIPTION', 'DATA_TYPE']].copy()
    
    # Drop rows where TABLE_NAME is NaN (artifacts of the sql paste)
    df_clean = df_clean.dropna(subset=['TABLE_NAME'])
    
    print("\n--- Clinical Data Dictionary Preview (First 20 entries) ---")
    print(df_clean.head(20).to_markdown(index=False))
    
    # Save full markdown dictionary
    md_path = 'c:/_Consultas/diccionario_preliminar.md'
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write("# Diccionario de Datos Clínico ALMA (IRIS)\n\n")
        f.write("Generado a partir de metadatos locales.\n\n")
        
        # Group by Table
        for table, group in df_clean.groupby('TABLE_NAME'):
            f.write(f"## Tabla: {table}\n\n")
            f.write(group[['COLUMN_NAME', 'DATA_TYPE', 'DESCRIPTION']].to_markdown(index=False))
            f.write("\n\n")
            
    print(f"\nFull dictionary generated at: {md_path}")
    
except Exception as e:
    print(f"Error reading Excel: {e}")
    # Fallback debug
    df = pd.read_excel(excel_path, header=None)
    print("Raw row 2:", df.iloc[2].tolist())
