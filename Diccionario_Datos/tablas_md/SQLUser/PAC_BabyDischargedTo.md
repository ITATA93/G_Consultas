# SQLUser.PAC_BabyDischargedTo

**Schema:** SQLUser
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BABYDT_RowId | bigint | PK |  | NO | - |
| BABYDT_Code | varchar |  |  | NO | Code |
| BABYDT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| BABYDT_CreatedDate | date |  |  | SI | Created Date |
| BABYDT_CreatedTime | time |  |  | SI | Created Time |
| BABYDT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| BABYDT_DateFrom | date |  |  | SI | Date From |
| BABYDT_DateTo | date |  |  | SI | Date To |
| BABYDT_Desc | varchar |  |  | NO | Description |
| BABYDT_Owner | varchar |  |  | SI | Owner |
| BABYDT_UpdatedDate | date |  |  | SI | Updated Date |
| BABYDT_UpdatedTime | time |  |  | SI | Updated Time |
| BABYDT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q12Q1 | - |  |  | SI | Date |
| Q12Q2 | - |  |  | SI | Time |
| Q12Q3 | - |  |  | SI | Dressing status |
| Q12Q4 | - |  |  | SI | Insertion site check |
| Q12Q5 | - |  |  | SI | Actions performed |
| Q12Q6 | - |  |  | SI | Assessment notes |
| Q12Q7 | - |  |  | SI | Assessment performed by |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*