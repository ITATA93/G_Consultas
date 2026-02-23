# SQLUser.ARC_InsTypeParticipants

**Schema:** SQLUser
**Columnas:** 23
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Seguros**. Planes y convenios. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PATCP_ParRef | bigint | PK |  | NO | ARC_InsuranceType Parent Reference |
| ChildQ20DR | - |  |  | SI | Child Reference: Desarrollo Psicomotor |
| PATCP_CapbId | varchar |  |  | SI | CapabilityId |
| PATCP_CapbId2 | varchar |  |  | SI | SecondaryCapabilityId |
| PATCP_CapbName | varchar |  |  | SI | CapabilityName |
| PATCP_CapbRoleCde | varchar |  |  | SI | CapabilityRoleCde |
| PATCP_CapbVerId | varchar |  |  | SI | CapabilityVersionId |
| PATCP_Childsub | double |  |  | NO | Childsub |
| PATCP_ContactNum | varchar |  |  | SI | ParticipantContactNum |
| PATCP_CreatedDate | date |  |  | SI | Created Date |
| PATCP_CreatedTime | time |  |  | SI | Created Time |
| PATCP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PATCP_DateUpdated | date |  |  | SI | DateUpdated |
| PATCP_ID | varchar |  |  | SI | ParticipantId |
| PATCP_Name | varchar |  |  | SI | ParticipantName |
| PATCP_RowId | varchar |  |  | NO | - |
| PATCP_Type | varchar |  |  | SI | ParticipantType |
| PATCP_UpdatedDate | date |  |  | SI | Updated Date |
| PATCP_UpdatedTime | time |  |  | SI | Updated Time |
| PATCP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q86Q1 | - |  |  | SI | Evaluación |
| Q86Q2 | - |  |  | SI | Comentarios (Texto libre) |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*