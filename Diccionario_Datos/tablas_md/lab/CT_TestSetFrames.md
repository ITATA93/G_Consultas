# lab.CT_TestSetFrames

**Schema:** lab
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTTSA_ParRef | varchar | PK |  | NO | CT_TestSet Parent Reference |
| CTTSA_Code | numeric |  |  | NO | Frame code |
| CTTSA_Name | varchar |  |  | SI | Frame Name |
| CTTSA_RowID | varchar |  |  | NO | - |
| CTTSA_Sequence | numeric |  |  | SI | Sequence number |
| CTTSA_Title | varchar |  |  | SI | Display Title |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*