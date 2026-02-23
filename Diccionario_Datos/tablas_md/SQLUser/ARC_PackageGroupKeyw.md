# SQLUser.ARC_PackageGroupKeyw

**Schema:** SQLUser
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| KEYW_ParRef | bigint | PK |  | NO | ARC_PackageGroup Parent Reference |
| KEYW_Childsub | double |  |  | NO | Childsub |
| KEYW_Description | varchar |  |  | SI | Description |
| KEYW_RowId | varchar |  |  | NO | - |
| KEYW_Text | varchar |  |  | SI | Text |
| Q01Q1 | - |  |  | SI | Eje Diagnóstico |
| Q01Q2 | - |  |  | SI | Diagnóstico |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*