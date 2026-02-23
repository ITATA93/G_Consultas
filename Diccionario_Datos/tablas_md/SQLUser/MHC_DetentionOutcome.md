# SQLUser.MHC_DetentionOutcome

**Schema:** SQLUser
**Columnas:** 24
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Detalle de la entidad padre.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MHCDO_RowId | bigint | PK |  | NO | - |
| ChildQRVDIDR | - |  |  | SI | Child Reference: Resumen Visita Diaria Integral |
| MHCDO_Code | varchar |  |  | NO | Code |
| MHCDO_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| MHCDO_CreatedDate | date |  |  | SI | Created Date |
| MHCDO_CreatedTime | time |  |  | SI | Created Time |
| MHCDO_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MHCDO_DateFrom | date |  |  | SI | Date From |
| MHCDO_DateTo | date |  |  | SI | Date To |
| MHCDO_Desc | varchar |  |  | NO | Description |
| MHCDO_Owner | varchar |  |  | SI | Owner |
| MHCDO_TribunalOnly | varchar |  |  | SI | TribunalOnly  |
| MHCDO_TriggerDetention_DR | bigint |  | FK | SI | Des Ref MHCDetentionType |
| MHCDO_UpdatedDate | date |  |  | SI | Updated Date |
| MHCDO_UpdatedTime | time |  |  | SI | Updated Time |
| MHCDO_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| QRRQ1 | - |  |  | SI | Problemas Detectados |
| QRRQ2 | - |  |  | SI | Caso Índice / Familiar |
| QRRQ3 | - |  |  | SI | Plan de acción y acuerdos |
| QRRQ4 | - |  |  | SI | Responsable |
| QRRQ5 | - |  |  | SI | Tiempo de ejecución |
| QRRQ6 | - |  |  | SI | Evaluación |
| QRRQ7 | - |  |  | SI | Observación |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*