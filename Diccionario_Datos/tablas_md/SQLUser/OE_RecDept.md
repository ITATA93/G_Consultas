# SQLUser.OE_RecDept

**Schema:** SQLUser
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OEREC_OEORD_ParRef | numeric | PK |  | NO | Des Ref to OEORD |
| ChildQ69DR | - |  |  | SI | Child Reference: Range of Motion (ROM) |
| OEREC_CTLOC_DR | bigint |  | FK | SI | Des Ref to CTLOC |
| OEREC_Childsub | double |  |  | NO | OEORC Child Sub (New key) |
| OEREC_Match | varchar |  |  | SI | Match Field |
| OEREC_RowId | varchar |  |  | NO | - |
| Q32Q1 | - |  |  | SI | Activity |
| Q32Q2 | - |  |  | SI | Condition |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*