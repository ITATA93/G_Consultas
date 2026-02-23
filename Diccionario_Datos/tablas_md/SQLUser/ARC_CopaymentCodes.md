# SQLUser.ARC_CopaymentCodes

**Schema:** SQLUser
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| COPC_RowId | bigint | PK |  | NO | - |
| COPC_Code | varchar |  |  | NO | Code |
| COPC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| COPC_CreatedDate | date |  |  | SI | Created Date |
| COPC_CreatedTime | time |  |  | SI | Created Time |
| COPC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| COPC_Desc | varchar |  |  | NO | Description |
| COPC_Owner | varchar |  |  | SI | Owner |
| COPC_UpdatedDate | date |  |  | SI | Updated Date |
| COPC_UpdatedTime | time |  |  | SI | Updated Time |
| COPC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| QR119Q1 | - |  |  | SI | Vacunas |
| QR119Q2 | - |  |  | SI | Aplicación |
| QR119Q3 | - |  |  | SI | Fecha |
| QR119Q4 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*