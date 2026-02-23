# SQLUser.CT_HospitalKeyw

**Schema:** SQLUser
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Hospital**. Configuración del establecimiento.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| KEYW_ParRef | bigint | PK |  | NO | CT_Hospital Parent Reference |
| ChildQ81DR | - |  |  | SI | Child Reference: Eyes closed, foam surface |
| KEYW_Childsub | double |  |  | NO | Childsub |
| KEYW_Description | varchar |  |  | SI | Description |
| KEYW_RowId | varchar |  |  | NO | - |
| KEYW_Text | varchar |  |  | SI | Text |
| Q80Q1 | - |  |  | SI | Time |
| Q80Q2 | - |  |  | SI | Strategy |
| Q80Q3 | - |  |  | SI | Sway |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*