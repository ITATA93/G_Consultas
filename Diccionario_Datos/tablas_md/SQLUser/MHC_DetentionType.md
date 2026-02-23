# SQLUser.MHC_DetentionType

**Schema:** SQLUser
**Columnas:** 31
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MHCDT_RowId | bigint | PK |  | NO | - |
| MHCDT_Code | varchar |  |  | NO | Code |
| MHCDT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| MHCDT_CommBasedEditable | varchar |  |  | SI | Community Based Editable |
| MHCDT_CommunityBased | varchar |  |  | SI | CommunityBased |
| MHCDT_CreatedDate | date |  |  | SI | Created Date |
| MHCDT_CreatedTime | time |  |  | SI | Created Time |
| MHCDT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MHCDT_DateFrom | date |  |  | SI | Date From |
| MHCDT_DateTo | date |  |  | SI | Date To |
| MHCDT_Desc | varchar |  |  | NO | Description |
| MHCDT_MaxDuration | double |  |  | SI | MaxDuration |
| MHCDT_MaxDurationUnits | varchar |  |  | SI | MaxDurationUnits |
| MHCDT_MinDuration | double |  |  | SI | MinDuration |
| MHCDT_MinDurationUnits | varchar |  |  | SI | MinDurationUnits |
| MHCDT_NationalCode | varchar |  |  | SI | NationalCode |
| MHCDT_NationalDesc | varchar |  |  | SI | NationalDescription |
| MHCDT_Owner | varchar |  |  | SI | Owner |
| MHCDT_PatConsentRequired | varchar |  |  | SI | PatientConsentRequired |
| MHCDT_RemindOffsetDays | double |  |  | SI | RemindOffsetDays |
| MHCDT_SecondOpinionRequired | varchar |  |  | SI | SecondOpinionRequired |
| MHCDT_UpdatedDate | date |  |  | SI | Updated Date |
| MHCDT_UpdatedTime | time |  |  | SI | Updated Time |
| MHCDT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| QRVDIQ1 | - |  |  | SI | Fecha |
| QRVDIQ2 | - |  |  | SI | Responsable |
| QRVDIQ3 | - |  |  | SI | N° de Visita |
| QRVDIQ4 | - |  |  | SI | Motivo de la visita |
| QRVDIQ5 | - |  |  | SI | Intervenciones o acciones realizadas y temas trata... |
| QRVDIQ6 | - |  |  | SI | Acuerdos tomados |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*