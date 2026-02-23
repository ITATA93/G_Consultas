# SQLUser.RB_ApptSchemaAppt

**Schema:** SQLUser
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| AP_ParRef | bigint | PK |  | NO | RB_ApptSchema Parent Reference |
| AP_ApptNumber | double |  |  | SI | ApptNumber |
| AP_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| AP_Childsub | double |  |  | NO | Childsub |
| AP_ConsultCateg_DR | bigint |  | FK | SI | Des Ref ConsultCateg |
| AP_FreqInterval | varchar |  |  | SI | FreqInterval |
| AP_Frequency | double |  |  | SI | Frequency |
| AP_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| AP_Resource_DR | bigint |  | FK | SI | Des Ref Resource |
| AP_RowId | varchar |  |  | NO | - |
| AP_Service_DR | bigint |  | FK | SI | Des Ref Service |
| AP_SessionType_DR | bigint |  | FK | SI | Des Ref SessionType |
| AP_WLPriority_DR | bigint |  | FK | SI | Des Ref WLPriority |
| AP_WLStatus_DR | bigint |  | FK | SI | Des Ref WLStatus |
| AP_WLType_DR | bigint |  | FK | SI | Des Ref WLType |
| AP_WL_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| AP_WL_CareProv_DR | varchar |  | FK | SI | Des Ref CareProv |
| AP_WL_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*