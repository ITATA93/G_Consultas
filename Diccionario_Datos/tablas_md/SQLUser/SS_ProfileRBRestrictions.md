# SQLUser.SS_ProfileRBRestrictions

**Schema:** SQLUser
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RB_ParRef | bigint | PK |  | NO | Parent table |
| RB_CTLOC_DR | bigint |  | FK | SI | Location |
| RB_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| RB_DoNotAllowOverbooking | varchar |  |  | SI | Do not Allow Overbooking Flag |
| RB_LineCode | varchar |  |  | SI | Line Code |
| RB_LineData | varchar |  |  | SI | Line Data |
| RB_NumberOfFields | double |  |  | SI | Number Of Fields |
| RB_PatientType | varchar |  |  | SI | Patient Type |
| RB_RefHosp_DR | bigint |  | FK | SI | Referring Hospital |
| RB_Resource_DR | bigint |  | FK | SI | Resource |
| RB_RowID | varchar |  |  | NO | - |
| RB_ServiceSet_DR | bigint |  | FK | SI | Service Set |
| RB_Service_DR | bigint |  | FK | SI | Service |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*