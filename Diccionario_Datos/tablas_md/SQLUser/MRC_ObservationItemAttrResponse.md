# SQLUser.MRC_ObservationItemAttrResponse

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RESP_ParRef | varchar | PK |  | NO | - |
| Q16Q2 | - |  |  | SI | Tipo de Profesional |
| Q16Q3 | - |  |  | SI | RUT / Identificador Profesional |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| RESP_Childsub | double |  |  | NO | Childsub |
| RESP_Code | varchar |  |  | NO | Code |
| RESP_CreatedDate | date |  |  | SI | Created Date |
| RESP_CreatedTime | time |  |  | SI | Created Time |
| RESP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RESP_DateFrom | date |  |  | SI | Active Date From for new Observation Entries |
| RESP_DateTo | date |  |  | SI | Active Date To for new Observation Entries |
| RESP_Desc | varchar |  |  | NO | Description |
| RESP_Generated | varchar |  |  | SI | Response has been used in previous data - Code can... |
| RESP_RowId | varchar |  |  | NO | - |
| RESP_Score | double |  |  | SI | Score |
| RESP_SequenceOrder | double |  |  | SI | Sequence Order |
| RESP_UpdatedDate | date |  |  | SI | Updated Date |
| RESP_UpdatedTime | time |  |  | SI | Updated Time |
| RESP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*