# SQLUser.PAC_CarerAvailability

**Schema:** SQLUser
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CARAVL_RowId | bigint | PK |  | NO | - |
| CARAVL_CareTyp | varchar |  |  | SI | Care Type codes |
| CARAVL_Code | varchar |  |  | SI | Code |
| CARAVL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CARAVL_CreatedDate | date |  |  | SI | Created Date |
| CARAVL_CreatedTime | time |  |  | SI | Created Time |
| CARAVL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CARAVL_DateFrom | date |  |  | SI | Date From |
| CARAVL_DateTo | date |  |  | SI | Date To |
| CARAVL_Default | varchar |  |  | SI | Default |
| CARAVL_Desc | varchar |  |  | SI | Description |
| CARAVL_DischargeType | varchar |  |  | SI | Discharge Type Codes |
| CARAVL_NationalCode | varchar |  |  | SI | National Code |
| CARAVL_Owner | varchar |  |  | SI | Owner |
| CARAVL_UpdatedDate | date |  |  | SI | Updated Date |
| CARAVL_UpdatedTime | time |  |  | SI | Updated Time |
| CARAVL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ16DR | - |  |  | SI | Child Reference: Carbohydrate |
| Q15Q1 | - |  |  | SI | Items |
| Q15Q2 | - |  |  | SI | Likes and dislikes |
| Q15Q3 | - |  |  | SI | Comments |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*