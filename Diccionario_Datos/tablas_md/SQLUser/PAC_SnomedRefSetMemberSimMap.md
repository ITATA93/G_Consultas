# SQLUser.PAC_SnomedRefSetMemberSimMap

**Schema:** SQLUser
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SNORFSSM_RowId | bigint | PK |  | NO | - |
| ChildQ08DR | - |  |  | SI | Child Reference: Add clinicians present |
| Q20Q1 | - |  |  | SI | Action order number |
| Q20Q2 | - |  |  | SI | Time stamp |
| Q20Q3 | - |  |  | SI | Action type |
| Q20Q4 | - |  |  | SI | Other (specify) |
| Q20Q5 | - |  |  | SI | By whom |
| Q20Q6 | - |  |  | SI | Notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| SNORFSSM_CreatedDate | date |  |  | SI | Created Date |
| SNORFSSM_CreatedTime | time |  |  | SI | Created Time |
| SNORFSSM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SNORFSSM_MapTarget | varchar |  |  | SI | Map Target |
| SNORFSSM_RefSetMember_DR | bigint |  | FK | SI | Des Ref PACSnomedRefSetMember |
| SNORFSSM_UpdatedDate | date |  |  | SI | Updated Date |
| SNORFSSM_UpdatedTime | time |  |  | SI | Updated Time |
| SNORFSSM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*