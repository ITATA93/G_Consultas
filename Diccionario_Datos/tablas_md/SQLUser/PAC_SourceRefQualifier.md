# SQLUser.PAC_SourceRefQualifier

**Schema:** SQLUser
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SRQ_RowId | bigint | PK |  | NO | - |
| SRQ_Code | varchar |  |  | NO | Code |
| SRQ_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SRQ_CreatedDate | date |  |  | SI | Created Date |
| SRQ_CreatedTime | time |  |  | SI | Created Time |
| SRQ_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SRQ_DateFrom | date |  |  | SI | DateFrom |
| SRQ_DateTo | date |  |  | SI | DateTo |
| SRQ_Desc | varchar |  |  | NO | Description |
| SRQ_NationalCode | varchar |  |  | SI | NationalCode |
| SRQ_Owner | varchar |  |  | SI | Owner |
| SRQ_RTTFlag | varchar |  |  | SI | RTTFlag |
| SRQ_RTTPathwayRequired | varchar |  |  | SI | RTTPathwayRequired  |
| SRQ_RTTPathway_DR | bigint |  | FK | SI | Des Ref RTTPathway |
| SRQ_UpdatedDate | date |  |  | SI | Updated Date |
| SRQ_UpdatedTime | time |  |  | SI | Updated Time |
| SRQ_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*