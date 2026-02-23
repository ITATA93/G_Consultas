# SQLUser.SS_UserBillingTaskAssign

**Schema:** SQLUser
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BTA_ParRef | bigint | PK |  | NO | SS_User Parent Reference |
| BTA_BillingTask | varchar |  |  | SI | Billing Task |
| BTA_Childsub | double |  |  | NO | Childsub |
| BTA_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| BTA_DateFrom | date |  |  | SI | Date From |
| BTA_DateTo | date |  |  | SI | Date To |
| BTA_RowId | varchar |  |  | NO | - |
| BTA_User_DR | bigint |  | FK | SI | Des Ref SSUser |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*