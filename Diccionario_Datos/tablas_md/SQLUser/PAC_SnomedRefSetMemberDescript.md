# SQLUser.PAC_SnomedRefSetMemberDescript

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SNORFSDSC_RowId | bigint | PK |  | NO | - |
| ChildQ11DR | - |  |  | SI | Child Reference: Add action(s) for postpartum pre-... |
| Q10Q1 | - |  |  | SI | Action order number |
| Q10Q2 | - |  |  | SI | Time stamp |
| Q10Q3 | - |  |  | SI | Action type |
| Q10Q4 | - |  |  | SI | Other (specify) |
| Q10Q5 | - |  |  | SI | By whom |
| Q10Q6 | - |  |  | SI | Notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| SNORFSDSC_AttribDesc_DR | bigint |  | FK | SI | Attribute Description |
| SNORFSDSC_AttribOrder | integer |  |  | SI | Attribute Order |
| SNORFSDSC_AttribType_DR | bigint |  | FK | SI | Attribute Type |
| SNORFSDSC_CreatedDate | date |  |  | SI | Created Date |
| SNORFSDSC_CreatedTime | time |  |  | SI | Created Time |
| SNORFSDSC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SNORFSDSC_RefSetMember_DR | bigint |  | FK | SI | Des Ref PACSnomedRefSetMember |
| SNORFSDSC_UpdatedDate | date |  |  | SI | Updated Date |
| SNORFSDSC_UpdatedTime | time |  |  | SI | Updated Time |
| SNORFSDSC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*