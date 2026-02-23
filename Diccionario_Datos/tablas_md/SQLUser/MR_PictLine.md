# SQLUser.MR_PictLine

**Schema:** SQLUser
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MRPL_ParRef | varchar | PK |  | NO | MR_Pictures Parent Reference |
| MRPL_Childsub | double |  |  | NO | Childsub |
| MRPL_Line | varchar |  |  | SI | Line |
| MRPL_RowId | varchar |  |  | NO | - |
| Q02Q1 | - |  |  | SI | Drain Number |
| Q02Q2 | - |  |  | SI | Location |
| Q02Q3 | - |  |  | SI | Drainage Amount / Volume |
| Q02Q4 | - |  |  | SI | Drainage Type |
| Q02Q5 | - |  |  | SI | Days since Insertion |
| Q02Q6 | - |  |  | SI | Insertion Site Condition |
| Q02Q7 | - |  |  | SI | Comments |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*