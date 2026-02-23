# SQLUser.OE_OrdResultCodes

**Schema:** SQLUser
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Órdenes Médicas**. Solicitudes de exámenes, procedimientos, etc.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| COD_ParRef | varchar | PK |  | NO | OE_OrdResult Parent Reference |
| COD_Childsub | double |  |  | NO | Childsub |
| COD_RowId | varchar |  |  | NO | - |
| COD_WordResutCode_DR | bigint |  | FK | SI | Des Ref Word Resut Code |
| Q68Q1 | - |  |  | SI | Assessed By |
| Q68Q2 | - |  |  | SI | Date |
| Q68Q3 | - |  |  | SI | Order / Garment type |
| Q68Q4 | - |  |  | SI | Relevant funding body |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*