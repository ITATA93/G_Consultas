# SQLUser.ORC_AnaestAgent

**Schema:** SQLUser
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ANAGN_RowId | bigint | PK |  | NO | - |
| ANAGN_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCIM |
| ANAGN_Code | varchar |  |  | NO | An. Agent Code |
| ANAGN_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ANAGN_CreatedDate | date |  |  | SI | Created Date |
| ANAGN_CreatedTime | time |  |  | SI | Created Time |
| ANAGN_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ANAGN_DateFrom | date |  |  | SI | Date From |
| ANAGN_DateTo | date |  |  | SI | Date To |
| ANAGN_Desc | varchar |  |  | NO | An.Agent Description |
| ANAGN_General | varchar |  |  | SI | Checkbox for Spinal Restriction |
| ANAGN_Local | varchar |  |  | SI | Checkbox for Epidural Restriction |
| ANAGN_Method_DR | bigint |  | FK | SI | Des Ref Method |
| ANAGN_Owner | varchar |  |  | SI | Owner |
| ANAGN_UpdatedDate | date |  |  | SI | Updated Date |
| ANAGN_UpdatedTime | time |  |  | SI | Updated Time |
| ANAGN_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q52Q1 | - |  |  | SI | Shoulder instability |
| Q52Q2 | - |  |  | SI | Left |
| Q52Q3 | - |  |  | SI | Right |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*