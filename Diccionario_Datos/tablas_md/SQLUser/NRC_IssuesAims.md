# SQLUser.NRC_IssuesAims

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Enfermería**. Parámetros de enfermería.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| NRCIA_ParRef | bigint | PK |  | NO | NRCIssues Parent Reference |
| NRCIA_Aim_DR | bigint |  | FK | SI | Des Ref MRCCareAim |
| NRCIA_Childsub | double |  |  | NO | Childsub |
| NRCIA_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| NRCIA_CreatedDate | date |  |  | SI | Created Date |
| NRCIA_CreatedTime | time |  |  | SI | Created Time |
| NRCIA_CreatedUser_DR | bigint |  | FK | SI | Created User |
| NRCIA_RowId | varchar |  |  | NO | - |
| NRCIA_UpdatedDate | date |  |  | SI | Updated Date |
| NRCIA_UpdatedTime | time |  |  | SI | Updated Time |
| NRCIA_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q84Q1 | - |  |  | SI | Date |
| Q84Q2 | - |  |  | SI | Time |
| Q84Q3 | - |  |  | SI | Checklist |
| Q84Q4 | - |  |  | SI | Catheter length at wedge (cm) |
| Q84Q5 | - |  |  | SI | Pulmonary capillary wedge pressure (mmHg) |
| Q84Q6 | - |  |  | SI | Comments |
| Q84Q7 | - |  |  | SI | Staff |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*