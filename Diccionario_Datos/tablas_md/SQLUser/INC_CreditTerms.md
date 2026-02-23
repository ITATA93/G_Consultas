# SQLUser.INC_CreditTerms

**Schema:** SQLUser
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Incidentes**. Reportes de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CRT_RowId | bigint | PK |  | NO | - |
| CRT_Code | varchar |  |  | NO | Code |
| CRT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CRT_CreatedDate | date |  |  | SI | Created Date |
| CRT_CreatedTime | time |  |  | SI | Created Time |
| CRT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CRT_Desc | varchar |  |  | NO | Description |
| CRT_Owner | varchar |  |  | SI | Owner |
| CRT_UpdatedDate | date |  |  | SI | Updated Date |
| CRT_UpdatedTime | time |  |  | SI | Updated Time |
| CRT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q60Q1 | - |  |  | SI | Central intravenous tissue plasminogen activator (... |
| Q60Q2 | - |  |  | SI | Central intravenous tissue plasminogen activator (... |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*