# SQLUser.SS_GroupRBRestrictions

**Schema:** SQLUser
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RB_ParRef | bigint | PK |  | NO | SS_Group Parent Reference |
| RB_CTLOC_DR | bigint |  | FK | SI | Des CTLOC |
| RB_Childsub | double |  |  | NO | Childsub |
| RB_LineCode | varchar |  |  | SI | LineCode |
| RB_LineData | varchar |  |  | SI | LineData |
| RB_NumberOfFields | double |  |  | SI | Number Of Fields |
| RB_PatientType | varchar |  |  | SI | PatientType |
| RB_RefHosp_DR | bigint |  | FK | SI | Des Ref Refer Hosp |
| RB_Resource_DR | bigint |  | FK | SI | Des Ref Resource |
| RB_RowId | varchar |  |  | NO | - |
| RB_ServiceSet_DR | bigint |  | FK | SI | Des Ref ServiceSet |
| RB_Service_DR | bigint |  | FK | SI | Des Ref Service |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*