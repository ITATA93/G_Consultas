# SQLUser.MRC_DiagnosSignSymptom

**Schema:** SQLUser
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DSYM_RowId | bigint | PK |  | NO | - |
| ChildQ81DR | - |  |  | SI | Child Reference: Psicomotricidad |
| DSYM_ARCOS_DR | varchar |  | FK | SI | Des Ref ARCOS |
| DSYM_ActiveInActive | varchar |  |  | SI | Active InActive |
| DSYM_CTLOC_DR | bigint |  | FK | SI | Des Ref to CTLOC |
| DSYM_Code | varchar |  |  | NO | Code |
| DSYM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DSYM_CreatedDate | date |  |  | SI | Created Date |
| DSYM_CreatedTime | time |  |  | SI | Created Time |
| DSYM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DSYM_DateFrom | date |  |  | SI | Date From |
| DSYM_DateTo | date |  |  | SI | Date To |
| DSYM_Desc | varchar |  |  | NO | Description |
| DSYM_Owner | varchar |  |  | SI | Owner |
| DSYM_TriageSequence | integer |  |  | SI | Triage Sequence |
| DSYM_UpdatedDate | date |  |  | SI | Updated Date |
| DSYM_UpdatedTime | time |  |  | SI | Updated Time |
| DSYM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q80Q1 | - |  |  | SI | Evaluación |
| Q80Q2 | - |  |  | SI | Comentario (Texto libre) |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*