# SQLUser.PAC_SnomedRefSetMemberLanguage

**Schema:** SQLUser
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SNORFSLAN_RowId | bigint | PK |  | NO | - |
| ChildQ12DR | - |  |  | SI | Child Reference: Add action(s) |
| Q11Q1 | - |  |  | SI | Action order number |
| Q11Q2 | - |  |  | SI | Time stamp |
| Q11Q3 | - |  |  | SI | Action type |
| Q11Q4 | - |  |  | SI | Other (specify) |
| Q11Q5 | - |  |  | SI | By whom |
| Q11Q6 | - |  |  | SI | Notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| SNORFSLAN_Acceptability_DR | bigint |  | FK | SI | Acceptability |
| SNORFSLAN_CreatedDate | date |  |  | SI | Created Date |
| SNORFSLAN_CreatedTime | time |  |  | SI | Created Time |
| SNORFSLAN_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SNORFSLAN_RefSetMember_DR | bigint |  | FK | SI | Des Ref PACSnomedRefSetMember |
| SNORFSLAN_UpdatedDate | date |  |  | SI | Updated Date |
| SNORFSLAN_UpdatedTime | time |  |  | SI | Updated Time |
| SNORFSLAN_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*