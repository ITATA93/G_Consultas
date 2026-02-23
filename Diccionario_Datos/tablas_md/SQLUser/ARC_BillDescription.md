# SQLUser.ARC_BillDescription

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BILLDESC_RowId | bigint | PK |  | NO | - |
| BILLDESC_Code | varchar |  |  | NO | Code |
| BILLDESC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| BILLDESC_CreatedDate | date |  |  | SI | Created Date |
| BILLDESC_CreatedTime | time |  |  | SI | Created Time |
| BILLDESC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| BILLDESC_DateFrom | date |  |  | SI | Date From |
| BILLDESC_DateTo | date |  |  | SI | Date To |
| BILLDESC_Default | varchar |  |  | SI | Default Flag |
| BILLDESC_Desc | varchar |  |  | NO | Description |
| BILLDESC_Owner | varchar |  |  | SI | Owner |
| BILLDESC_UpdatedDate | date |  |  | SI | Updated Date |
| BILLDESC_UpdatedTime | time |  |  | SI | Updated Time |
| BILLDESC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q30Q1 | - |  |  | SI | Nombre de Cuidador |
| Q30Q2 | - |  |  | SI | Parentesco del Cuidador |
| Q30Q3 | - |  |  | SI | Teléfono cuidador |
| Q30Q4 | - |  |  | SI | N° Integrante |
| Q30Q5 | - |  |  | SI | Detalle |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*