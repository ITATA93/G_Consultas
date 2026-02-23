# SQLUser.PAC_SnomedRefSetMemberModDep

**Schema:** SQLUser
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SNORFSMD_RowId | bigint | PK |  | NO | - |
| ChildQ20DR | - |  |  | SI | Child Reference: Add action(s) for Dummy1 |
| Q12Q1 | - |  |  | SI | Action order number |
| Q12Q2 | - |  |  | SI | Time stamp |
| Q12Q3 | - |  |  | SI | Action type |
| Q12Q4 | - |  |  | SI | By whom |
| Q12Q5 | - |  |  | SI | Notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| SNORFSMD_CreatedDate | date |  |  | SI | Created Date |
| SNORFSMD_CreatedTime | time |  |  | SI | Created Time |
| SNORFSMD_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SNORFSMD_RefSetMember_DR | bigint |  | FK | SI | Des Ref PACSnomedRefSetMember |
| SNORFSMD_SourceEffDate | date |  |  | SI | Source Effective Date |
| SNORFSMD_TargetEffDate | date |  |  | SI | Target Effective Date |
| SNORFSMD_UpdatedDate | date |  |  | SI | Updated Date |
| SNORFSMD_UpdatedTime | time |  |  | SI | Updated Time |
| SNORFSMD_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*