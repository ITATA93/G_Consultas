# SQLUser.PA_DepAdm

**Schema:** SQLUser
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DEPADM_RowId | bigint | PK |  | NO | - |
| ChildQ75DR | - |  |  | SI | Child Reference: Treatment Provided |
| DEPADM_BookedStatus | varchar |  |  | SI | BookedStatus  |
| DEPADM_Location_DR | bigint |  | FK | SI | Des Ref CTLOC, Location where the patient was at t... |
| DEPADM_PAADM_DR | bigint |  | FK | SI | Des Ref PAADM |
| DEPADM_ReqLoc_DR | bigint |  | FK | SI | Des Ref CTLOC |
| DEPADM_Trans_DR | varchar |  | FK | SI | Des Ref PAAdmTransaction                     |
| Q74Q1 | - |  |  | SI | Date |
| Q74Q2 | - |  |  | SI | Time |
| Q74Q3 | - |  |  | SI | When |
| Q74Q4 | - |  |  | SI | Pain medication status |
| Q74Q5 | - |  |  | SI | Description |
| Q74Q6 | - |  |  | SI | Patient scale |
| Q74Q7 | - |  |  | SI | Pain comments |
| Q74Q8 | - |  |  | SI | Entered by |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*