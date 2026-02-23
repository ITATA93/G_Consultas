# SQLUser.OE_OrdSubCateg

**Schema:** SQLUser
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Órdenes Médicas**. Solicitudes de exámenes, procedimientos, etc.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SUBCAT_ParRef | numeric | PK |  | NO | OE_Order Parent Reference |
| ChildQ26DR | - |  |  | SI | Child Reference: Cortical Sensation |
| Q25Q1 | - |  |  | SI | Location |
| Q25Q2 | - |  |  | SI | Criteria |
| Q25Q3 | - |  |  | SI | Score |
| Q25Q4 | - |  |  | SI | Comments |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| SUBCAT_Qty | double |  |  | SI | Qty |
| SUBCAT_RowId | varchar |  |  | NO | - |
| SUBCAT_SubCateg_DR | bigint |  | FK | NO | Des Ref ARCItemCat |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*