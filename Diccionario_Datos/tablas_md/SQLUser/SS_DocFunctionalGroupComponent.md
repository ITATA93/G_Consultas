# SQLUser.SS_DocFunctionalGroupComponent

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SSDOCCOM_ParRef | bigint | PK |  | NO | SSDocFunctionalGroup Parent Reference |
| SSDOCCOM_Childsub | double |  |  | NO | Childsub |
| SSDOCCOM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SSDOCCOM_Component_DR | bigint |  | FK | NO | Des Ref to Component |
| SSDOCCOM_CreatedDate | date |  |  | SI | Created Date |
| SSDOCCOM_CreatedTime | time |  |  | SI | Created Time |
| SSDOCCOM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SSDOCCOM_DateFrom | date |  |  | SI | Date From |
| SSDOCCOM_DateTo | date |  |  | SI | Date To |
| SSDOCCOM_RowId | varchar |  |  | NO | - |
| SSDOCCOM_UpdatedDate | date |  |  | SI | Updated Date |
| SSDOCCOM_UpdatedTime | time |  |  | SI | Updated Time |
| SSDOCCOM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*