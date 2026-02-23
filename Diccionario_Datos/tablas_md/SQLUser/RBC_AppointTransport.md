# SQLUser.RBC_AppointTransport

**Schema:** SQLUser
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de RB**. Parámetros de módulos RB.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| APTR_RowId | bigint | PK |  | NO | - |
| APTR_Adress | varchar |  |  | SI | Adress |
| APTR_Code | varchar |  |  | NO | Code |
| APTR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| APTR_ContactMethod | varchar |  |  | SI | Contact Methods |
| APTR_CreatedDate | date |  |  | SI | Created Date |
| APTR_CreatedTime | time |  |  | SI | Created Time |
| APTR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| APTR_DateFrom | date |  |  | SI | Date From |
| APTR_DateTo | date |  |  | SI | Date To |
| APTR_Desc | varchar |  |  | NO | Description |
| APTR_Email | varchar |  |  | SI | Email |
| APTR_Fax | varchar |  |  | SI | Fax |
| APTR_Owner | varchar |  |  | SI | Owner |
| APTR_Phone | varchar |  |  | SI | Phone |
| APTR_UpdatedDate | date |  |  | SI | Updated Date |
| APTR_UpdatedTime | time |  |  | SI | Updated Time |
| APTR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*