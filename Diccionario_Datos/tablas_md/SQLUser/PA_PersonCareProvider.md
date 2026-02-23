# SQLUser.PA_PersonCareProvider

**Schema:** SQLUser
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CP_ParRef | bigint | PK |  | NO | PA_Person Parent Reference |
| CP_CancelReason | varchar |  |  | SI | CancelReason |
| CP_CareProv_DR | varchar |  | FK | SI | Des Ref CareProv |
| CP_Childsub | double |  |  | NO | Childsub |
| CP_DateFrom | date |  |  | SI | DateFrom |
| CP_DateTo | date |  |  | SI | DateTo |
| CP_RespUnit_DR | bigint |  | FK | SI | Des Ref RespUnit |
| CP_Role_DR | bigint |  | FK | SI | Multidisciplinary Role |
| CP_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*